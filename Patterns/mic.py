from Patterns.pattern import Pattern
from Color import color as Colors
from Mic_lib.mic_lib import Mic
import time, random

class Wave:
    def __init__(self, numpix, colorsList, maxMicOut, basemMicOut):
        # Reference points used in calculations
        self.maxLen = numpix
        self.center = int(self.maxLen / 2)
        self.baseLen = 30
        self.expRoom = self.maxLen - self.baseLen
        self.micDiff = maxMicOut - basemMicOut

        # Pick two colors
        self.baseColor = colorsList[random.randint(0, len(colorsList)-1)]
        self.color = colorsList[random.randint(0, len(colorsList)-1)]
        # Make sure it's two different colors
        if (len(colorsList) > 1):
            while self.baseColor == self.color:
                self.color = colorsList[random.randint(0, len(colorsList)-1)]

        print("baseColor", self.baseColor, "color", self.color)

        self.lowEnd = self.center-int(self.baseLen/2)
        self.highEnd = self.center+int(self.baseLen/2)
        self.oldExp = 0

    def big(self):
        # Decrese low end, now smaller than zero
        self.lowEnd = max((self.lowEnd - 1), 0)
        # Increase highEnd, not bigger than maxLen
        self.highEnd = min((self.highEnd + 1), self.maxLen)

    def small(self):
        # Increase lowEnd, not bigger than lowEnd base
        self.lowEnd = min((self.lowEnd + 1), self.center - int(self.baseLen/2))
        # Decrese highEnd, not smaller than highEnd base
        self.highEnd = max((self.highEnd - 1), self.center + int(self.baseLen/2))

__pwrPin = 4
__adcPin = 26
__maxMicOut = 65535
__baseMicOut = 30500

mic = Mic(__pwrPin, __adcPin, __maxMicOut, __baseMicOut)
wave = Wave(0, [0], 0, 0)

def soundWaveInit(strip, numpix, colorsList):
    global wave, mic

    wave = Wave(numpix, colorsList, mic.getMaxOut(), mic.getBaseOut())

    # Power ON mic board
    mic.setPwr(True)

    # Fill strip buffer for the first time
    strip.fill(wave.baseColor)
    strip[wave.lowEnd:wave.highEnd] = wave.color
    # Show base wave
    strip.show()

    print("Mic pattern initialized")

def soundWave(strip, numpix, colorsList):
    global mic, wave

    print("Mic pattern running")

    # Read mic input
    noise = mic.read()
    # Calculate difference in input from 0dB input voltage
    diff = -1*(noise - mic.getBaseOut())

    # print("Input diff:", diff)

    # calulcate wave expansion based on mic input
    waveExp = ((wave.expRoom * diff) / wave.micDiff) * mic.amplify

    # print("Wave expansion:", waveExp)

    if (waveExp > wave.oldExp):
        #Calculate how much to extend
        diff = (waveExp - wave.oldExp) / 2
        # Bigger wave
        for _ in range(1, diff):
            wave.big()
            # Print wave to strip buffer
            strip.fill(wave.baseColor)
            strip[wave.lowEnd:wave.highEnd] = wave.color
            # Show wave
            strip.show()

            # print("B -> lowEnd:", lowEnd, "highEnd:", highEnd)
    elif (waveExp < wave.oldExp):
        #Calculate how much to shrink
        diff = (wave.oldExp - waveExp) / 2
        # Smaller wave
        for _ in range(1, diff):
            wave.small()
            # Print wave to strip buffer
            strip.fill(wave.baseColor)
            strip[wave.lowEnd:wave.highEnd] = wave.color
            # Show wave
            strip.show()

            # print("S -> lowEnd:", lowEnd, "highEnd:", highEnd)

    wave.oldExp = waveExp

    time.sleep_ms(5)

# Colors list
colors = [  Colors.red.getRGB(),
            Colors.orange.getRGB(),
            Colors.yellow.getRGB(),
            Colors.green.getRGB(),
            Colors.blue.getRGB(),
            Colors.indigo.getRGB(),
            Colors.violet.getRGB(),
            Colors.lightBlue.getRGB(),
            Colors.lightGreen.getRGB(),
            Colors.waterGreen.getRGB() ]

soundwavePattern = Pattern(soundWaveInit, soundWave, colors)