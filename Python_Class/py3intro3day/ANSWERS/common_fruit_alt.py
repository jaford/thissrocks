#!/usr/bin/env python

with open("../DATA/fruit1.txt") as fruit1_in:
    file_contents = fruit1_in.read()
    fruits = file_contents.lower().splitlines()
    fruit1 = set(fruits)

with open("../DATA/fruit2.txt") as fruit2_in:
    file_contents = fruit2_in.read().lower()
    fruits = file_contents.lower().splitlines()
    fruit2 = set(fruits)

common_fruits = fruit1 & fruit2

print(common_fruits)
