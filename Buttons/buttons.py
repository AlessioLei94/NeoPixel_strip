from machine import Pin
import Fsm.fsm as Fsm
import time

btn1Pin = Pin(20, Pin.IN, Pin.PULL_DOWN) # Pattern FW
btn2Pin = Pin(18, Pin.IN, Pin.PULL_DOWN) # Pattern BW
btn3Pin = Pin(21, Pin.IN, Pin.PULL_DOWN) # Brightness UP
btn4Pin = Pin(19, Pin.IN, Pin.PULL_DOWN) # Brightness DOWN

btn1T = 0
btn2T = 0
btn3T = 0
btn4T = 0

__debounceT_ = 500

def checkPartyBtnState():
    global btn3Pin
    if btn3Pin.value() == 1:
        return True

def btn1Cb(pin):
    global btn1T, __debounceT_
    if((time.ticks_ms() - btn1T) > __debounceT_ or (btn1T == 0)):
        btn1T = time.ticks_ms()
        Fsm.patternFW()

def btn2Cb(pin):
    global btn2T, __debounceT_

    if((time.ticks_ms() - btn2T) > __debounceT_ or (btn2T == 0)):
        btn2T = time.ticks_ms()
        Fsm.patternBW()

def btn3Cb(pin):
    global btn3T, __debounceT_

    if((time.ticks_ms() - btn3T) > __debounceT_ or (btn3T == 0)):
        btn3T = time.ticks_ms()
        Fsm.brightUp()

def btn4Cb(pin):
    global btn4T, __debounceT_

    if((time.ticks_ms() - btn4T) > __debounceT_ or (btn4T == 0)):
        btn4T = time.ticks_ms()
        Fsm.brightDw()

def Init():
    btn1Pin.irq(btn1Cb, trigger=Pin.IRQ_RISING)
    btn2Pin.irq(btn2Cb, trigger=Pin.IRQ_RISING)
    btn3Pin.irq(btn3Cb, trigger=Pin.IRQ_RISING)
    btn4Pin.irq(btn4Cb, trigger=Pin.IRQ_RISING)

