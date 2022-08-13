#!/usr/bin/env python

with open("../DATA/fruit.txt", "r") as F:
    fruit_lines = F.readlines()

print("".join(sorted(fruit_lines)))
print()

print("".join(sorted(fruit_lines, key=str.lower)))
print()

print("".join(sorted(fruit_lines, key=lambda s: (len(s), s.lower()))))
print()

print("".join(sorted(fruit_lines, key=lambda s: (s[1].lower(), s[0].lower()))))
print()
