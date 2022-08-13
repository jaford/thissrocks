#!/usr/bin/env python

fruit = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi", "ORANGE",
         "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana", "Tamarind",
         "persimmon", "elderberry", "peach", "BLUEberry", "lychee", "grape"
         ]

fruit.sort(key=str.lower)  # <1>

print(" ".join(fruit))
