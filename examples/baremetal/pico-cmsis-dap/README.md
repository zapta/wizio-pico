# CMSIS-DAP - Raspberry Pi Pico RP2040 

Original idea: [Peter Lawrence ( majbthrd )](https://github.com/majbthrd/pico-debug)

CMSIS-DAP use Core 1 and TinyUSB for USB communication with OpenOCD to GDB

No hardware is added... all in one...

## How to

```c
int main(void)
{
    extern void dap_init(void);
    dap_init(); // run dap ( before all ) cmsis-dap @ core 1

    /* 
         YOUR CODE 
    */
    
```

add to platformio.ini

```ini
build_flags = 
    -D PICO_STDIO_UART              ; for printf()
    -D PICO_USB                     ; load tyniusb for OpenOCD @ cmsis-dap
    -D CFG_TUD_HID=1                ; enable HID
    -D CFG_TUD_HID_EP_BUFSIZE=64    ; set HID size

lib_deps = dap                      ; load library

debug_tool = cmsis-dap              ; select tool

board_build.optimization = -O0
```

Compile, Upload, set bleakpoints, F5 for Debug...( tested on Windows 7/10 )

_must work and with Arduino ( not tested )_


## OpenOCD
For [MacOS](https://github.com/Wiz-IO/tool-pico-openocd/tree/main/darwin_x86_64) and [Linux](https://github.com/Wiz-IO/tool-pico-openocd/tree/main/linux_x86_64) read links

**The platform Debuger is a work in progress, there may be bugs...**