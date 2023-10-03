from machine import Pin
import time

__debounceT_ = 500

class Button:
    def __init__(self, pinNum, onPress, onRelease=None):
        self.onPress = onPress
        self.onRelease = onRelease
        self.lastPress = 0

        self.pin = Pin(pinNum, Pin.IN, Pin.PULL_DOWN)
        self.pin.irq(self.__onPress, trigger=Pin.IRQ_RISING)

    def getState(self):
        return self.pin.value()

    def __onPress(self, pin):
        if((time.ticks_ms() - self.lastPress) > __debounceT_ or (self.lastPress == 0)):
            self.lastPress = time.ticks_ms()
            self.onPress()