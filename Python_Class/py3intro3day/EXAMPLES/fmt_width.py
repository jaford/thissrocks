#!/usr/bin/env python

name = 'Ann Elk'
value = 10000
airspeed = 22.347
# note: [] are used to show blank space, and are not part of the formatting
print('[{:s}]'.format(name))     # <1>
print('[{:10s}]'.format(name))   # <2>
print('[{:3s}]'.format(name))    # <3>
print('[{:3.3s}]'.format(name))  # <4>
print()
print('[{:8d}]'.format(value))       # <5>
print('[{:8f}]'.format(value))       # <6>
print('[{:8f}]'.format(airspeed))    # <7>
print('[{:.2f}]'.format(airspeed))   # <8>
print('[{:8.3f}]'.format(airspeed))  # <9>
