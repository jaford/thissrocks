# Matching a string with a true or false value based if a string as the same characters.

string1 = 'cat'
string2 = 'tac'

if string1 == string2:
    print('These strings are the same\n')
else:
    print('These strings are not the same\n') 

# Check to see if two strings are a anagram

def check(string1, string2):

    # Sort the strings
    if(sorted(string1) == sorted(string2)):
        print('These strings are a anagram.\n')
    else:
        print('These strings are not a anagram.\n')

string1 = 'bat'
string2 = 'bay'
check(string1, string2)
