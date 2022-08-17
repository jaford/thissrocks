"""
I wanted to make more practice with classes and objects before stepping into systriage! 
This can be a good way to make sure I understand lines and how they are setup! 
"""

"""
Syntax
obj = MyClass()
print(obj.x)
"""
print('----This is the start of my class----')
class Bike:
    def __init__(self, m, p):
        self.model = m
        self.price = p

print('----This is adding/assigning attributes to said class----')
Ducati = Bike('Streesfighter & the price is: ', 10000)
print(Ducati.model)
print(Ducati.price)

"""
Syntax 

obj_name.var_name
Ducati.model

obj_name.method_Name()
Ducati.ShowModel();

obj_name.method_name(parameter_list)
Ducati.ShowModel(100);

"""
print('\n----Practice 1----')

class Bike: 

    # Class Variable
    vehicle = 'bike'

    # The init method or contructor
    def __init__(self, model):

        # Instance Varaible
        self.model = model

    # Adds an instance Variable
    def setprice(self, price):
        self.price = price

    # Retrieves instance Variable 
    def getprice(self):
        return self.price

# Drive Code 
BMW = Bike('GS')
BMW.setprice(10000)
print(BMW.getprice())

print('\n----Practice 2----')
class CarBrand:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    

class Car:

    # Class Variable 
    vehicle = 'Car'
    CAR_TAX = 0.2

    def __init__(self, brand, price=None):
        self.price = brand.price
        self.number_of_doors = 4
        self.brand = brand

    # Class method
    def price_after_car_tax(car_price): 
        return Car.CAR_TAX * car_price
        # print('BEEP')

    # Instant Method
    def honk_horn(self): 
        print('BEEP: {}'.format(self.price))

volkswagon_brand = CarBrand('Volkswagon', 32000)
volkswagon_car = Car(volkswagon_brand)
print(volkswagon_brand.price)
print(volkswagon_car.brand.name)
volkswagon_car.price = 100
volkswagon_brand.price = 500
print(volkswagon_car.brand.price)
print(volkswagon_car.price)


toyota_brand = CarBrand('Toyota', 15000)


# Objects of class
car_name = 'BMW'
car_age_years = 3
volkswagon = Car(volkswagon_brand)
toyota_car = Car(toyota_brand)
print(toyota_car.price)
volkswagon.price = 10000

print('----Volkswagon Car Detail----')
print('Volkswagon is a {}'.format(Car.vehicle))
print('Volkswagon price is {}'.format(volkswagon.price))
volkswagon.honk_horn()
Car.price_after_car_tax(20000)
Car.price_after_car_tax(volkswagon.price)


print('Toyota price is {}'.format(toyota_car.price))
print('Volkswagon is a {}'.format(volkswagon.number_of_doors))
print('Model: {}'.format(volkswagon.brand.name))
print('Price: ${}'.format(volkswagon.price))


print('----Toyota Car Detail----')
print('Toyota is a {}'.format(toyota_car.vehicle))
print('Model: {}'.format(toyota_car.brand.name))
print('Price: ${}'.format(toyota_car.price))

# Class variables can be accessed using class
# name also!
print('\nAcessing Class variable using class name')
print(Car.vehicle)

# or
print(volkswagon.vehicle)

# or 
print(toyota_car.vehicle)

print('\n----Practice 3----')

# This one is a tad confusing.
# SELF is a defult variable that contains the memory address of the 
# current object. Intance variables and methods can be referred to 
# by the self variable. 
class Test:
    def __init__(MyObject, a, b):
        MyObject.state = a 
        MyObject.city = b 
    
    def myfunction(abc):
        print('I live in {}, {}! It is really nice!'.format(abc.city, abc.state))

x = Test('Albuquerque', 'New Mexico')
x.myfunction()