#This program is intended to practice with regex
#find and print the match
import re


# pattern = "."
string = "123-654-8545, 321-654-8789, 789-654-2354, 123-698-7856"

x = re.findall(".",string)
print(x)

if re.findall(".", string):
    print("Found a match!")
    print(string)
else:
    print("No match found")