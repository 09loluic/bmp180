#!/usr/bin/python
"""
Released under the MIT License
Copyright 2015-2016 MrTijn/Tijndagamer
"""

from BMP180 import BMP180

bmp = BMP180(0x77)

print("Temp: " + str(bmp.get_temp()))
print("Pressure: " + str(bmp.get_pressure()))
print("Altitude: " + str(bmp.get_altitude()))