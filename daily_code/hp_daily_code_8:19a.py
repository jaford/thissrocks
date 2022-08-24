"""
Python Arrays!

Python does not have built in support for Arrays.
Python lists can be used instead.

This shows how to use list as Arrays! A list is essentally an array from my understanding. 

"""

# Array "aka list"
cars = ['Ford', 'Volvo', 'BMW']
# Finds the first index
x = cars[0]
# modifies the index
cars[0] = 'Toyota'
# returnts the length
x = len(cars)

# Looping through the elements 
for x in cars:
    print(x)

# adding array elements 
cars.append('Honda')
# removing array elements
cars.pop(3)
# removing array elements another way.
cars.remove('Volvo')
