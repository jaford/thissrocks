#!/usr/bin/env python

a_lines = []
b_lines = []

with open("../DATA/alt.txt") as f_in:
    for line in f_in:
        if line.startswith('a'):
            a_lines.append(line)
        elif line.startswith('b'):
            b_lines.append(line)

with open("a_sorted.txt", "w") as a_out:
    a_out.writelines(sorted(a_lines))

with open("b_sorted.txt", "w") as b_out:
    b_out.writelines(sorted(b_lines, reverse=True))
