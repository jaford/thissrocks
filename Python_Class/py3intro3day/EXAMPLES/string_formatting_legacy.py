#!/usr/bin/env python

name = "Tim"
count = 5
avg = 3.456
info = 2093

print("Name is [%-10s]" % name)   # <1>
print("Name is [%10s]" % name)   # <2>
print("count is %03d avg is %.2f" % (count, avg)) # <3>

print("info is %d %o %x" % (info, info, info))      # <4>
print("info is %d %o %x" % ((info,) * 3))    # <5>

print("info is %d %#oo %#x" % (info, info, info))    # <6>
