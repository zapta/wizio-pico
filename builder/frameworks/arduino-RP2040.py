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
        CPPDEFINES = [ platform.upper()+"=200", ],
        CPPPATH = [   
            join(env.framework_dir, sdk, "include"),     # SDK      
            join(env.framework_dir, platform, platform), # ARDUINO
            join(env.framework_dir, platform, "cores", core),            
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
#WIZIO 
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, "wizio"),   
        join(env.framework_dir, "wizio") ) )          
# SDK 
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, sdk), 
        join(env.framework_dir, sdk),
        src_filter=[ "+<*>", "-<boot_stage2>", 
            "-<pico/pico_standard_link>",       # build_flags =
            "-<pico/pico_float>",               #   -D PICO_FLOAT_SUPPORT_ROM_V1
            "-<pico/pico_double>",              #   -D PICO_DOUBLE_SUPPORT_ROM_V1
            "-<pico/pico_printf>",              #   -D PICO_PRINTF_PICO               
            "-<pico/pico_stdio_semihosting>",            
            "-<pico/pico_stdio_uart>",          
            "-<pico/pico_stdio_usb>",                          
            "-<pico/pico_stdio>",            
            "-<pico/pico_malloc>", 
            "-<lib/tinyusb>",           
        ]
    ))   

# FINALIZE      
    add_common(env)
    set_bynary_type(env)
    env.Append(LIBS = libs)  

