#!/usr/bin/env python

name = "Tim"
count = 5
avg = 3.456
info = 2093

print("Name is [{:<10s}]".format(name))  # <1>
print("Name is [{:>10s}]".format(name))  # <2>
print("count is {:03d} avg is {:.2f}".format(count, avg))  # <3>

print("info is {0} {0:d} {0:o} {0:x}".format(info))  # <4>
print("info is {0} {0:d} {0:#o} {0:#x}".format(info))  # <5>

print("${:,d}".format(38293892))  # <6>

print("It is {temp} in {city}".format(city='Orlando', temp=85))  # <7>
