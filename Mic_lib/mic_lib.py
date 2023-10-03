from machine import Pin, ADC

class Mic:
    def __init__(self, pwrPinNum, AdcPinNum, maxOut, baseOut):
        # pin to power mic board
        self.micPwrPin = Pin(pwrPinNum, Pin.OUT, Pin.PULL_UP)
        # pin to read mic analog output
        self.micAdc = ADC(AdcPinNum)
        # Multiplying factor used to adjust mic sensitivity
        self.amplify = 3
        # Max Mic output
        self.maxOut = maxOut
        # Base Mic output
        self.baseOut = baseOut

    # Read mic analog output
    def read(self):
        return self.micAdc.read_u16()

    # Set power to mic board
    def setPwr(self, on):
        if on:
            self.micPwrPin.on()
        else:
            self.micPwrPin.off()

    def getMaxOut(self):
        return self.maxOut

    def getBaseOut(self):
        return self.baseOut