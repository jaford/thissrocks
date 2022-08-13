#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
    print("Syntax: countwords.py PATTERN FILE ...")
    sys.exit()

pattern = sys.argv[1].lower()

for file_name in sys.argv[2:]:
    count = 0
    with open(file_name) as file_in:
        for line in file_in:
            if pattern in line.lower():
                count += 1
    print('''"{}" occured {} times in {}'''.format(pattern, count, file_name))
