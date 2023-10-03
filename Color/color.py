class Color:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def getRGB(self):
        return self.R, self.G, self.B

# List of supported colors
red = Color(255, 0, 0)
orange = Color(255, 165, 0)
yellow = Color(255, 150, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)
indigo = Color(75, 0, 130)
violet = Color(138, 43, 226)
lightBlue = Color(18, 204, 198)
lightGreen = Color(37, 184, 20)
waterGreen = Color(35, 207, 115)
darkOrange = Color(150, 50, 10)
acidGreen = Color(50, 200, 10)
purple = Color(232, 100, 255)