#!/usr/bin/env python

my_list = ["Idle", "Cleese", "Chapman", "Gilliam", "Palin", "Jones"]
my_tuple = "Roger", "Old Woman", "Prince Herbert", "Brother Maynard"
my_str = "She turned me into a newt"

for p in my_list:  # <1>
    print(p)
print()

for r in my_tuple:  # <2>
    print(r)
print()

for ch in my_str:  # <3>
    print(ch, end=' ')
print()
