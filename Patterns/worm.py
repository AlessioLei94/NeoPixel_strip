import time, random

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors = [red, orange, yellow, green, blue, indigo, violet]

def moveFW(head, butt):
    head += 1
    butt += 1

    return head, butt

def moveBW(head, butt):
    head -= 1
    butt -= 1

    return head, butt

def bigWorm(numpix, head, butt):
    head = head+1
    butt = butt-1

    print("big: h:" , head, "b:" ,butt)

    return head, butt

def smallWorm(numpix, head, butt):
    head = head-1
    butt = butt+1

    print("small: h:" , head, "b:" ,butt)

    return head, butt

def newWorm(head, butt, color1, color2, colors):
    lenght = random.randint(15, 50)
    step_len = lenght / 3

    head = 1
    butt = head-lenght

    print("New worm is h:", head, "b:", butt)

    color1 = colors[random.randint(0, (len(colors)//2-1))]
    color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

    return head, butt, color1, color2, lenght, step_len

def showWorm(strip, numpix, head, butt, color1, color2):
    # Don't go out of bounds
    butt = max(butt, 0)
    head = min(head, numpix)

    strip[:] = color1
    strip[butt:head] = color2
    strip.show()

def isDead(head, butt, numpix):
    #check if we got to the end
    if(butt >= numpix):
        return True

    return False

def worm(strip, npx):
    global colors
    lenght = random.randint(15, 50)
    head = 1
    butt = head - lenght
    step_len = int(lenght / 3)
    sleepTime = 0.2 #sec
    color1 = (0,0,0)
    color2 = (0,0,0)

    print("Worm starting")

    #create new worm
    head, butt, color1, color2, lenght, step_len = newWorm(head, butt, color1, color2, colors)

    #print first time
    showWorm(strip, npx, head, butt, color1, color2)

    while(True):
        #bigger
        for _ in range(step_len):
            #move
            head, butt = moveFW(head, butt)

            #bigger worm
            head, butt = bigWorm(npx, head, butt)

            #show new worm
            showWorm(strip, npx, head, butt, color1, color2)

            if(Patterns.checkStop()):
                return

            #check if we got to the end
            if isDead(head, butt, npx):
                head, butt, color1, color2, lenght, step_len = newWorm(head, butt, color1, color2, colors)

            time.sleep(sleepTime)

        #smaller
        for _ in range(step_len):
            #move
            head, butt = moveFW(head, butt)

            #smaller warm
            head, butt = smallWorm(npx, head, butt)

            #show new worm
            showWorm(strip, npx, head, butt, color1, color2)

            Patterns.checkStop()
            #check if we got to the end
            if isDead(head, butt, npx):
                head, butt, color1, color2, lenght, step_len = newWorm(head, butt, color1, color2, colors)

            time.sleep(sleepTime)

#import at the end of the file because
#of cyclic import between worm and patterns
import Patterns.patterns as Patterns
