from LedController.LedController import LedController
import time

btn1Pin = 20 # Pattern FW
btn2Pin = 18 # Pattern BW
btn3Pin = 21 # Brightness UP - Party mode if pressed at boot
btn4Pin = 19 # Brightness DOWN - Mic pattern if pressed at boot
numLeds = 120 # Number of LEDs in the strip

Leds = LedController(numLeds, btn1Pin, btn2Pin, btn3Pin, btn4Pin)

Leds.init()

while True:
    Leds.run()

    time.sleep(0.1)
