#!/usr/bin/env python

fruit1 = set()
with open("../DATA/fruit1.txt") as fruit1_in:
    for raw_line in fruit1_in:
        fruit = raw_line.rstrip().lower()
        fruit1.add(fruit)

fruit2 = set()
with open("../DATA/fruit2.txt") as fruit2_in:
    for raw_line in fruit2_in:
        fruit = raw_line.rstrip().lower()
        fruit2.add(fruit)

common_fruits = fruit1 & fruit2

print(common_fruits)
