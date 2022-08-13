#!/usr/bin/env python

name = 'Ann'
value = 123

print('[{:>10s}]'.format(name))    # <1>
print('[{:.>10s}]'.format(name))   # <2>
print('[{:->10s}]'.format(name))    # <3>
print('[{:.10s}]'.format(name))    # <4>
print()
print('[{:10d}]'.format(value))    # <5>
print('[{:010d}]'.format(value))   # <6>
print('[{:_>10d}]'.format(value))  # <7>
print('[{:+>10d}]'.format(value))  # <8>
