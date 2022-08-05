"""
Dictionary Practice

Python dictionaries stores data in key:value pairs. 
"""
import this


print('-----------Practice 1-----------')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)

print('-----------Practice 2-----------')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict['brand'])

"""
It is important to note that Python 3.7 dictionaries are 
ordered. Meaning that an item has a defined order. 
Where older versions have unordered dictionaries. That means that 
you can not refer to an item using an index.
"""

"""
No duplicate keys allowed!
"""
print('-----------Practice 3-----------')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2000
}
print(thisdict)

"""
You can list the amount of items in said dictionary.
"""
print('-----------Practice 4-----------')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(len(thisdict))

"""
You can print out the type as well!
"""
print('-----------Practice 5-----------')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "electric" : False,
    "colors" : ['red', 'white', 'blue']
}
print(type(thisdict))

"""
Accessing items
"""
print('-----------Practice 6-----------')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "electric" : False,
    "colors" : ['red', 'white', 'blue']
}
x = thisdict["model"]
# OR 
x = thisdict.get('model')
print(x)

"""
You can also get a list of the keys as well! 
"""
print('-----------Practice 7-----------')

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "electric" : False,
    "colors" : ['red', 'white', 'blue']
}
x = thisdict.keys()
print(x)

"""
Lets add a new item to this dictionary and see what happens when we print
it out before and after!  
"""
print('-----------Practice 8-----------')

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
}

print('**Before**')
x = car.keys()
print(x)

car['color'] = 'white'

print('**After**')
print(x)

"""
You can also grab the value as well by using the code bellow!   
"""
print('-----------Practice 9-----------')
x = car.values()
print(x)

"""
We can also change the values in the dictionary as well! 
"""
print('-----------Practice 10-----------')

bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}

print('**Before**')
x = bike.values()
print(x)

bike['color'] = 'white'

print('**After**')
print(x)

"""
If we use the item() method, this will return each item in a dictionary,
as tuples in a list. 
"""
print('-----------Practice 11-----------')
x = bike.items()
print(x)

"""
Makeing a change in the orginal dicitionary, and see that the items list gets updated 
as well!
"""
print('-----------Practice 12-----------')

bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013
}

print('**Before**')
x = bike.items()
print(x)

bike['year'] = 2020

print('**After**')
print(x)

"""
Add a new intem to the orginal dictionary, and see that the items list gets updated as well! 
"""
print('-----------Practice 13-----------')

bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}

print('**Before**')
x = bike.items()
print(x)

bike['color'] = 'white'

print('**After**')
print(x)

"""
To see if a spefic key is present, in a dictionary use the 'in' keyword! 
"""
print('-----------Practice 14-----------')

bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}
if 'model' in bike:
    print('Yes, "Model" is one of the keys in the bike dictionary!')
x = bike["model"]
print('--> {}'.format(x))

"""
You can also update and change dictionary items! 
"""
print('-----------Practice 15-----------')

bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}
bike.update({"year" : 2022})
print(bike)

"""
You can also use the update() to add items as well! 
"""
print('-----------Practice 16-----------')

bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}
bike.update({"engin_size" : '848cc'})
print(bike)

"""
Several ways to remove items dictionary items.
You can use: 
pop()
popitem()
del

Also clear() method empties the dictionary
"""
print('-----------Practice 17-----------')

bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}
bike.pop("year")
#popitem removes the last inserted item!
bike.popitem()
#del removes the item with the specified key name!
del bike["model"]
print(bike)