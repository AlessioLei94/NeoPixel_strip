import time, random

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
        return

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

                checkStop()

def smoothRainbow(strip, numpix):
    global __patternStop__
    print("Smooth rainbow starting")

    hue = 0

    while(True):
        color = strip.colorHSV(hue, 255, 150)
        strip.fill(color)
        strip.show()

        hue += 150

        checkStop()

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

            checkStop()

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

        checkStop()

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

        checkStop()

def worm(strip, numpix):
    global __patternStop__
    head = random.randint(0, numpix-1)
    butt = head
    lenght = random.randint(7, 15)
    color1 = (0,0,0)
    color2 = (0,0,0)

    red = (255, 0, 0)
    orange = (255, 50, 0)
    yellow = (255, 100, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    indigo = (100, 0, 90)
    violet = (200, 0, 100)
    colors = [red, orange, yellow, green, blue, indigo, violet]

    #create new worm
    head = 1 #random.randint(0, numpix-1)
    butt = head-lenght

    color1 = colors[random.randint(0, (len(colors)//2-1))]
    color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

    #print first time
    strip[:] = color1
    strip[butt:head] = color2
    strip.show()

    while(True):
        print("bigger")

        for _ in range(10):
            #cover up old worm
            strip[butt:head] = color1

            #move
            head += 1
            butt += 1

            print("s: h b", head, butt)

            #bigger worm
            head = min(numpix-1, head+1)
            print("h: h b", head, butt)

            butt = max(0, butt-1)
            butt = min(numpix-1, butt)

            print("b: h b", head, butt)

            #show new worm
            strip[butt:head] = color2
            strip.show()

            checkStop()
            #check if we got to the end
            if(head == butt):
                #create new worm
                head = random.randint(0, numpix-1)
                butt = head-lenght

                color1 = colors[random.randint(0, (len(colors)//2-1))]
                color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

                #reset strip
                strip[:] = color1

            time.sleep(0.01)

        print("smaller")

        for _ in range(10):
            #cover up old worm
            strip[butt:head] = color1

            #move
            head += 1
            butt += 1

            print("s: h b", head, butt)
            #smaller warm
            head = min(numpix-1, head-1)
            print("h: h b", head, butt)
            butt = min(numpix-1, butt+1)

            print("b: h b", head, butt)

            #show new worm
            strip[butt:head] = color2
            strip.show()


            checkStop()
            #check if we got to the end
            if(head == butt):
                #create new worm
                head = random.randint(0, numpix-1)
                butt = head-lenght

                color1 = colors[random.randint(0, (len(colors)//2-1))]
                color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

                #reset strip
                strip[:] = color1

            time.sleep(0.01)

patternList = [ worm, colorwave, fireflies, rainbow, smoothRainbow, setRange ]
patternCount = len(patternList)
