from Neopixel_lib.neopixel import Neopixel
import Patterns.patterns, Buttons.buttons

numpix = 300
strip = Neopixel(numpix, 1, 1, "GRB")

Buttons.Init()

Patterns.fireflies(strip, numpix)
