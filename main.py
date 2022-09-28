from Neopixel_lib.neopixel import Neopixel
import Fsm.fsm as Fsm
import time

numpix = 300
strip = Neopixel(numpix, 1, 1, "GRB")

while True:
    Fsm.run(strip, numpix)

    time.sleep(0.1)
