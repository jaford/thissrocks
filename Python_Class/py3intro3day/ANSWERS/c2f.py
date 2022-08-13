#!/usr/bin/env python
temp_str = input("Enter Celsius temp: ")
celsius = float(temp_str)
fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

