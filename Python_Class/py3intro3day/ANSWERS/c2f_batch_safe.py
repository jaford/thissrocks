#!/usr/bin/env python
import sys

try:
    celsius = float(sys.argv[1])
except ValueError as err:
    print("Error!", err)
else:
    fahrenheit = ((9 * celsius) / 5) + 32
    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))
