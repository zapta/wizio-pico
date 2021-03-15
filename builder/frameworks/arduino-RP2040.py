# WizIO 2021 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

import os
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
    add_flags(env, def_heap_size = '65536') 
    core = env.BoardConfig().get("build.core")
    variant= env.BoardConfig().get("build.variant")  
    env.Append(
        CPPDEFINES = [ platform.upper()+"=200", ], # "OS_HEAP_SIZE=" + env.heap_size,
        CPPPATH = [   
            join(env.framework_dir, sdk, "include"),     # SDK      
            join(env.framework_dir, platform, platform), # ARDUINO
            join(env.framework_dir, platform, "cores", core), 
            join(env.framework_dir, platform, "cores", core, 'newlib'),            
            join(env.framework_dir, platform, "variants", variant), 
        ],
        LIBSOURCE_DIRS = [ join(env.framework_dir, platform, "libraries", core) ], 
        LIBPATH        = [ join(env.framework_dir, platform, "libraries", core) ],         
    )
#ARDUINO 
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, "arduino"),   
        join(env.framework_dir, platform, platform) ) )     
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, "cores", core),         
        join(env.framework_dir, platform, "cores", core) ) )    
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, "variants", variant),      
        join(env.framework_dir, platform, "variants", variant) ) )  
# SDK 
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, sdk), 
        join(env.framework_dir, sdk),
        src_filter=[ "+<*>", "-<boot_stage2>", 
            "-<pico/pico_standard_link>",
            "-<pico/pico_malloc",
            "-<pico/pico_printf>",               
            "-<pico/pico_stdio_semihosting>",            
            "-<pico/pico_stdio_uart>",
            "-<pico/pico_stdio_usb>",
            "-<pico/pico_stdio>",                
            "-<pico/pico_fix>",    
            "-<pico/pico_float>",  
            "-<pico/pico_double>", 
            #"-<pico/pico_util>",
        ]
    ))   
# FINALIZE      
    add_common(env)
    env.Append(LIBS = libs)  
    set_bynary_type(env)

