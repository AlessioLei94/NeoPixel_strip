import Buttons.buttons as Buttons
import Patterns.patterns as Patterns

# FSM states
FSM_INIT = 0
FSM_RUN = 1
FSM_STOP = 2

__fsmState__ = FSM_INIT
__patternIdx__ = 0
__strip__ = 0
__numpix__ = 0

def setState(state):
    global __fsmState__

    __fsmState__ = state

def getState(state):
    global __fsmState__

    return __fsmState__

def patternFW():
    global __patternIdx__

    if(__patternIdx__ == Patterns.patternCount - 1):
        __patternIdx__ = 0
    else:
        __patternIdx__ += 1

    print("Pattern is now ", __patternIdx__)

    Patterns.stopCurrentPattern()

def patternBW():
    global __patternIdx__

    if(__patternIdx__ == 0):
        __patternIdx__ = Patterns.patternCount - 1
    else:
        __patternIdx__ -= 1

    print("Pattern is now ", __patternIdx__)

    Patterns.stopCurrentPattern()

def brightUp():
    Patterns.__brightness__ += Patterns.__brightStep__

    if(Patterns.__brightness__ > 255):
        Patterns.__brightness__ = 255

    print("Brightness is now ", Patterns.__brightness__)

    __strip__.brightness(Patterns.__brightness__)

def brightDw():
    Patterns.__brightness__ -= Patterns.__brightStep__

    if(Patterns.__brightness__ < 0):
        Patterns.__brightness__ = 0

    print("Brightness is now ", Patterns.__brightness__)

    __strip__.brightness(Patterns.__brightness__)

def run(party):
    global FSM_INIT, FSM_RUN, FSM_STOP
    global __patternIdx__
    global __fsmState__
    global __strip__, __numpix__

    if(__fsmState__ == FSM_INIT):
        Buttons.Init()
        Patterns.setList(party)
        __fsmState__ = FSM_RUN

    elif(__fsmState__ == FSM_RUN):
        Patterns.patternList[__patternIdx__](__strip__, __numpix__)

def init(strip, numpix):
    global __strip__, __numpix__

    __strip__ = strip
    __numpix__ = numpix
