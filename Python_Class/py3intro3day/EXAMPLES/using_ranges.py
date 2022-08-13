#!/usr/bin/env python

print("range(1, 6): ", end=' ')
for x in range(1, 6):  # <1>
    print(x, end=' ')
print()

print("range(6): ", end=' ')
for x in range(6):  # <2>
    print(x, end=' ')
print()

print("range(3, 12): ", end=' ')
for x in range(3, 12):  # <3>
    print(x, end=' ')
print()

print("range(5, 30, 5): ", end=' ')
for x in range(5, 30, 5):  # <4>
    print(x, end=' ')
print()

print("range(10, 0, -1): ", end=' ')
for x in range(10, 0, -1):  # <5>
    print(x, end=' ')
print()
