"""
Beep boopin on some classes once more. 
"""
# Created a class 
class MyClass():
    x = 5

print('----Practice 1----')
# Create object 
p1 = MyClass()
print(p1.x)

"""
The __init___() Function 

These examples are not really good on what real world 
scenarios may look like, but at least show somewhat on how it may be 
set up. 

All classes have this function. Which is always executed when the class is 
being initiated.

Use the __init__() function to assign values to object properties, or other operations
that are necessary to do when the object is being created!
"""
class Person():

    """
    Note that 'self' parameter is a referance to the current instance of the class,
    and is used to access variables that belongs to the class. 

    It does not have to be named self. You can call it whatever you like. 
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Creating a method
    def myfunc(self):
        print('Hello my name is {}'.format(self.name)) 
"""
Please note that the __init__() function is called automatically every time 
the class is being used to create a new object. 
"""
print('----Practice 2----')
p1 = Person('Bob', 22)

print(p1.name)
print(p1.age)

"""
Object Method. 

Objects can also contain methods. Methods in objects are functions that belon to the object.
"""
print('----Practice 3----')
p1 = Person('John', 30)
p1.myfunc()

# Modify Object Properties 
p1.age = 40

# Delete Object Properties 
del p1.age
# Delete Objects 
del p1

"""
Python Inheritance 

Inheritance allows us to define a class that inherits all the methods and properties
from another class. 

Parents class: The class being inherited from also called base class. 

Sub Class: The class that inherits from another class, also called derived class. 
"""
class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

# Use the Person Class to create an object and then execute the printname method:
print('----Practice 4----')
x = Person('John', 'Doe')
x.printname()

x = Student('Mike', 'Doe')
x.printname()

"""
When adding the __init__() function to the sub class,
the function is called automatically every time the class is being used 
to create a new object. 

When you add __init__() function, the sub class will no longer inherit the parents __inits__() function.
This function overrides the inheritance of the parents __inits__() function.
"""
class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
"""
Use the super() function!

Python also has a super() function that will make the child class inherit all the 
methods and properties from its parents: 
"""
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # Adding properties
        self.graduationyear = year
    
    # You can also add methods
    def welcome(self):
        print('Welcome', self.firstname, self.lastname, 'to the class of', self.graduationyear) 

x = Student('Mike', 'Olsen', 2019)