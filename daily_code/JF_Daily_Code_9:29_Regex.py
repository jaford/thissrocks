#This program is intended to practice with regex

import re


pattern = "[\dreg]"
string = "This is a test of regex. blah blah blah.  let's see what what letters I can pull out of this.  Oh wait," \
         "letters and numbers 6465.  This is regex"
#
# if re.search(pattern, string):
#     print("Found a match!")
#     print(string)
# else:
#     print("No match found")

x = re.findall(pattern,string)
print(x)