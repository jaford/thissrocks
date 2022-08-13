#!/usr/bin/env python

print("Hello, world")
print("#------------------------")

print("Hello,", end=' ')  # <1>
print("world")
print("#------------------------")

print("Hello,", end=' ')
print("world", end='!')  # <2>
print("#------------------------")

x = "Hello"
y = "world"

print(x, y)  # <3>
print("#------------------------")

print(x, y, sep=', ')  # <4>
print("#------------------------")

print(x, y, sep='')  # <5>
print("#------------------------")
