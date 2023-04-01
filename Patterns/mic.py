import Mic_lib.mic_lib as Mic
import time, random, math
from Patterns import patterns

__maxMicOut = 65535
__baseMicOut = 30500

def soundWave(strip, npx):
    global __maxMicOut, __baseMicOut

    print("Mic pattern starting")

    # Multiplying factor used to adjust mic sensitivity
    micAmplfy = 3
    # Power ON mic board
    Mic.setPwr(True)
    
    # Colors list
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

    # Reference points used in calculations
    stripCenter = int(npx / 2)
    waveBaseLen = 30
    waveExpRoom = npx - waveBaseLen
    micDiff = __maxMicOut - __baseMicOut

    # Pick two colors
    mainColor = colors[random.randint(0, len(colors)-1)]
    waveColor = colors[random.randint(0, len(colors)-1)]
    # Make sure it's two different colors
    while mainColor == waveColor:
        waveColor = colors[random.randint(0, len(colors)-1)]
    
    print("mainColor", mainColor, "waveColor", waveColor)

    lowEnd = stripCenter-int(waveBaseLen/2)
    highEnd = stripCenter+int(waveBaseLen/2)
    oldExp = 0

    # Fill strip buffer for the first time
    strip.fill(mainColor)
    strip[lowEnd:highEnd] = waveColor
    # Show base wave
    strip.show()

    while True:
        # Read mic input
        noise = Mic.readMic()
        # Calculate difference in input from 0dB input voltage
        diff = abs(noise - __baseMicOut)

        # print("Input diff:", diff)

        # calulcate wave expansion based on mic input
        waveExp = ((waveExpRoom * diff) / micDiff) * micAmplfy

        # print("Wave expansion:", waveExp)

        if (waveExp > oldExp):
            #Calculate how much to extend
            diff = (waveExp - oldExp) / 2
            # Bigger wave
            for _ in range(1, diff):
                # Decrese low end, now smaller than zero
                lowEnd = max((lowEnd - 1), 0)
                # Increase highEnd, not bigger than npx
                highEnd = min((highEnd + 1), npx)
                # Print wave to strip buffer
                strip.fill(mainColor)
                strip[lowEnd:highEnd] = waveColor
                # Show wave
                strip.show()

                # print("B -> lowEnd:", lowEnd, "highEnd:", highEnd)
        elif (waveExp < oldExp):
            #Calculate how much to shrink
            diff = (oldExp - waveExp) / 2
            # Smaller wave
            for _ in range(1, diff):
                # Increase lowEnd, not bigger than lowEnd base
                lowEnd = min((lowEnd + 1), stripCenter - int(waveBaseLen/2))
                # Decrese highEnd, not smaller than highEnd base
                highEnd = max((highEnd - 1), stripCenter + int(waveBaseLen/2))
                # Print wave to strip buffer
                strip.fill(mainColor)
                strip[lowEnd:highEnd] = waveColor
                # Show wave
                strip.show()

                # print("S -> lowEnd:", lowEnd, "highEnd:", highEnd)

        oldExp = waveExp

        time.sleep_ms(1)

        if patterns.checkStop():
            break
