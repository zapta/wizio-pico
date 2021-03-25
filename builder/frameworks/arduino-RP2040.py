# WizIO 2021 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

from os.path import join
from SCons.Script import DefaultEnvironment, Builder
from common import *

def dev_init(env, platform):
    env.platform = platform    
    env.framework_dir = env.PioPlatform().get_package_dir("framework-wizio-pico")    
    env.libs = libs = []     
    sdk = dev_sdk(env)  
    dev_compiler(env, 'ARDUINO')
    dev_create_template(env)
    add_flags(env) 
    core = env.BoardConfig().get("build.core")
    variant= env.BoardConfig().get("build.variant")  
    env.Append(
        CPPDEFINES = [ "ARDUINO=200" ],
        CPPPATH = [   
            join(env.framework_dir, sdk, "include"),     # SDK      
            join(env.framework_dir, platform, platform), # ARDUINO
            join(env.framework_dir, platform, "cores", core),            
            join(env.framework_dir, platform, "variants", variant), 
        ],
        LIBSOURCE_DIRS = [ join(env.framework_dir, platform, "libraries", core) ], 
        LIBPATH        = [ join(env.framework_dir, platform, "libraries", core) ],         
    )
    libs.append( env.BuildLibrary( 
        join( "$BUILD_DIR", platform, "arduino" ),   
        join( env.framework_dir, platform, platform ) ) )     
    libs.append( env.BuildLibrary( 
        join( "$BUILD_DIR", platform, "arduino", "cores", core ),         
        join( env.framework_dir, platform, "cores", core ) ) )    
    libs.append( env.BuildLibrary( 
        join( "$BUILD_DIR", platform, "arduino", "variants", variant ),      
        join( env.framework_dir, platform, "variants", variant ) ) )  
    dev_finalize(env)

