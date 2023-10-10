from Patterns.pattern import Pattern
from Color import color as Colors
import time, random

max_len=20
min_len = 5
#pixelnum, posn in flash, flash_len, direction
flashing = []
num_flashes = 10

def firefliesInit(strip, numpix, colorsList):
    global max_len, min_len, flashing, num_flashes

    for i in range(num_flashes):
        pix = random.randint(0, numpix - 1)
        col = random.randint(1, len(colorsList) - 1)
        flash_len = random.randint(min_len, max_len)
        flashing.append([pix, colorsList[col], flash_len, 0, 1])

    strip.fill((0,0,0))

    print("Fireflies initialized")

def fireflies(strip, numpix, colorsList):
    global max_len, min_len, flashing, num_flashes
    # print("Fireflies running")

    strip.show()
    for i in range(num_flashes):

        pix = flashing[i][0]
        brightness = (flashing[i][3]/flashing[i][2])
        color = (int(flashing[i][1][0]*brightness),
                int(flashing[i][1][1]*brightness),
                int(flashing[i][1][2]*brightness))
        strip.set_pixel(pix, color)

        if flashing[i][2] == flashing[i][3]:
            flashing[i][4] = -1
        if flashing[i][3] == 0 and flashing[i][4] == -1:
            pix = random.randint(0, numpix - 1)
            col = random.randint(0, len(colors) - 1)
            flash_len = random.randint(min_len, max_len)
            flashing[i] = [pix, colors[col], flash_len, 0, 1]
        flashing[i][3] = flashing[i][3] + flashing[i][4]
        time.sleep(0.005)

colors = [  Colors.purple.getRGB(),
            Colors.yellow.getRGB(),
            Colors.blue.getRGB(),
            Colors.darkOrange.getRGB(),
            Colors.acidGreen.getRGB() ]

firefliesPattern = Pattern(firefliesInit, fireflies, colors)