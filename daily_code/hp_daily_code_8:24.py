"""
Python scopes

A variable is only available from inside the region it is called. 
This is called scope! 
"""

# Local Scope
# A variable created inside a function belongs to the local scope of that function
# this can only used inside taht function! 


print('----Practice 1----')
def myfunc():
    x = 10 
    print(x)

myfunc()

# A function inside a function
# Like the function above, the variable x is not available outside the function, 
# but it is availble for any function inside the function
print('----Practice 2----')
def myfunc():
    x = 30 
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

# Global Scope 
# This variable is created in the main body of the python code and belongs to the global scope
print('----Practice 3----')
x = 25

def myfunc():
    print(x)
myfunc()

print(x)

# Naming Variables
# Making a variable that is the same inside and outside of a function, python will treat them as 
# two seperate variables. A global variable and a local variable! 
print('----Practice 4----')
x = 100 

def myfunc():
    x = 200 
    print(x)

myfunc()
print(x)

# You can use the global keyword if you want to make 
# change to a global variable inside a function.
print('----Practice 5----')
x = 400 
def myfunc():
    global x 
    x = 450

myfunc()

print(x)