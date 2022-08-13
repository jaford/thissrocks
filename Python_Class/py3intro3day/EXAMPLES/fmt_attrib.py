#!/usr/bin/env python

from datetime import date

fruits = 'apple', 'banana', 'mango'
values = [5, 18, 27, 6]
dday = date(1944, 6, 6)
pythons = {'Idle': 'Eric', 'Cleese': 'John', 'Gilliam': 'Terry',
           'Chapman': 'Graham', 'Palin': 'Michael', 'Jones': 'Terry'}

print('{0[0]} {0[2]}'.format(fruits))  # <1>
print('{f[0]} {f[2]}'.format(f=fruits))  # <2>
print()
print('{0[0]} {0[2]}'.format(values))  # <3>
print()
print('{0[Palin]} {0[Cleese]}'.format(pythons))  # <4>
print('{names[Palin]} {names[Cleese]}'.format(names=pythons))  # <5>
print()
print('{0.month}-{0.day}-{0.year}'.format(dday))  # <6>
