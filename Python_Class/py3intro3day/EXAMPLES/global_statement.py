#!/usr/bin/env python

x = 5


def spam():
    global x  # <1>
    x = 22  # <2>
    print("spam(): x is", x)


spam()
print("main: x is ", x)
