# WizIO 2021 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

from os.path import join
from SCons.Script import DefaultEnvironment, Builder
from platformio.builder.tools.piolib import PlatformIOLibBuilder
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
        CPPPATH    = [ 
            join(env.framework_dir, sdk, "include"), # SDK
            join(env.framework_dir, sdk, "boards"),  # BOARDS
        ],
        LINKFLAGS = [ "-Wl,-wrap,malloc", "-Wl,-wrap,free", "-Wl,-wrap,calloc", ],    
    )    
# SDK           
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, sdk),   
        join(env.framework_dir, sdk),
        src_filter=[ "+<*>", "-<boot_stage2>", 
            "-<pico/pico_standard_link/crt0.S>",    # build_flags =
            "-<pico/pico_stdio_semihosting>",       #   -D PICO_STDIO_SEMIHOSTING
            "-<pico/pico_stdio_uart>",              #   -D PICO_STDIO_UART
            "-<pico/pico_stdio_usb>",               #   -D PICO_STDIO_USB  
            "-<pico/pico_float>",                   #   -D PICO_FLOAT_SUPPORT_ROM_V1
            "-<pico/pico_double>",                  #   -D PICO_DOUBLE_SUPPORT_ROM_V1
            "-<pico/pico_printf>",                  #   -D PICO_PRINTF_PICO
            "-<lib/tinyusb>",            
        ]
    )) 
# WIZIO    
    libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", platform, "wizio"),   
        join(env.framework_dir, "wizio") ) )         
# FINALIZE        
    add_common(env)
    set_bynary_type(env)
    env.Append(LIBS = libs)  
