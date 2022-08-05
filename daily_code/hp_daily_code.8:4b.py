"""
Dictionary Practice

Python dictionaries stores data in key:value pairs. 

In this file I will be practicing loops, copy, and nested dictionaries.
"""

"""
You can loop throuhgh a dictionary via using a for loop! 
"""
print('-----------Practice 1-----------')
bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}
print('-----------Key names-----------')
#Prints the key names
for x in bike:
    print(x)
#Another way to print the keys
for x in bike.keys():
    print(x)

print('-----------Values names-----------')
#Prints the values 
for x in bike:
    print(bike[x])
#Another way to print the values
for x in bike.values():
    print(x)

print('-----------Both Keys & Values-----------')
for x, y in bike.items():
    print(x, y)

"""
You cannot copy a dict by typeing dict1 = dict2 

Many issues can arrise! 

Now if you use the copy() method!
"""
print('-----------Practice 2-----------')
bike = {
    "brand" : "Ducati",
    "model" : "Streetfighter",
    "year" : 2013,
    "color" : "Yellow"
}

my_copy_bike = bike.copy()
print(my_copy_bike)

"""
Nested dictionaries are dictionaries, IN dictionaries!!
"""
print('-----------Practice 3-----------')

my_family = {
    'child1' :{
        'name' : 'Hunter',
        'age' : 23
    },
    'child2' :{
        'name' : 'Bob',
        'age' : 20
    },
    'child3' :{
        'name' : 'Tim',
        'age' : 31
    },
}

"""
You can also create three dictionaries then make one new dictionary 
that will contain the three dictionaries.
"""

child1 = {
    'name' : 'Hunter',
    'age' : 23
}
child2 = {
    'name' : 'Bob',
    'age' : 20
}
child3 = {
    'name' : 'Tim',
    'age' : 31
}

my_family = {
    'child1' : child1,
    'child2' : child2,
    'child3' : child3
}