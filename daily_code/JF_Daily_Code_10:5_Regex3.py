#This program is intended to practice with regex, open a file and print the matches
import re


# pattern = "."
# dict = {"Boston:978", "New York:917", "Albuquerque:505", "Cupertino:408"}
# x = "Boston:978, Boston:617, New York:917, Albuquerque:505, Cupertino:408"
#defining the pattern

pattern = re.compile("(Boston:[0-9]{3})")
with open('demo_dict.txt', 'r') as x:
    x_read = x.read()
    y = re.findall(pattern, x_read)
    print(y)


    # for line in x:
    #     match = re.match(pattern, x_read)
    # print(match)

# x = {"Boston":978, "New York":917, "Albuquerque":505, "Cupertino":408}

# for key in x.keys():
#     print(key)

# x = re.findall("123.[0-9]{3}.[0-9]{4}",dict)
# print(x)

# if re.findall(".", string):
#     print("Found a match!")
# else:
#     print("No match found")