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
    head = min(numpix-1, head+1)

    butt = max(0, butt-1)
    butt = min(numpix-1, butt)

    #print("big: h b", head, butt)

    return head, butt

def smallWorm(numpix, head, butt):
    head = min(numpix-1, head-1)
    butt = min(numpix-1, butt+1)

    #print("small: h b", head, butt)

    return head, butt

def newWorm(head, butt, color1, color2, colors, lenght):

    head = 1 #random.randint(0, numpix-1)
    butt = head-lenght

    color1 = colors[random.randint(0, (len(colors)//2-1))]
    color2 = colors[random.randint(len(colors)//2, len(colors)-1)]

    return head, butt, color1, color2

def showWorm(strip, head, butt, color1, color2):

    strip[:] = color1
    strip[butt:head] = color2
    strip.show()

def isDead(head, butt):

    #check if we got to the end
    if(head == butt):
        return True

    return False

def worm(strip, npx):
    global colors
    head = 1
    butt = head
    lenght = random.randint(7, 15)
    color1 = (0,0,0)
    color2 = (0,0,0)

    #create new worm
    head, butt, color1, color2 = newWorm(head, butt, color1, color2, colors, lenght)

    #print first time
    showWorm(strip, head, butt, color1, color2)

    while(True):
        #bigger
        for _ in range(10):
            #move
            head, butt = moveFW(head, butt)

            #bigger worm
            head, butt = bigWorm(npx, head, butt)

            #show new worm
            showWorm(strip, head, butt, color1, color2)

            Patterns.checkStop()
            #check if we got to the end
            if isDead(head, butt):
                head, butt, color1, color2 = newWorm(head, butt, color1, color2, colors, lenght)

            time.sleep(0.01)

        #smaller
        for _ in range(10):
            #move
            head, butt = moveFW(head, butt)

            #smaller warm
            head, butt = smallWorm(npx, head, butt)

            #show new worm
            showWorm(strip, head, butt, color1, color2)

            Patterns.checkStop()
            #check if we got to the end
            if isDead(head, butt):
                head, butt, color1, color2 = newWorm(head, butt, color1, color2, colors, lenght)

            time.sleep(0.01)

#import at the end of the file because
#of cyclic import between worm and patterns
import Patterns.patterns as Patterns
