#!/usr/bin/env python

person = 'Bob'
age = 22

print("{0} is {1} years old.".format(person, age))  # <1>
print("{0}, {0}, {0} your boat".format('row'))  # <2>
print("The {1}-year-old is {0}".format(person, age))  # <3>
print("{name} is {age} years old.".format(name=person, age=age))  # <4>
print()
print("{} is {} years old.".format(person, age))  # <5>
print("{name} is {} and his favorite color is {}".format(22, 'blue', name='Bob'))  # <6>
