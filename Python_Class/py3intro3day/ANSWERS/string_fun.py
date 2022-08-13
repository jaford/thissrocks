#!/usr/bin/env python

name = input("Enter a full name: ")

print("name: ", name)
print("upper: ", name.upper())
print("title: ", name.title())

j_count = name.lower().count('j')
print("j count:", j_count)

print("len:", len(name))

print("position of 'jacob':", name.index('jacob'))

