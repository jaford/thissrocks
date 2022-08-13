#!/usr/bin/env python

name = 'Ann'
value = 12345
nvalue = -12345

# <1>
print('[{0:10s}]'.format(name))    # <2>
print('[{0:<10s}]'.format(name))   # <3>
print('[{0:>10s}]'.format(name))   # <4>
print('[{0:^10s}]'.format(name))   # <5>
print()
print('[{0:10d}] [{1:10d}]'.format(value, nvalue))    # <6>
print('[{0:>10d}] [{1:>10d}]'.format(value, nvalue))  # <7>
print('[{0:<10d}] [{1:<10d}]'.format(value, nvalue))  # <8>
print('[{0:^10d}] [{1:^10d}]'.format(value, nvalue))  # <9>
print('[{0:=10d}] [{1:=10d}]'.format(value, nvalue))  # <10>
