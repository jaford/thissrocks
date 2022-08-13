#!/usr/bin/env python

from datetime import datetime

event = datetime(2016, 1, 2, 3, 4, 5)

print(event)  # <1>
print()

print("Date is {0:%m}/{0:%d}/{0:%y}".format(event))  # <2>
print("Date is {:%m/%d/%y}".format(event))  # <3>
print("Date is {:%A, %B %d, %Y}".format(event))  # <4>
