import Buttons.buttons as Buttons
import Patterns.patterns as Patterns

# FSM states
FSM_INIT = 0
FSM_RUN = 1
FSM_STOP = 2

__fsmState__ = FSM_INIT
__patternIdx__ = 0

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
        __patternIdx__ = __patternIdx__ + 1

    Patterns.stopCurrentPattern()

def patternBW():
    global __patternIdx__

    if(__patternIdx__ == 0):
        __patternIdx__ = Patterns.patternCount - 1
    else:
        __patternIdx__ = __patternIdx__ - 1

    Patterns.stopCurrentPattern()

def run(strip, numpix):
    global FSM_INIT, FSM_RUN, FSM_STOP
    global __patternIdx__
    global __fsmState__

    if(__fsmState__ == FSM_INIT):
        Buttons.Init()
        __fsmState__ = FSM_RUN

    elif(__fsmState__ == FSM_RUN):
        Patterns.patternList[__patternIdx__](strip, numpix)
