#!/usr/bin/env python

set1 = {'red', 'blue', 'green', 'purple', 'green'}  # <1>
set2 = {'green', 'blue', 'yellow', 'orange'}

set1.add('taupe')  # <2>

print(set1)
print(set2)
print(set1 & set2)  # <3>
print(set1 | set2)  # <4>
print(set1 ^ set2)  # <5>
print(set1 - set2)  # <6>
print(set2 - set1)
print()

food = 'spam ham ham spam spam spam ham spam spam eggs cheese spam'.split()
food_set = set(food)  # <7>
print(food_set)
