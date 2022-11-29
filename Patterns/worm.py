import time, random

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors = [red, orange, yellow, green, blue, indigo, violet]

def moveFW(nWorms, head, butt):
    for i in range(nWorms):
        head[i] += 1
        butt[i] += 1

def moveBW(nWorms, head, butt):
    for i in range(nWorms):
        head[i] -= 1
        butt[i] -= 1

def bigWorm(numpix, nWorms, head, butt):
    for i in range(nWorms):
        head[i] = min(numpix-1, head[i]+1)

        butt[i] = max(0, butt[i]-1)
        butt[i] = min(numpix-1, butt[i])

        #print("big: h b", head[i], butt[i])

def smallWorm(numpix, nWorms, head, butt):
    for i in range(nWorms):
        head[i] = min(numpix-1, head[i]-1)
        butt[i] = min(numpix-1, butt[i]+1)

        #print("small: h b", head[i], butt[i])

def newWorm(head, butt, color1, color2, colors, lenght):
    head = 1
    butt = head-lenght

    color1 = colors[random.randint(0, (len(colors)//2-1))]
    color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

def newRandWorm(numpix, head, butt, color1, color2, colors, lenght):
    head = random.randint(0, numpix-1)
    butt = head-lenght

    color1 = colors[random.randint(0, (len(colors)//2-1))]
    color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

def showWorms(strip, nWorms, head, butt, color1, color2):
    for i in range(nWorms):
        strip[:] = color1[i]
        strip[butt:head] = color2[i]

    strip.show()

def isDead(head, butt):

    #check if we got to the end
    if(head == butt):
        return True

    return False

def multiWorm(strip, npx):
    global colors
    nWorms = 20
    head = [0] * nWorms
    butt = head[:]
    lenght = [0] * nWorms
    random.randint(7, 15)
    color1 = [0,0,0] * nWorms
    color2 = color1[:]

    #create new worms
    for idx in range(nWorms):
        newRandWorm(npx, head[i], butt[i], color1[i], color2[i], colors[i], lenght[i])
    
    showWorms(strip, nWorms, head, butt, color1, color2)

    while(True):
        #bigger
        for _ in range(10):
            #move
            moveFW(nWorms ,head, butt)

            #bigger worm
            bigWorm(npx, nWorms, head, butt)

            #show new worm
            showWorms(strip, nWorms, head, butt, color1, color2)

            Patterns.checkStop()
            #check if we got to the end
            for i in range(nWorms):
                if isDead(head[i], butt[i]):
                    newRandWorm(npx, head, butt, color1, color2, colors, lenght)

            time.sleep(0.01)

        #smaller
        for _ in range(10):
            #move
            moveFW(nWorms, head, butt)

            #smaller warm
            smallWorm(npx, nWorms, head, butt)

            #show new worm
            showWorms(strip, head, nWorms, butt, color1, color2)

            Patterns.checkStop()
            #check if we got to the end
            for i in range(nWorms):
                if isDead(head[i], butt[i]):
                    newRandWorm(npx, head, butt, color1, color2, colors, lenght)

            time.sleep(0.01)

#import at the end of the file because
#of cyclic import between worm and patterns
import Patterns.patterns as Patterns
