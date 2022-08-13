#!/usr/bin/env python

colors = ["red", "blue", "green", "yellow", "brown", "black"]

months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print("yellow in colors: ", ("yellow" in colors))  # <1>
print("pink in colors: ", ("pink" in colors))

print("colors: ", ",".join(colors))  # <2>

del colors[4]  # remove brown   <3>

print("removed 'brown':", ",".join(colors))

colors.remove('green')  # <4>

print("removed 'green':", ",".join(colors))

sum_of_lists = [True] + [True] + [False]  # <5>

print("sum of lists:", sum_of_lists)

product = [True] * 5  # <6>

print("product of lists:", product)
