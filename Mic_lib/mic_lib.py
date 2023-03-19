from machine import Pin, ADC

micPwrPin = Pin(4, Pin.OUT, Pin.PULL_UP) # pin to power mic board
micAdc = ADC(26) # pin to read mic analog output

# Read mic analog output
def readMic():
    return micAdc.read_u16()

# Set power to mic board
def setPwr(on):
    if on:
        micPwrPin.on()
    else:
        micPwrPin.off()