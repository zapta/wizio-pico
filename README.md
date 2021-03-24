## Raspberry Pi Pico RP2040 - PlatformIO ( Pico-SDK & Arduino ) (1.0.3)

**A few words in the beginning**
* **Version: 1.0.3** The project is a work in progress and is **very beta version** - there may be bugs...
* This project not an official platform and is based on [**pico-sdk**](https://github.com/raspberrypi/pico-sdk)
* **Systems support**
* * Windows, Linux, Darwin
* **PICO-SDK** _( the file organization has been restructured to be flexible and have a fast compilation )_
* * [ver 1.1.0 release](https://github.com/raspberrypi/pico-sdk/releases/tag/1.1.0) ( **default** )
* **Frameworks**
* * Baremetal ( pico-sdk, C/C++ ) _baremetal is just a name for pico-sdk here_
* * Arduino ( in progress... )
* **Libraries** [FreeRTOS](https://github.com/Wiz-IO/wizio-pico/wiki/COMMON#freertos), FatFS, littlefs ... etc
* Basic **[File System](https://github.com/Wiz-IO/wizio-pico/wiki/COMMON#file-system--vfs--virtual-file-system-)** ( RAM disk, FLASH disk, SD card )
* [**READ WIKI**](https://github.com/Wiz-IO/wizio-pico/wiki/) 
* [Framework code](https://github.com/Wiz-IO/framework-wizio-pico)
* [Baremetal Examples](https://github.com/Wiz-IO/wizio-pico/tree/main/examples/baremetal)
* [Arduino Examples](https://github.com/Wiz-IO/wizio-pico/tree/main/examples/arduino)

**Notes**
* Please [Re-Install](https://github.com/Wiz-IO/wizio-pico/blob/main/README.md#fast-uninstal--reinstal--do-this-and-install-again) the platform
* _I am in Home-Office, it's hard for me to test hardwares as SPI, I2C ... etc_

![pico](https://raw.githubusercontent.com/Wiz-IO/LIB/master/pico/a1.jpg)

## Install Platform
_Note: be sure [**git**](https://git-scm.com/downloads) is installed_
* PIO Home > Platforms > Advanced Installation 
* paste https://github.com/Wiz-IO/wizio-pico
* INSTALL

## Uninstall ( fast ) ... Re-Install ( do this and Install again )
* goto C:\Users\USER_NAME\.platformio\ **platforms & packages**
* delete folder **wizio-pico** ( builders )
* delete folder **framework-wizio-pico** ( sources )
* delete folder **tool-wizio-pico** ( tools, picoasm )
* _delete folder toolchain-gccarmnoneeabi (compiler, **may not be deleted** )_

![pico](https://raw.githubusercontent.com/Wiz-IO/LIB/master/pico/pio-pico.jpg)
***

## Baremetal - New Project
PlatformIO -> Home -> New
* Enter Project Name - Board search '**WizIO-PICO**' boards - Select **Baremetal**
* Click BUILD and you will have basic project ( from template )
* For CPP project, **rename** main.c **to** main.cpp ( if you delete main file, builder will create new main.c as template )
* Connect Pico as Mass Storage Device
* Open **platformio.ini** and edit your settings
* BUILD / UPLOAD
* [READ WIKI - BAREMETAL](https://github.com/Wiz-IO/wizio-pico/wiki/BAREMETAL)

## Arduino - New Project
PlatformIO -> Home -> New
* Enter Project Name - Board search '**WizIO-PICO**' boards - Select **Arduino**
* Connect Pico as Mass Storage Device
* Open **platformio.ini** and edit your settings
* BUILD / UPLOAD
* [READ WIKI - ARDUINO](https://github.com/Wiz-IO/wizio-pico/wiki/ARDUINO)

<a href="https://raw.githubusercontent.com/Wiz-IO/LIB/master/pico/pico_pins.svg">
<img src="https://raw.githubusercontent.com/Wiz-IO/LIB/master/pico/pico_pins.svg" alt="Raspberry Pi Pico pin out diagram">
</a>

## Thanks to:
* [Timo Sandmann](https://github.com/tsandmann)
* [Dean Blackketter](https://github.com/blackketter)
* [Ivan Kravets ( PlatformIO )](https://platformio.org/)
* [Comet Electronics](https://www.comet.bg/en/)

***

>If you want to help / support:   
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=ESUP9LCZMZTD6)
