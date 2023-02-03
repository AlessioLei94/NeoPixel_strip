import time, random
from Patterns.worm import worm

__patternStop__ = False
__brightness__ = 100 #Default
__brightStep__ = 25

def stopCurrentPattern():
    global __patternStop__
    __patternStop__ = True

def checkStop():
    global __patternStop__
    if(__patternStop__ == True):
        __patternStop__ = False
        return True

def simpleColor(strip, numpix):
    global __patternStop__
    print("Simple color starting")

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

    color = colors[random.randint(0, len(colors)-1)]
    #print(color[0], color[1], color[2])

    while True:
        # Check if we need to stop
        if(checkStop()):
            return
        
        strip.fill(color)
        strip.show()

        time.sleep(0.01)

def rainbow(strip, numpix):
    global __patternStop__
    print("Rainbow starting")

    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 150, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    indigo = (75, 0, 130)
    violet = (138, 43, 226)
    colors = (red, orange, yellow, green, blue, indigo, violet)

    while True:
        for color in colors:
            for i in range(numpix):
                strip.set_pixel(i, color)
                time.sleep(0.01)
                strip.show()

                # Check if we need to stop
                if(checkStop()):
                    return

def smoothRainbow(strip, numpix):
    global __patternStop__
    print("Smooth rainbow starting")

    hue = 0

    while(True):
        color = strip.colorHSV(hue, 255, 150)
        strip.fill(color)
        strip.show()

        hue += 150

        # Check if we need to stop
        if(checkStop()):
            return

def fireflies(strip, numpix):
    global __patternStop__
    print("Fireflies starting")

    colors = [
    (232, 100, 255),  # Purple
    (200, 200, 20),  # Yellow
    (30, 200, 200),  # Blue
    (150,50,10),
    (50,200,10), ]

    max_len=20
    min_len = 5
    #pixelnum, posn in flash, flash_len, direction
    flashing = []

    num_flashes = 10

    for i in range(num_flashes):
        pix = random.randint(0, numpix - 1)
        col = random.randint(1, len(colors) - 1)
        flash_len = random.randint(min_len, max_len)
        flashing.append([pix, colors[col], flash_len, 0, 1])

    strip.fill((0,0,0))

    while True:
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

            # Check if we need to stop
            if(checkStop()):
                return

def colorwave(strip, numpix):
    global __patternStop__
    print("Colorwave starting")

    red = (255, 0, 0)
    orange = (255, 50, 0)
    yellow = (255, 100, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    indigo = (100, 0, 90)
    violet = (200, 0, 100)
    colors = [red, orange, yellow, green, blue, indigo, violet]

    step = round(numpix / len(colors))
    current_pixel = 0

    for color1, color2 in zip(colors, colors[1:]):
        strip.set_pixel_line_gradient(current_pixel, current_pixel + step, color1, color2)
        current_pixel += step

    strip.set_pixel_line_gradient(current_pixel, numpix - 1, violet, red)

    while True:
        strip.rotate_right(1)
        time.sleep(0.042)
        strip.show()

        # Check if we need to stop
        if(checkStop()):
            return

def setRange(strip, numpix):
    global __patternStop__
    print("setRange starting")

    K = 3

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    # set the first K to red, next K to green, next K to blue;
    # and the rest to R,G,B,R,B  ... and then spin it.

    # reduce K, if numpix is < K*3+1
    K = min(K,(numpix-1)//3)

    strip[:] = blue   # all to blue first...
    # now fill in the red & green...
    strip[:K] = red
    strip[K:2*K] = green
    strip[3*K::3] = red
    strip[3*K+1::3] = green

    strip.show()

    # show it for 5 seconds...
    time.sleep(5.0)

    # spin it...
    sleepTime = 0.1
    spinTime = 0.5
    idx = 0

    while(True):
        if(idx * sleepTime >= sleepTime):
            strip.rotate_right()
            strip.show()
            idx = 0

        time.sleep(sleepTime)

        idx = idx + 1

        # Check if we need to stop
        if(checkStop()):
            return

#patternList = [ worm, colorwave, fireflies, rainbow, smoothRainbow, setRange ]
patternList = [ simpleColor ]
patternCount = len(patternList)
