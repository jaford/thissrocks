#!/usr/bin/env python

def cleanup(s):
    return s.strip().lower()

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

for old_string in spam:
    new_string = cleanup(old_string)
    print("Before: >{}<\nAfter: >{}<\n".format(old_string, new_string))
