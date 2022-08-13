#!/usr/bin/env python

values = 123, -321, 14, -2, 0

for value in values:
    print("default: |{:d}|".format(value))  # <1>
print()

for value in values:
    print("   plus: |{:+d}|".format(value))  # <2>
print()

for value in values:
    print("  minus: |{:-d}|".format(value)) # <3>
print()

for value in values:
    print("  space: |{: d}|".format(value)) # <4>
print()
