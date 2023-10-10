import machine
import time
import os

#Settings files name's list
__settingsList__ = [ "bright.txt", "simpleColorIdx.txt" ]

os.chdir("/")

def readSetting(idx=0):
    global __settingsList__

    # Check index is valid
    if (idx > len(__settingsList__)):
        print("Invalid setting index ", idx, " max is ", len(__settingsList__))
        return 0

    file = open(__settingsList__[idx])
    value = file.read()

    # Check what was read from the file
    # and make sure it's properly casted to integer
    if (value == ""):
        value = 0
    else:
        value = int(value)

    #print("Read", value)
    file.close()

    return value

def writeSetting(value, idx=0):
    file = open(__settingsList__[idx], 'w')

    file.write(str(value))
    file.close()