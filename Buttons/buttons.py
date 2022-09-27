from machine import Pin
import Fsm
import time

btn1Pin = Pin(18, Pin.OUT)
btn2Pin = Pin(19, Pin.OUT)
btn3Pin = Pin(20, Pin.OUT)
btn4Pin = Pin(21, Pin.OUT)

btn1T = 0
btn2T = 0
btn3T = 0
btn4T = 0

def btn1Cb(pin):
    global btn1T
    if(btn1T == 0):
        btn1T = time.ticks_ms()
        return
    elif((time.ticks_ms() - btn1T) < 200):
        btn1T = time.ticks_ms()
        return
    
    Fsm.patternFW()

def btn2Cb(pin):
    print("BTN2 callback")

def btn3Cb(pin):
    print("BTN3 callback")

def btn4Cb(pin):
    print("BTN4 callback")

def Init():
    btn1Pin.irq(btn1Cb)
    btn2Pin.irq(btn2Cb)
    btn3Pin.irq(btn3Cb)
    btn4Pin.irq(btn4Cb)
