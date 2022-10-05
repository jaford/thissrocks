#This program is intended to practice with regex
#find and print the match
#print only the phone numbers with area code 123
import re


# pattern = "."
string = "123-654-8545, 321-654-8789, 789-654-2354, 123-698-7856"

x = re.findall("123.[0-9]{3}.[0-9]{4}",string)
print(x)

# if re.findall(".", string):
#     print("Found a match!")
# else:
#     print("No match found")