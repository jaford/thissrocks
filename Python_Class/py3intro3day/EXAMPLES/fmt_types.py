#!/usr/bin/env python

person = 'Bob'
value = 488
bigvalue = 3735928559
result = 234.5617282027

print('{:s}'.format(person))    # <1>
print('{name:s}'.format(name=person))    # <2>
print('{:d}'.format(value))    # <3>
print('{:b}'.format(value))    # <4>
print('{:o}'.format(value))    # <5>
print('{:x}'.format(value))    # <6>
print('{:X}'.format(bigvalue))    # <7>
print('{:f}'.format(result))    # <8>
print('{:.2f}'.format(result))    # <9>
