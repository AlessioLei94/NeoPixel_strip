from Patterns.pattern import Pattern
import Color.color as Color
import time

def colorwaveInit(strip, numpix, colorsList):
    step = round(numpix / len(colors))
    current_pixel = 0

    for color1, color2 in zip(colorsList, colorsList[1:]):
        strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
        current_pixel += step

    strip.set_pixel_line_gradient(current_pixel, numpix - 1, Color.violet.getRGB(), Color.red.getRGB())

    print("Colorwave initialized")


def colorwave(strip, numpix=None, colorsList=None):
    print("Colorwave running")

    strip.rotate_right(1)
    time.sleep(0.042)
    strip.show()

colors = [  Color.red.getRGB(),
            Color.orange.getRGB(),
            Color.yellow.getRGB(),
            Color.green.getRGB(),
            Color.blue.getRGB(),
            Color.indigo.getRGB(),
            Color.violet.getRGB() ]

colorwavePattern = Pattern(colorwaveInit, colorwave, colors)