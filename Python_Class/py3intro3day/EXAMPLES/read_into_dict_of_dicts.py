#!/usr/bin/env python

knight_info = {}

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

for name, info in knight_info.items():
    print("{} {}".format(info['title'], name))
