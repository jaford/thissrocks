"""
I want to see if I can make a class all on my own without help! 
"""
print('-----------Practice 1-----------')

class Cat:

    species = "Mammal"

    def __init__(self, name, age, breed, fur_color):
        self.name = name
        self.age = age
        self.breed = breed
        self.fur_color = fur_color 

#Instantiate the Cat Class 
cat_1 = Cat('Forest', 4, 'Tabi', 'Orange')
cat_2 = Cat('Izzy', 8, 'Tabi', 'Grey')
"""
The code above is what made the class. Bellow I can call the contents in the class! 

Here I am storing (I think) the contents inside the class in order to set them without
having to write the code over and over again! You can easlily read what a class is, see the 
contents and attributes then use them in your code to do what you need it to do!  
"""
#Access the instance 
print('{} is a {} and he is {} years old. His fur color is {}!'.format(cat_1.name, cat_1.breed, cat_1.age, cat_1.fur_color))
print('{} is a {} and he is {} years old. His fur color is {}!'.format(cat_2.name, cat_2.breed, cat_2.age, cat_2.fur_color))
print('Out of both {} and {}, they are both amazing pets!'.format(cat_1.name, cat_2.name))

#Access the class attributes and instance
print('{} is a {}'.format(cat_1.name, cat_1.__class__.species))
print('{} is a {}'.format(cat_2.name, cat_2.__class__.species))

"""
I now want to take the data from the Instantiation of the cat class 
and see if I can list it, print it, and do other things with it! 
"""
print('-----------Practice 2-----------')

#creating the list
list_1 = []

#appending intances to list!
list_1.append(Cat('Forest', 4, 'Tabi', 'Orange'))
list_1.append(Cat('Izzy', 8, 'Tabi', 'Grey'))

for x in list_1:
    print(x.name, x.breed, x.age, cat_1.fur_color)

"""
Going to make a new class that does some sort of calculation! 
Then using the list.append to print out the results! 
"""
print('-----------Practice 3-----------')


class Math:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def Sum(self):
        print(self.x + self.y)

    def Sub(self):
        print(self.x - self.y)

    def Multi(self):
        print(self.x * self.y)

    def Div(self):
        print(self.x / self.y)


#creating the list
list_2 = []

#appending intances to list!
list_2.append(Math(5, 5))
list_2.append(Math(10, 5))
list_2.append(Math(2, 20))
list_2.append(Math(42, 7))

print('-----------This is Addition-----------')
for object in list_2:
    #Calling the method in the Class
    object.Sum()

print('-----------This is Subtraction-----------')
for object in list_2:
    #Calling the method in the Class
    object.Sub()

print('-----------This is Multiplcation-----------')
for object in list_2:
    #Calling the method in the Class
    object.Multi()

print('-----------This is Division-----------')
for object in list_2:
    #Calling the method in the Class
    object.Div()


