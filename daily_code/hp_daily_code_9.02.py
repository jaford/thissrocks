"""
Small little code challanges/programs to keep practicing code
so I can better understand and remember the language as best as I can! 
"""

# Finf the reverse of a string
print('----Practice 1----')

def ReverseString(s):
    return s == s[::-1]

s = 'radar'
answer = ReverseString(s)

if answer:
    print('Yes!')
else: 
    print('No')