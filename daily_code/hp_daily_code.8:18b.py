"""
Python Lamdba

This is a small anonymous function.
Lambda can take any number of arguments, but can only have one expression 
"""

# The Basic Syntax
"""
lambda arguments : expression
"""
print('----Practice 1----')
x = lambda a : a + 10
print(x(5))

print('----Practice 2----')
x = lambda a, b : a * b
print(x(5, 5))

"""
Why use Lambda? 

Occording to W3Schools this is good for using them as an
anonymous function inside another function. 

Here is an example. 
"""
print('----Practice 3----')
def func(n):
    return lambda a : a * n

x = func(2)

print(x(6))