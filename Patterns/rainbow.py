from Patterns.pattern import Pattern
from Color import color as Color
import time

def rainbowInit(strip, numpix, colorsList):
    # Nothing to do here
    return

def rainbow(strip, numpix, colorsList):
    print("Rainbow running")

    for color in colorsList:
        for i in range(numpix):
            strip.set_pixel(i, color)
            time.sleep(0.01)
            strip.show()

colors = [  Color.red.getRGB(),
            Color.orange.getRGB(),
            Color.yellow.getRGB(),
            Color.green.getRGB(),
            Color.blue.getRGB(),
            Color.indigo.getRGB(),
            Color.violet.getRGB() ]

rainbowPattern = Pattern(rainbowInit, rainbow, colors)