#!/usr/bin/env python

from temp_conv import c2f

temp_str = input("Enter Celsius temp: ")
celsius = float(temp_str)
fahrenheit = c2f(celsius)

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

