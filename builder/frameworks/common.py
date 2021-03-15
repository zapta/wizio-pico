# WizIO 2021 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

from SCons.Script import DefaultEnvironment, Builder, ARGUMENTS
import os, json, tempfile, shutil
from os.path import join, normpath, basename
from shutil import copyfile
from colorama import Fore
from subprocess import check_output, CalledProcessError, call, Popen, PIPE
from uf2conv import upload_app

def dev_uploader(target, source, env):
    drive = env.get("UPLOAD_PORT")
    if None == drive:
        drive = env.get("BUILD_DIR") + '/'
    return upload_app(join(env.get("BUILD_DIR"), env.get("PROGNAME")) + '.bin', drive, env.address)

def do_copy(src, dst, name):
    if False == os.path.isfile( join(dst, name) ):
        copyfile( join(src, name), join(dst, name) )

def do_mkdir(path, name):
    dir = join(path, name)
    if False == os.path.isdir( dir ):
        try:
            os.mkdir(dir)
        except OSError:
            print ("[ERROR] Creation of the directory %s failed" % dir)
            exit(1)
    return dir

def dev_create_template(env):
    src = join(env.PioPlatform().get_package_dir("framework-wizio-pico"), "templates")
    dst = do_mkdir( env.subst("$PROJECT_DIR"), "include" )

    if "freertos" in env.GetProjectOption("lib_deps", []):
        do_copy(src, dst, "FreeRTOSConfig.h")

    if "fatfs"    in env.GetProjectOption("lib_deps", []):
        do_copy(src, dst, "ffconf.h")

    if 'APPLICATION'== env.get("PROGNAME"):
        dst = do_mkdir( env.subst("$PROJECT_DIR"), join("include", "pico") )
        do_copy(src, dst, "config_autogen.h" )

        dst = join(env.subst("$PROJECT_DIR"), "src")
        if False == os.path.isfile( join(dst, "main.cpp") ):
            do_copy(src, dst, "main.c" )

def dev_sdk(env):
    env.sdk = env.BoardConfig().get("build.sdk", "SDK110") # get/set default sdk
    print()
    print( Fore.BLUE + "%s RASPBERRYPI PI PICO RP2040 ( PICO - %s )" % (env.platform.upper(), env.sdk.upper()) )
    return env.sdk

def dev_compiler(env, application_name = 'APPLICATION'):
    env.Replace(
        BUILD_DIR = env.subst("$BUILD_DIR").replace("\\", "/"),
        AR="arm-none-eabi-ar",
        AS="arm-none-eabi-as",
        CC="arm-none-eabi-gcc",
        GDB="arm-none-eabi-gdb",
        CXX="arm-none-eabi-g++",
        OBJCOPY="arm-none-eabi-objcopy",
        RANLIB="arm-none-eabi-ranlib",
        SIZETOOL="arm-none-eabi-size",
        ARFLAGS=["rc"],
        SIZEPROGREGEXP=r"^(?:\.text|\.data|\.bootloader)\s+(\d+).*",
        SIZEDATAREGEXP=r"^(?:\.data|\.bss|\.noinit)\s+(\d+).*",
        SIZECHECKCMD="$SIZETOOL -A -d $SOURCES",
        SIZEPRINTCMD='$SIZETOOL --mcu=$BOARD_MCU -C -d $SOURCES',
        PROGSUFFIX=".elf",
        PROGNAME = application_name
    )
    env.cortex = ["-mcpu=cortex-m0plus", "-mthumb"]

def get_nano(env):
    disable_nano = env.BoardConfig().get("build.disable_nano", "by defaut nano is enabled") #
    nano = []
    if disable_nano == "true":
        nano = ["-specs=nano.specs", "-u", "_printf_float", "-u", "_scanf_float" ]
    return nano

def add_flags(env, def_heap_size = "2048"):
    env.heap_size = env.BoardConfig().get("build.heap", def_heap_size)
    optimization = env.BoardConfig().get("build.optimization", "-Os")
    stack_size = env.BoardConfig().get("build.stack", "2048")
    print('  - OPTIMIZATION :', optimization)
    print('  - HEAP         :', env.heap_size)
    print('  - STACK        :', stack_size)
    env.Append(
        ASFLAGS=[ env.cortex, "-x", "assembler-with-cpp" ],
        CPPPATH = [
            join("$PROJECT_DIR", "src"),
            join("$PROJECT_DIR", "lib"),
            join("$PROJECT_DIR", "include"),
        ],
        CPPDEFINES = [
            "PICO_ON_DEVICE=1",
            "PICO_HEAP_SIZE="  + env.heap_size,
            "PICO_STACK_SIZE=" + stack_size,
        ],
        CFLAGS = [
            env.cortex,
            optimization,
            "-fdata-sections",
            "-ffunction-sections",
            "-Wall",
            "-Wfatal-errors",
            "-Wno-unused-function",
            "-Wno-unused-but-set-variable",
            "-Wno-unused-variable",
            "-Wno-unused-value",
            "-Wno-sign-compare",
        ],
        CXXFLAGS = [
            "-fno-rtti",
            "-fno-exceptions",
            "-fno-non-call-exceptions",
            "-fno-use-cxa-atexit",
            "-fno-threadsafe-statics",
        ],
        CCFLAGS = [
            env.cortex,
            optimization,
            "-fdata-sections",
            "-ffunction-sections",
            "-Wall",
            "-Wfatal-errors",
            "-Wno-unused-function",
            "-Wno-unused-but-set-variable",
            "-Wno-unused-variable",
            "-Wno-unused-value",
            "-Wno-sign-compare",         
        ],
        LINKFLAGS = [
            env.cortex,
            optimization,
            "-nostartfiles",
            "-Wall",
            "-Wfatal-errors",
            "-fno-use-cxa-atexit",
            "-fno-zero-initialized-in-bss",
            "-Xlinker", "--gc-sections",
            "-Wl,--gc-sections",
            "--entry=_entry_point",
            get_nano(env)
        ],
        LIBSOURCE_DIRS = [ join(env.framework_dir, "library") ],
        LIBPATH        = [ join(env.framework_dir, "library") ],
        LIBS = ['m', 'gcc'],
        BUILDERS = dict(
            ElfToBin = Builder(
                action = env.VerboseAction(" ".join([
                    "$OBJCOPY",
                    "-O",
                    "binary",
                    "$SOURCES",
                    "$TARGET",
                ]), "Building $TARGET"),
                suffix = ".bin"
            )
        ),
        UPLOADCMD = dev_uploader
    )

def add_common(env):
    boot = env.BoardConfig().get("build.boot", "w25q080") # get boot
    print('  - BOOT         :', boot)
    env.libs.append( env.BuildLibrary(
        join("$BUILD_DIR", env.platform, "wizio", "boot2"),
        join(env.framework_dir, "wizio", "boot2", boot) ) )

    if "PICO_STDIO_USB" in env.get("CPPDEFINES") and "tinyusb" in env.GetProjectOption("lib_deps", []):
        env.Append(
            CPPDEFINES = [
                "CFG_TUSB_MCU=OPT_MCU_RP2040",
                "CFG_TUSB_OS=OPT_OS_PICO",
                "CFG_TUSB_DEBUG=0",
            ],
            CPPPATH = [ join(join(env.framework_dir, "library", "tinyusb"), "src") ]
        )
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_fix"),
            join(env.framework_dir, env.sdk, "pico", "pico_fix") ) )
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_stdio_usb"),
            join(env.framework_dir, env.sdk, "pico", "pico_stdio_usb") ) )

    if "freertos" in env.GetProjectOption("lib_deps", []):
        env.Append(
            CPPDEFINES = [ "USE_FREERTOS"],
            CPPPATH    = [ join(join(env.framework_dir, "library", "freertos"), "include") ]
        )

    if "PICO_FLOAT_SUPPORT_ROM_V1" in env.get("CPPDEFINES"):
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_float"),
            join(env.framework_dir, env.sdk, "pico", "pico_float") ) )

    if "PICO_DOUBLE_SUPPORT_ROM_V1" in env.get("CPPDEFINES"):
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, env.sdk, "pico", "pico_double"),
            join(env.framework_dir, env.sdk, "pico", "pico_double") ) )

    if 'ARDUINO'== env.get("PROGNAME"):
        return #########################################################################

    if "PICO_STDIO_UART" in env.get("CPPDEFINES"):
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, "pico_stdio_uart"),
            join(env.framework_dir, env.sdk, "pico", "pico_stdio_uart") ) )

    if "PICO_STDIO_SEMIHOSTING" in env.get("CPPDEFINES"):
        env.Append( CPPPATH = [ join(env.framework_dir, env.sdk, "pico", "pico_stdio_semihosting", "include") ] )
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, "pico_stdio_semihosting"),
            join(env.framework_dir, env.sdk, "pico", "pico_stdio_semihosting") ) )

    if "PICO_PRINTF_PICO" in env.get("CPPDEFINES"):
        env.libs.append( env.BuildLibrary(
            join("$BUILD_DIR", env.platform, "pico_printf"),
            join(env.framework_dir, env.sdk, "pico", "pico_printf") ) )

def set_bynary_type(env):
    env.address = env.BoardConfig().get("build.address", "empty")   # get uf2 start address
    linker = env.BoardConfig().get("build.linker", "empty")         # get linker srcipt
    bynary_type = env.BoardConfig().get("build.bynary_type", 'default')

    if 'copy_to_ram' == bynary_type:
        if "empty" == env.address: env.address = '0x10000000'
        if "empty" == linker: linker = 'memmap_copy_to_ram.ld'
        env.Append(
            LDSCRIPT_PATH = join(env.framework_dir, env.sdk, "pico", "pico_standard_link", linker),
            CPPDEFINES = ['PICO_COPY_TO_RAM']
        )
    elif 'no_flash' == bynary_type:
        if "empty" == env.address: env.address = '0x20000000'
        if "empty" == linker: linker = 'memmap_no_flash.ld'
        env.Append(
            LDSCRIPT_PATH = join(env.framework_dir, env.sdk, "pico", "pico_standard_link", linker),
            CPPDEFINES = ['PICO_NO_FLASH']
        )
        pass
    #elif 'blocked_ram' == bynary_type: # ?????????
    else: #default
        if "empty" == env.address: env.address = '0x10000000'
        if "empty" == linker: linker = 'memmap_default.ld'
        env.Append(
            LDSCRIPT_PATH = join(env.framework_dir, env.sdk, "pico", "pico_standard_link", linker),
        )
    print('  - BINARY TYPE  :' , bynary_type, '[', linker, ' ', env.address, ']'  )
    print()


