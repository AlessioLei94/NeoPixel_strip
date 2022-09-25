from Neopixel_lib.neopixel import Neopixel
from Patterns.patterns import *

numpix = 300
strip = Neopixel(numpix, 1, 1, "GRB")


colorwave(strip, numpix)

fireflies(strip, numpix)
