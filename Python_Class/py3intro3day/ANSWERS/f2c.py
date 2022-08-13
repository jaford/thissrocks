#!/usr/bin/env python

from temp_conv import f2c

temp_str = input("Enter Fahrenheit temp: ")
fahrenheit = float(temp_str)
celsius = f2c(fahrenheit)

print("{:.1f} F is {:.1f} C".format(fahrenheit, celsius))

