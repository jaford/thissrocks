#!/usr/bin/env python

light, medium_light, medium, medium_dark, dark = range(0x1F3FB,0x1F400)
for skin_tone in light, medium_light, medium, medium_dark, dark:
    print("{0}{1}{2}{1}".format("\U0001F469", chr(skin_tone), "\U0001F91A"))

