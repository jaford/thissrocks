"""
Classes! 

I wanted to make a page where I can practice OOP. This topic is hard 
for me and I want to get better! I will use this file as an example!

"""
import re


print('-----------Practice 1-----------')
"""
Bellow is our class (AKA BLUEPRINT) of Parrot. An object(instance) is a instantiation of a class. When 
class is defined, only the description for the iobject is defined. Therefore, no memory or storage is 
allocated. 
"""
class Parrot:

    #Class attribute
    species = 'bird'

    #Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instantiate the Parrot Class 
blu = Parrot('Blu', 10)
woo = Parrot('Woo', 15)

#Access the class attributes
print('Blue is a {}'.format(blu.__class__.species))
print('Woo is a {}'.format(woo.__class__.species))

#Access the instance 
print("{} is {} years old!".format(blu.name, blu.age))
print("{} is {} years old!".format(woo.name, woo.age))

"""
Above we made a class for Parrot. Then we defined some attributes. 
The attributes are a characterisic of an object.

These attributes are defined inside the __init__ method of the class. 
It is the initializer method that is first run as soon as the object is created! 
"""
print('-----------Practice 2-----------')
"""
Methods

Methods are functions defined inside the body of a class. They are 
used to define the behaviors of an object!
"""

class Parrot:

    #Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #Instance method 
    def sing(self, song):
        return '{} sings {}'.format(self.name, song)

    def dance(self):
        return '{} is now dancing!'.format(self.name)

#Instantiate the object 
blu = Parrot("Blue", 10)

#Call our insance methods
print(blu.sing("'Blackbird'"))
print(blu.dance())
