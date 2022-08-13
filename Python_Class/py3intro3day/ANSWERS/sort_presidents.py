#!/usr/bin/env python

# list to hold all presidents (will be list of lists)
all_pres = []

with open("../DATA/presidents.txt", "r") as PRES:

    for line in PRES:
        fields = line.rstrip('\n\r').split(":")
        all_pres.append(fields) # add list of fields

# sort by lname, fname
for fields in sorted(all_pres, key=lambda e: (e[1], e[2])):
    print(fields[2], fields[1], fields[6])

