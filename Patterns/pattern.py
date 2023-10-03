class Pattern:
    def __init__(self, patternInit, patternRun, colorsList):
        self.patternInit = patternInit
        self.patternRun = patternRun
        self.patternStop = False
        self.colorsList = colorsList

    def __checkStop(self):
        if (self.patternStop == True):
            self.patternStop = False
            return True

    def run(self, strip, numpix):
        self.patternInit(strip, numpix, self.colorsList)

        while (True):
            # Execute pattern function that shouldn't contain any loop
            self.patternRun(strip, numpix, self.colorsList)
            # Check if we need to stop executing pattern
            if (self.__checkStop()):
                print("Exiting pattern")
                return

    def stop(self):
        self.patternStop = True