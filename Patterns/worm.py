from Patterns.pattern import Pattern
from Color import color as Colors
import time, random

class Worm:
    def __init__(self, colorsList, maxLen):
        self.lenght = random.randint(15, 50)
        self.head = 1
        self.butt = self.head - self.lenght
        self.step_len = self.lenght // 3
        self.sleepTime = 0.2 #seconds
        if (len(colorsList) > 1):
            self.color1 = colorsList[random.randint(0, (len(colorsList)//2-1))]
            self.color2 = colorsList[random.randint(len(colorsList)//2, len(colorsList)-1)]
        self.maxLen = maxLen

    def fixBounds(self):
        self.butt = max(self.butt, 0)
        self.head = min(self.head, self.maxLen)

    def newWorm(self, colorsList, maxLen):
        self.__init__(colorsList, maxLen)

    def moveFW(self):
        # Increment Head and Butt
        self.head += 1
        self.butt += 1

    def moveBW(self):
        # Decrement Head and Butt
        self.head -= 1
        self.butt -= 1

    def bigWorm(self):
        # Increment Head
        self.head += 1
        # Decrement Butt
        self.butt -= 1

        print("big: h:" , self.head, "b:" , self.butt)

    def smallWorm(self):
        # Decrement Head
        self.head -= 1
        # Increment Butt
        self.butt += 1

        print("small: h:" , self.head, "b:" , self.butt)

    def isDead(self):
        # Check if we got to the end
        if(self.butt >= self.maxLen):
            return True

        return False

wormObj = Worm([0], 0)

def showWorm(strip, wormObj):
    # Don't go out of bounds
    wormObj.fixBounds()

    strip[:] = wormObj.color1
    strip[wormObj.butt:wormObj.head] = wormObj.color2
    strip.show()

def wormInit(strip, numpix, colorsList):
    global wormObj

    #create new worm
    wormObj = Worm(colorsList, numpix)

    #print first time
    showWorm(strip, wormObj)

    print("Worm initialized")

def worm(strip, numpix, colorsList):
    global wormObj
    # print("Worm running")

    #bigger
    for _ in range(wormObj.step_len):
        #move
        wormObj.moveFW()

        #bigger worm
        wormObj.bigWorm()

        #show new worm
        showWorm(strip, wormObj)

        #check if we got to the end
        if wormObj.isDead():
            wormObj.newWorm(colorsList, numpix)

        time.sleep(wormObj.sleepTime)

    #smaller
    for _ in range(wormObj.step_len):
        #move
        wormObj.moveFW()

        #smaller warm
        wormObj.smallWorm()

        #show new worm
        showWorm(strip, wormObj)

        #check if we got to the end
        if wormObj.isDead():
            wormObj.newWorm(colorsList, numpix)

        time.sleep(wormObj.sleepTime)

colors = [  Colors.red.getRGB(),
            Colors.orange.getRGB(),
            Colors.yellow.getRGB(),
            Colors.green.getRGB(),
            Colors.blue.getRGB(),
            Colors.indigo.getRGB(),
            Colors.violet.getRGB() ]

wormPattern = Pattern(wormInit, worm, colors)