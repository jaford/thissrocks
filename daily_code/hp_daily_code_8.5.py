"""
Boolean Practice

The python boolean logic is simply put to be true or false. 
The digital equal is either 1 or 0. From these basic elements we can
build upon complex programs! 

The Boolean operator (aka booleans) are a core data type. xw
"""

"""
Super simple udnerstanding of what the results of comparing two values can look like.
"""
from stat import FILE_ATTRIBUTE_SPARSE_FILE


print('-----------Practice 1-----------')
print(10 > 9)
print(10 == 9)
print(10 < 9)

"""
You can also print a message based upon the condition is true or false.
"""
print('-----------Practice 2-----------')
a = 200
b = 100 

if b > a:
    print('b is greater than a')
else:
    print('b is not greater than a')

"""
Evaluate Values and variables.

Using the bool() function allows you to evaluate any value. 
"""
print('-----------Practice 3-----------')
print(bool("Howdy"))
print(bool(2))

x = 15
y = "Hello"
print(bool(x))
print(bool(y))

"""
Most values are true if it has some sort of content. 

The exceptions are empty strings, "0", and empty lists!
"""
print('-----------Practice 4-----------')
bool(False)
bool(None)
bool(0)
bool('')
bool(())
bool({})
bool([])

"""
Functions can return a boolean as well! 
"""
print('-----------Practice 5-----------')
def function():
    return True
print(function())

"""
Some more boolean operators!
==
!=
and
or
not
>= (is greater than or equal to)
<= (is less tjam pr equal to)
"""
print('-----------Practice 6-----------')
def func_1(x, y):
    x = 1 
    y = 0
    x != y
print(bool(func_1(x, y)))

def func_2():
    cats = 1 
    dogs = 0 
    cats and dogs
print(bool(func_2()))

"""
To overview some basics, boolean or bool represent 
True and False. You can also refer to them as 0 and 1!
"""

"""
Conjunction (AND)
The conjuction combines two boolean expressions!

x∧y

as x and y can only be 0 or 1, all possible combinations can be written down 
in a "truth table"

The operator for conjunction is 'and'
"""
print('-----------Practice 7-----------')
False and False
False and True
True and False
True and True
"""
The last "True and True" will be the only statement that will result in a 
true for that. 
"""

"""
Disjunction (OR)

x∨y

This operation evaluates to 1 when atleast one of the variables is 1! 
"""
print('-----------Practice 8-----------')
False or False
False or True
True or False
True or True
"""
The only way to result in a true statement is when both expressions are 0(AKA False)
"""

"""
Negation (NOT)

¬x

This last operation of the boolean algebra Negation.
When using NOT, operator 0 turns into 1 and 1 turns into 0:
"""
print('-----------Practice 9-----------')
not True
not False
