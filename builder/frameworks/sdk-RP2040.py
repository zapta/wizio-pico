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
    dev_compiler(env)
    dev_create_template(env)    
    add_flags(env) 
    env.Append( 
        CPPPATH = [ 
            join(env.framework_dir, sdk, "include"), # SDK
            join(env.framework_dir, sdk, "boards"),  # BOARDS
        ],
    )
    dev_finalize(env)

