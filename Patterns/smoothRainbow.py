from Patterns.pattern import Pattern

hue = 0

def smoothRainbowInit(strip, numpix, colorsList):
    # Nothing to do here
    return

def smoothRainbow(strip, numpix, colorsList):
    global hue
    print("Smooth rainbow running")

    color = strip.colorHSV(hue, 255, 150)
    strip.fill(color)
    strip.show()

    hue += 150

smoothRainbowPattern = Pattern(smoothRainbowInit, smoothRainbow, None)