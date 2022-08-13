#!/usr/bin/env python

from collections import namedtuple

knight = namedtuple('knight', 'title color quest comment')

knight_info = {}
with open('../DATA/knights.txt') as knights_in:
    for line in knights_in:
        knight_name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[knight_name] = knight(title, color, quest, comment)

for knight_name, knight in knight_info.items():
    print(knight.title, knight_name)
