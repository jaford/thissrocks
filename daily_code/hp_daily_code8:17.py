# continuing more with classes and methods! 

print('----Practice 1----')
class CarModel:

    def __init__(self, model_name, model_price, model_year, max_speed, mileage):
        self.model_name = model_name
        self.model_price = model_price
        self.model_year = model_year
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return '{} is the maxium capacity for {}. '.format(capacity, self.model_name)


class CarBrand:

    def __init__(self, name, parent_company):
        self.name = name
        self.parent_company = parent_company

class Car:

    # Class Variable 
    vehicle = 'Car'
    CAR_TAX = 0.08

    def __init__(self, brand, turnsignal, honk):
        self.brand = brand
        self.turnsignal = turnsignal
        self.honk = honk

    # Class method
    def price_after_car_tax(car_price): 
        x = Car.CAR_TAX * car_price
        return float(x)
        # print('BEEP')

    # Instant Method
    def honk_horn(self): 
        print('BEEP BEEP')
        # Instant Method
    def turn_signal(self): 
        print('You have activated your turn signal')

# ----Sub Classes----
class BusModel(CarModel):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

class BusBrand(CarBrand):
    pass 

class Bus(Car):
    pass 
 
# ----Object Instantiation----
volkswagen_brand = CarBrand('Volkswagen', 'Volkswage AG.')
volkswagen_model = CarModel('Jetta', 21000, 2022, 160, 24)
volkswagen_car = Car(volkswagen_model, True, True)

print('\n----Acessing class attributes and methods through objects----')
print('----Volkswagen----')
print(volkswagen_brand.name)
print('{} are own by {}'.format(volkswagen_brand.name, volkswagen_brand.parent_company))
print('{} {}s are typically ${}'.format(volkswagen_brand.name, volkswagen_model.model_name, volkswagen_model.model_price))
print('{} horn made a {}'.format(volkswagen_model.model_name, volkswagen_car.honk_horn()))
print('The car price after tax is ${}'.format(Car.price_after_car_tax(volkswagen_model.model_price)))


toyota_brand = CarBrand('Toyota', 'Toyota Motor Corp.')
toyota_model = CarModel('Corrola', 24000, 2022, 150, 26)
toyota_car = Car(toyota_brand, True, True)
print('----Toyota----')
print(toyota_brand.name)
print(toyota_model.model_name)
print(f'The price of a {toyota_model.model_name} is ${toyota_model.model_price}. After tax this would be the price: ${Car.price_after_car_tax(toyota_model.model_price)}')


# ----Create a child class Bus----
# Using this child class, you can inherit all the variables and methods
ic_bus_brand = BusBrand('ICBus', 'Navistar International')
ic_bus_model = BusModel('IC-CE', 90000, 2017, 90000, 12)
ic_bus = Car(ic_bus_brand, True, True)
print('----IC Bus----')
print(ic_bus_brand.name)
print(ic_bus_model.model_name)
print(ic_bus_model.seating_capacity())
