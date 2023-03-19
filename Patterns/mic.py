import Mic_lib.mic_lib as Mic
import time, random
from Patterns import patterns

__maxMicOut = 65535
__baseMicOut = 30500

def soundWave(strip, npx):
    global __maxMicOut, __baseMicOut

    print("Mic pattern starting")

    # Power ON mic board
    Mic.setPwr(True)

    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 150, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    indigo = (75, 0, 130)
    violet = (138, 43, 226)
    lightBlue = (18, 204, 198)
    lightGreen = (37, 184, 20)
    waterGreen = (35, 207, 115)
    colors = (red, orange, yellow, green, blue, indigo, violet, lightBlue, lightGreen, waterGreen)

    stripCenter = int(npx / 2)
    waveBaseLen = 30
    waveExpRoom = npx - waveBaseLen
    micDiff = __maxMicOut - __baseMicOut

    mainColor = colors[random.randint(0, len(colors)-1)]
    waveColor = colors[random.randint(0, len(colors)-1)]
    # Make sure it's two different colors
    while mainColor == waveColor:
        waveColor = colors[random.randint(0, len(colors)-1)]
    
    print("mainColor", mainColor, "waveColor", waveColor)

    lowEnd = stripCenter-int(waveBaseLen/2)
    highEnd = stripCenter+int(waveBaseLen/2)

    strip.fill(mainColor)
    strip[lowEnd:highEnd] = waveColor
    strip.show()

    while True:
        noise = Mic.readMic()
        diff = noise - __baseMicOut

        print("Input diff:", diff)

        waveExp = ((waveExpRoom * diff) / micDiff) * 2

        print("Wave expansion:", waveExp)

        newLow = max((lowEnd - int(waveExp/2)), 0)
        newHigh = min((highEnd + int(waveExp/2)), npx)

        print("lowEnd", newLow, "highEnd", newHigh)

        strip.fill(mainColor)
        strip[newLow:newHigh] = waveColor
        strip.show()

        time.sleep_ms(100)

        if patterns.checkStop():
            break
