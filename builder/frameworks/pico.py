# WizIO 2021 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

from os.path import join
from SCons.Script import DefaultEnvironment, Builder
from platformio.builder.tools.piolib import PlatformIOLibBuilder


def add_ops(env):
    tab = '  *'
    if "PICO_DOUBLE_SUPPORT_ROM_V1" in env.get("CPPDEFINES"):
        print(tab, 'PICO_DOUBLE_SUPPORT_ROM_V1')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_double"),
            join(env.framework_dir, env.sdk, "pico", "pico_double") ) )
        env.Append( LINKFLAGS = [    
                "-Wl,-wrap,wrapper_func __aeabi_drsub",
                "-Wl,-wrap,wrapper_func_d2 __aeabi_dsub",
                "-Wl,-wrap,wrapper_func_d2 __aeabi_dadd",
                "-Wl,-wrap,wrapper_func_d2 __aeabi_ddiv",
                "-Wl,-wrap,wrapper_func_d2 __aeabi_dmul",
                "-Wl,-wrap,wrapper_func __aeabi_cdrcmple",
                "-Wl,-wrap,wrapper_func __aeabi_cdcmple",
                "-Wl,-wrap,wrapper_func __aeabi_cdcmpeq",
                "-Wl,-wrap,wrapper_func __aeabi_dcmpeq",
                "-Wl,-wrap,wrapper_func __aeabi_dcmplt",
                "-Wl,-wrap,wrapper_func __aeabi_dcmple",
                "-Wl,-wrap,wrapper_func __aeabi_dcmpge",
                "-Wl,-wrap,wrapper_func __aeabi_dcmpgt",
                "-Wl,-wrap,wrapper_func __aeabi_dcmpun",
                "-Wl,-wrap,wrapper_func __aeabi_ui2d",
                "-Wl,-wrap,wrapper_func __aeabi_i2d",
                "-Wl,-wrap,wrapper_func __aeabi_d2iz",
                "-Wl,-wrap,wrapper_func __aeabi_d2uiz",
                "-Wl,-wrap,wrapper_func __aeabi_l2d",
                "-Wl,-wrap,wrapper_func __aeabi_ul2d",
                "-Wl,-wrap,wrapper_func __aeabi_d2lz",
                "-Wl,-wrap,wrapper_func __aeabi_d2ulz",
                "-Wl,-wrap,wrapper_func __aeabi_d2f",
                "-Wl,-wrap,wrapper_func_d1 sqrt",
                "-Wl,-wrap,wrapper_func cos",
                "-Wl,-wrap,wrapper_func sin",
                "-Wl,-wrap,wrapper_func sincos",
                "-Wl,-wrap,wrapper_func tan",
                "-Wl,-wrap,wrapper_func_d2 atan2",
                "-Wl,-wrap,wrapper_func_d1 exp",
                "-Wl,-wrap,wrapper_func_d1 log",
        ])             

    if "PICO_FLOAT_SUPPORT_ROM_V1" in env.get("CPPDEFINES"):
        print(tab, 'PICO_FLOAT_SUPPORT_ROM_V1')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_float"),
            join(env.framework_dir, env.sdk, "pico", "pico_float") ) )
        env.Append( LINKFLAGS = [    
                "-Wl,-wrap,wrapper_func __aeabi_frsub",
                "-Wl,-wrap,wrapper_func_f2 __aeabi_fsub",
                "-Wl,-wrap,wrapper_func_f2 __aeabi_fadd",
                "-Wl,-wrap,wrapper_func_f2 __aeabi_fdiv",
                "-Wl,-wrap,wrapper_func_f2 __aeabi_fmul",
                "-Wl,-wrap,wrapper_func __aeabi_cfrcmple",
                "-Wl,-wrap,wrapper_func __aeabi_cfcmple",
                "-Wl,-wrap,wrapper_func __aeabi_cfcmpeq",
                "-Wl,-wrap,wrapper_func __aeabi_fcmpeq",
                "-Wl,-wrap,wrapper_func __aeabi_fcmplt",
                "-Wl,-wrap,wrapper_func __aeabi_fcmple",
                "-Wl,-wrap,wrapper_func __aeabi_fcmpge",
                "-Wl,-wrap,wrapper_func __aeabi_fcmpgt",
                "-Wl,-wrap,wrapper_func __aeabi_fcmpun",
                "-Wl,-wrap,wrapper_func __aeabi_ui2f",
                "-Wl,-wrap,wrapper_func __aeabi_i2f",
                "-Wl,-wrap,wrapper_func __aeabi_f2iz",
                "-Wl,-wrap,wrapper_func __aeabi_f2uiz",
                "-Wl,-wrap,wrapper_func __aeabi_l2f",
                "-Wl,-wrap,wrapper_func __aeabi_ul2f",
                "-Wl,-wrap,wrapper_func __aeabi_f2lz",
                "-Wl,-wrap,wrapper_func __aeabi_f2ulz",
                "-Wl,-wrap,wrapper_func __aeabi_f2d",
                "-Wl,-wrap,wrapper_func_f1 sqrtf",
                "-Wl,-wrap,wrapper_func cosf",
                "-Wl,-wrap,wrapper_func sinf",
                "-Wl,-wrap,wrapper_func sincosf",
                "-Wl,-wrap,wrapper_func tanf",
                "-Wl,-wrap,wrapper_func_f2 atan2f",
                "-Wl,-wrap,wrapper_func_f1 expf",
                "-Wl,-wrap,wrapper_func_f1 logf",
        ]) 

    if "PICO_DIVIDER_HARDWARE" in env.get("CPPDEFINES"):
        print(tab, 'PICO_DIVIDER_HARDWARE')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_divider"),
            join(env.framework_dir, env.sdk, "pico", "pico_divider") ) )          
        env.Append( LINKFLAGS = [    
                "-Wl,-wrap,__aeabi_idiv",
                "-Wl,-wrap,__aeabi_idivmod",
                "-Wl,-wrap,__aeabi_uidiv",
                "-Wl,-wrap,__aeabi_uidivmod",
                "-Wl,-wrap,__aeabi_ldivmod",
                "-Wl,-wrap,__aeabi_uldivmod",
        ])    

    if "PICO_INT64_OPS_PICO" in env.get("CPPDEFINES"):  
        print(tab, 'PICO_INT64_OPS_PICO')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_int64_ops"),
            join(env.framework_dir, env.sdk, "pico", "pico_int64_ops") ) )                
        env.Append( LINKFLAGS = [    
                "-Wl,-wrap,wrapper_func __aeabi_lmul", 
        ])   

    if "PICO_BIT_OPS_PICO" in env.get("CPPDEFINES"):
        print(tab, 'PICO_BIT_OPS_PICO')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_bit_ops"),
            join(env.framework_dir, env.sdk, "pico", "pico_bit_ops") ) )        
        env.Append( LINKFLAGS = [    
                "-Wl,-wrap,__clz",
                "-Wl,-wrap,__clzl",
                "-Wl,-wrap,__clzsi2",
                "-Wl,-wrap,__ctzsi2",
                "-Wl,-wrap,__popcountsi2",
                "-Wl,-wrap,__clzll",
                "-Wl,-wrap,__clzdi2",
                "-Wl,-wrap,__ctzdi2",
                "-Wl,-wrap,__popcountdi2",
        ])        

    if "PICO_MEM_OPS_PICO" in env.get("CPPDEFINES"):
        print(tab, 'PICO_MEM_OPS_PICO')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_mem_ops"),
            join(env.framework_dir, env.sdk, "pico", "pico_mem_ops") ) )           
        env.Append( LINKFLAGS = [
                "-Wl,-wrap,__aeabi_memset",
                "-Wl,-wrap,__aeabi_memset4",
                "-Wl,-wrap,__aeabi_memset8",
                "-Wl,-wrap,__aeabi_memcpy4",
                "-Wl,-wrap,__aeabi_memcpy8",
                "-Wl,-wrap,__aeabi_memcpy",
                "-Wl,-wrap,memcpy",
                "-Wl,-wrap,memset",
        ])

    if "PICO_PRINTF_PICO" in env.get("CPPDEFINES"):
        print(tab, 'PICO_PRINTF_PICO')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_printf"),
            join(env.framework_dir, env.sdk, "pico", "pico_printf") ) )
        env.Append( LINKFLAGS = [
                "-Wl,-wrap,sprintf",
                "-Wl,-wrap,snprintf",
                "-Wl,-wrap,vsnprintf",
        ])

    if 'ARDUINO' == env.get("PROGNAME"): return #############

    if "PICO_STDIO_USB" in env.get("CPPDEFINES") or "PICO_STDIO_UART" in env.get("CPPDEFINES") or "PICO_STDIO_SEMIHOSTING" in env.get("CPPDEFINES"):
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_stdio"),
            join(env.framework_dir, env.sdk, "pico", "pico_stdio") ) )

    if "PICO_STDIO_USB" in env.get("CPPDEFINES"):
        print(tab, 'PICO_STDIO_USB')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_stdio_usb"),
            join(env.framework_dir, env.sdk, "pico", "pico_stdio_usb") ) )

    if "PICO_STDIO_UART" in env.get("CPPDEFINES"):
        print(tab, 'PICO_STDIO_UART')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_stdio_uart"),
            join(env.framework_dir, env.sdk, "pico", "pico_stdio_uart") ) )

    if "PICO_STDIO_SEMIHOSTING" in env.get("CPPDEFINES"):
        print(tab, 'PICO_STDIO_SEMIHOSTING')
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_stdio_semihosting"),
            join(env.framework_dir, env.sdk, "pico", "pico_stdio_semihosting") ) )        

    env.Append( LINKFLAGS = [ 
        "-Wl,-wrap,malloc", 
        "-Wl,-wrap,calloc", 
        "-Wl,-wrap,free",             
    ])   


def add_sdk(env):
    add_ops(env)
    if 'ARDUINO'!= env.get("PROGNAME"):
        new_delete = "+" 
        pico_malloc = '+'
    else:
        new_delete = "-"
        pico_malloc = '-'
        
    env.libs.append( env.BuildLibrary( 
        join("$BUILD_DIR", env.platform, env.sdk), 
        join(env.framework_dir, env.sdk),
        src_filter=[ "+<*>", 
            "-<boot_stage2>",      
            "-<pico/pico_bit_ops>",
            "-<pico/pico_divider>",
            "-<pico/pico_int64_ops>",
            "-<pico/pico_printf>",  
            "-<pico/pico_float>",              
            "-<pico/pico_double>",  
            "-<pico/pico_stdio>",             
            "-<pico/pico_stdio_usb>",  
            "-<pico/pico_stdio_uart>",              
            "-<pico/pico_stdio_semihosting>", 
            "-<pico/pico_mem_ops>",
            "-<pico/pico_standard_link/crt0.S>", 
            new_delete + "<pico/pico_standard_link/new_delete.cpp>",  
            pico_malloc + "<pico/pico_malloc>",                     
            "-<lib/tinyusb>",           
        ] ) )  