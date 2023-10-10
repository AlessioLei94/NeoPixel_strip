from Patterns.pattern import Pattern
import Settings.settings as Settings
from Color import color as Colors
import time, random

colors = [  Colors.red.getRGB(),
            Colors.orange.getRGB(),
            Colors.yellow.getRGB(),
            Colors.green.getRGB(),
            Colors.blue.getRGB(),
            Colors.indigo.getRGB(),
            Colors.violet.getRGB(),
            Colors.lightBlue.getRGB(),
            Colors.lightGreen.getRGB(),
            Colors.waterGreen.getRGB(),
            Colors.acidGreen.getRGB(),
            Colors.darkOrange.getRGB() ]

__color = 0

def loadIndex():
    index = Settings.readSetting(1)
    index = (index + 1) % len(colors)

    Settings.writeSetting(index, 1)

    return index

def simpleColorInit(strip, numpix, colorsList):
    global __color

    __color = colorsList[loadIndex()]

    print("Simple color initialized with R:", __color[0], " G:", __color[1], " B:", __color[2])

def simpleColor(strip, numpix, colorsList):
    print("Simple color running")

    strip.fill(__color)
    strip.show()

    time.sleep(0.01)

simpleColorPattern = Pattern(simpleColorInit, simpleColor, colors)