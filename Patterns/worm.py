import time, random

head = 1
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

def moveFW():
    global head, butt
    head += 1
    butt += 1

def moveBW():
    global head, butt
    head -= 1
    butt -= 1

def bigWorm(numpix):
    global head, butt

    head = min(numpix-1, head+1)

    butt = max(0, butt-1)
    butt = min(numpix-1, butt)

    print("big: h b", head, butt)

def smallWorm(numpix):
    global head, butt

    head = min(numpix-1, head-1)
    butt = min(numpix-1, butt+1)

    print("small: h b", head, butt)

def newWorm():
    global head, butt
    global color1, color2, colors

    head = 1 #random.randint(0, numpix-1)
    butt = head-lenght

    color1 = colors[random.randint(0, (len(colors)//2-1))]
    color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

def showWorm(strip):
    global head, butt
    global color1, color2

    strip[:] = color1
    strip[butt:head] = color2
    strip.show()

def isDead():
    global head, butt

    #check if we got to the end
    if(head == butt):
        return True

    return False

def worm(strip, npx):
    #create new worm
    newWorm()

    #print first time
    showWorm(strip)

    while(True):
        #bigger
        for _ in range(10):
            #move
            moveFW()

            #bigger worm
            bigWorm(npx)

            #show new worm
            showWorm(strip)

            Patterns.checkStop()
            #check if we got to the end
            if isDead():
                newWorm()

            time.sleep(0.01)

        #smaller
        for _ in range(10):
            #move
            moveFW()

            #smaller warm
            smallWorm(npx)

            #show new worm
            showWorm(strip)

            Patterns.checkStop()
            #check if we got to the end
            if isDead():
                newWorm()

            time.sleep(0.01)

#import at the end of the file because
#of cyclic import between worm and patterns
import Patterns.patterns as Patterns
