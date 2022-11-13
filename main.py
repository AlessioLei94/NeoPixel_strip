from Neopixel_lib import neopixel
import Patterns.patterns as Patterns
import Fsm.fsm as Fsm
import time

numpix = 300
strip = neopixel.Neopixel(numpix, 1, 1, "GRB")
strip.brightness(Patterns.__brightness__)

Fsm.init(strip, numpix)

while True:
    Fsm.run()

    time.sleep(0.1)
