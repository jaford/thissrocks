#!/usr/bin/env python

colors = "red blue green yellow brown black".split()

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

for i, color in enumerate(colors):  # <1>
    print(i, color)

print()


for num, month in enumerate(months, 1):  # <2>
    print("{} {}".format(num, month))
