from Patterns.pattern import Pattern
from Color import color as Colors
from Mic_lib.mic_lib import Mic
import time, random

__pwrPin = 4
__adcPin = 26
__maxMicOut = 65535
__baseMicOut = 30500

mic = Mic(__pwrPin, __adcPin, __maxMicOut, __baseMicOut)

def micTestInit(strip, numpix, colorsList):
    global mic

    # Power ON mic board
    mic.setPwr(True)

def micTest(strip, numpix, colorsList):
    global mic

    print((mic.read(), 0))

    time.sleep(0.05)

# Colors list
colors = [  Colors.red.getRGB() ]

micTestPattern = Pattern(micTestInit, micTest, colors)