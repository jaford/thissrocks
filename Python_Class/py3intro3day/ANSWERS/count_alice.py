#!/usr/bin/env python

count = 0
with open("../DATA/alice.txt") as alice_in:
    for line in alice_in:
        if "Alice" in line:
            count += 1

print("Alice occurred on {} lines in alice.txt".format(count))
