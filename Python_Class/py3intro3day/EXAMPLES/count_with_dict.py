#!/usr/bin/env python

counts = {}  # <1>
with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip('\n\r')
        if breakfast_item in counts:   # <2>
            counts[breakfast_item] = counts[breakfast_item] + 1   # <3>
        else:
            counts[breakfast_item] = 1 # <4>

for item, count in counts.items():
    print(item, count)
