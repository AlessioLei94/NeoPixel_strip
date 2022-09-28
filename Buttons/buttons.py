from machine import Pin
import Fsm.fsm as Fsm
import time

btn1Pin = Pin(18, Pin.IN, Pin.PULL_DOWN)
btn2Pin = Pin(19, Pin.IN, Pin.PULL_DOWN)
btn3Pin = Pin(20, Pin.IN, Pin.PULL_DOWN)
btn4Pin = Pin(21, Pin.IN, Pin.PULL_DOWN)

btn1T = 0
btn2T = 0
btn3T = 0
btn4T = 0

def btn1Cb(pin):
    global btn1T

    if((time.ticks_ms() - btn1T) > 1000 or (btn1T == 0)):
        btn1T = time.ticks_ms()
        Fsm.patternFW()

def btn2Cb(pin):
    global btn2T

    if((time.ticks_ms() - btn2T) > 1000 or (btn2T == 0)):
        btn2T = time.ticks_ms()
        Fsm.patternBW()

def btn3Cb(pin):
    print("BTN3 callback")

def btn4Cb(pin):
    print("BTN4 callback")

def Init():
    btn1Pin.irq(btn1Cb, trigger=Pin.IRQ_RISING)
    btn2Pin.irq(btn2Cb, trigger=Pin.IRQ_RISING)
    btn3Pin.irq(btn3Cb, trigger=Pin.IRQ_RISING)
    btn4Pin.irq(btn4Cb, trigger=Pin.IRQ_RISING)

