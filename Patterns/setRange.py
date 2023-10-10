from Patterns.pattern import Pattern
from Color import color as Colors
import time, random

sleepTime = 0.0
spinTime = 0.0
idx = 0

def setRangeInit(strip, numpix, colorsList):
    global sleepTime, spinTime, idx

    K = 3

    # set the first K to red, next K to green, next K to blue;
    # and the rest to R,G,B,R,B  ... and then spin it.

    # reduce K, if numpix is < K*3+1
    K = min(K,(numpix-1)//3)

    strip[:] = colorsList[2]   # all to blue first...
    # now fill in the red & green...
    strip[:K] = colorsList[0]
    strip[K:2*K] = colorsList[1]
    strip[3*K::3] = colorsList[0]
    strip[3*K+1::3] = colorsList[1]

    strip.show()

    # show it for 5 seconds...
    time.sleep(5.0)

    # spin it...
    sleepTime = 0.1
    spinTime = 0.5
    idx = 0

    print("setRange initialized")

def setRange(strip, numpix, colorsList):
    global sleepTime, spinTime, idx

    # print("setRange running")

    if(idx * sleepTime >= sleepTime):
        strip.rotate_right()
        strip.show()
        idx = 0

    time.sleep(sleepTime)

    idx = idx + 1

colors = [  Colors.red.getRGB(),
            Colors.green.getRGB(),
            Colors.blue.getRGB() ]

setRangePattern = Pattern(setRangeInit, setRange, colors)