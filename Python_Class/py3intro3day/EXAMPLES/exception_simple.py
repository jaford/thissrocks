#!/usr/bin/env python

try:  # <1>
    x = 5
    y = "cheese"
    z = x + y
    print("Bottom of try")

except TypeError as err:    # <2>
    print("Naughty programmer! ", err)

print("After try-except")  # <3>
