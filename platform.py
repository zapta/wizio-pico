# WizIO 2021 Georgi Angelov
#   http://www.wizio.eu/
#   https://github.com/Wiz-IO/wizio-pico

from platformio.managers.platform import PlatformBase

class WiziopicoPlatform(PlatformBase):
    def is_embedded(self):
        return True
    
