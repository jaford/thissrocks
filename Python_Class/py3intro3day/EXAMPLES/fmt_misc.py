#!/usr/bin/env python

'''Demonstrate misc formatting'''

big_number = 2303902390239

print("Big number: {:,d}".format(big_number))  # <1>
print()

value = 27

print("Binary: {:#010b}".format(value))  # <2>
print("Octal:  {:#010o}".format(value))  # <3>
print("Hex:    {:#010x}".format(value))  # <4>
print()
