from Neopixel_lib import neopixel
import Buttons.button as Button
import Settings.settings as Settings
from Patterns.colorwave import colorwavePattern
from Patterns.fireflies import firefliesPattern
from Patterns.mic import soundwavePattern
from Patterns.rainbow import rainbowPattern
from Patterns.setRange import setRangePattern
from Patterns.simpleColor import simpleColorPattern
from Patterns.smoothRainbow import smoothRainbowPattern
from Patterns.worm import wormPattern
import time

__brightness = 100 #Default
__brightStep = 25

class LedController:
    def __init__(self, numLeds, btnFW, btnBW, btnBrightUp, btnBrightDown):
        global __brightness

        self.strip = neopixel.Neopixel(numLeds, 1, 15)
        self.numpix = numLeds
        self.btnFW = Button.Button(btnFW, self.__patternFW)
        self.btnBW = Button.Button(btnBW, self.__patternBW)
        self.btnBrightUp = Button.Button(btnBrightUp, self.__brightUp) # Party mode
        self.btnBrightDown = Button.Button(btnBrightDown, self.__brightDown) # Mic mode
        self.patternsList = []
        self.patternIdx = 0

        # Load and set brightness
        __brightness = Settings.readSetting(0)
        self.strip.brightness(__brightness)

    def __patternFW(self):
        # Stop current pattern
        self.patternsList[self.patternIdx].stop()
        # Increase pattern index
        self.patternIdx = (self.patternIdx + 1) % len(self.patternsList)

    def __patternBW(self):
        # Stop current pattern
        self.patternsList[self.patternIdx].stop()
        # Decrease pattern index
        self.patternIdx = (self.patternIdx - 1) % len(self.patternsList)

    def __brightUp(self):
        global __brightness, __brightStep
        if(__brightness < 255):
            __brightness += __brightStep
            __brightness = min(__brightness, 255)
            # If changed, write setting to file
            Settings.writeSetting(__brightness)

        print("Brightness is now ", __brightness)

        self.strip.brightness(__brightness)

    def __brightDown(self):
        global __brightness, __brightStep
        if(__brightness > 0):
            __brightness -= __brightStep
            __brightness = max(__brightness, 0)
            # If changed, write setting to file
            Settings.writeSetting(__brightness)

        print("Brightness is now ", __brightness)

        self.strip.brightness(__brightness)

    def __checkPartyBtnState(self):
        if self.btnBrightUp.getState() == 1:
            return True

    def __checkMicBtnState(self):
        if self.btnBrightDown.getState() == 1:
            return True

    def __checkMode(self):
        if self.__checkPartyBtnState():
            return 0
        elif self.__checkMicBtnState():
            return 2
        else:
            return 1

    def __selectPatternList(self):
        mode = self.__checkMode()

        if (mode == 0):
            print("Party mode")
            self.patternsList = [ wormPattern, colorwavePattern, firefliesPattern, rainbowPattern,
                            smoothRainbowPattern, setRangePattern ]
        elif (mode == 1):
            print("Chill mode")
            self.patternsList = [ simpleColorPattern ]
        elif (mode == 2):
            print("Mic mode")
            self.patternsList = [ soundwavePattern ]

    def init(self):
        self.__selectPatternList()

    def run(self):
        self.patternsList[self.patternIdx].run(self.strip, self.numpix)

        time.sleep(0.01)