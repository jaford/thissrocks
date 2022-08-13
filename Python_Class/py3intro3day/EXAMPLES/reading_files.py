#!/usr/bin/env python

FILE_NAME = '../DATA/mary.txt'

mary_in = open(FILE_NAME)  # <.>
# read file...
mary_in.close()  # <.>

with open(FILE_NAME) as mary_in:  # <.>
    for raw_line in mary_in:  # <.>
        line = raw_line.rstrip()  # <.>
        print(line)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()  # <.>
    print("NORMAL:")
    print(contents)
    print("=" * 20)
    print("RAW:")
    print(repr(contents))  # <.>
print('-' * 60)

with open(FILE_NAME) as mary_in:
    lines_with_nl = mary_in.readlines()  # <.>
    print(lines_with_nl)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    lines_without_nl = mary_in.read().splitlines()  # <.>
    print(lines_without_nl)
