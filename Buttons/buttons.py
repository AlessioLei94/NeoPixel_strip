from machine import Pin

btn1Pin = Pin(18, Pin.OUT)
btn2Pin = Pin(19, Pin.OUT)
btn3Pin = Pin(20, Pin.OUT)
btn4Pin = Pin(21, Pin.OUT)

def btn1Cb(pin):
    print("BTN1 callback")

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
