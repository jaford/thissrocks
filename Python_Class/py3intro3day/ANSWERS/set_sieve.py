#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    limit = int(sys.argv[1])
else:
    limit = 50

flags = set()

print(2, end=' ')  # we know 2 is prime
for num in range(3, limit, 2):  # only test odd numbers
    if num not in flags:
        print(num, end=' ')
        for x in range(num, limit, num):
            flags.add(x)
