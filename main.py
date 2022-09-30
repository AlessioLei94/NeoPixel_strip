from Neopixel_lib.neopixel import Neopixel
from Patterns.patterns import __brightness__
import Fsm.fsm as Fsm
import time

numpix = 300
strip = Neopixel(numpix, 1, 1, "GRB")
strip.brightness(__brightness__)

Fsm.init(strip, numpix)

while True:
    Fsm.run()

    time.sleep(0.1)
