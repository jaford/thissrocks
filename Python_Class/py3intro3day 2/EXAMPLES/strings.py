#!/usr/bin/env python

a = "My hovercraft is full of EELS"

print("original:", a)
print("upper:", a.upper())
print("lower:", a.lower())
print("swapcase:", a.swapcase()) # <1>
print("title:", a.title())  # <2>
print("e count (normal):", a.count('e'))
print("e count (lower-case):", a.lower().count('e')) # <3>
print("found EELS at:", a.find('EELS'))
print("found WOLVERINES at:", a.find('WOLVERINES')) # <4>

b = "graham"
print("Capitalized:", b.capitalize()) # <5>
