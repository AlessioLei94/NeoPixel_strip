from Neopixel_lib import neopixel
import Buttons.buttons as Buttons
import Patterns.patterns as Patterns
import Fsm.fsm as Fsm
import time

numpix = 120
strip = neopixel.Neopixel(numpix, 1, 15)

Fsm.init(strip, numpix)


while True:
    Fsm.run(Buttons.checkMode())

    time.sleep(0.1)
