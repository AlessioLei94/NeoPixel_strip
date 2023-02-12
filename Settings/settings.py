import machine
import time
import os

#Settings files name's list
__settingsList__ = [ "bright.txt" ]

os.chdir("/")

def readSetting(idx=0):
    global __settingsList__
    file = open(__settingsList__[idx])

    value = file.read()
    #print("Read", value)
    file.close()

    return int(value)

def writeSetting(value, idx=0):
    file = open(__settingsList__[idx], "w")

    file.write(str(value))
    #print("Written", value)
    file.close()


