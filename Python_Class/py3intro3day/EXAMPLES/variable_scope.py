#!/usr/bin/env python

x = 5


def spam():
    x = 22  # <1>
    print("spam(): x is", x)
    y = "wolverine"  # <2>
    print("spam(): y is", y)


def eggs():
    print("eggs(): x is", x)  # <3>
    y = "wolverine"
    print("eggs(): y is", y)


spam()
print()
eggs()
print()
print("main: x is ", x)
