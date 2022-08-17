import re

# Attempting to mess with regular expression. 

# Regular Expression is a sequence of characters that forms a seardh pattern
# This can be used to check if a string contains the specifeid search patterm

some_txt = 'The BLA BAL BLA BLA Apple'
# This searches the string to see if it starts with "The" and ends with "Apple"
x = re.search('^The.*Apple$', some_txt)
print(type(x))
# Google or look up a cheat sheet of all the sequences. To many to list! 

print('----Practice 1----')
# Print a list of all matches 
x = re.findall('ppl', some_txt)
print(x)
# This can also return an empty list as well. 
x = re.findall('Some Random Text that is not in some_txt', some_txt)
print(x)

# Here is an example of the search function
x = re.search('\s', some_txt)
print('The first white-space character is located in position:', x.start())

# If no matches are found, it will retrun None
x = re.search('Text', some_txt)
print(x)

# Here is an example of the Split() function
# Returns a list where the string has been split at each match:
x = re.split('\s', some_txt)
print(x)

# You can also set a maxsplit parameter
x = re.split('\s', some_txt, 2)
print(x)

# Here is an example of the Sub() function
# This function replaces the matches with the text of your choice:
x = re.sub('\s', 'REKT', some_txt)
print(x)

# You can also replace the number of replacements as well:
x = re.sub('\s', 'DOUBLE REKT', some_txt, 2)
print(x)





