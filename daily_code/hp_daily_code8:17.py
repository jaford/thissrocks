# continuing more with classes and methods! 

print('----Practice 1----')
class CarModel:

    def __init__(self, model_name, model_price, model_year):
        self.model_name = model_name
        self.model_price = model_price
        self.model_year = model_year

class CarBrand:

    def __init__(self, name, parent_company):
        self.name = name
        self.parent_company = parent_company

class Car:

    # Class Variable 
    vehicle = 'Car'
    CAR_TAX = 0.08

    def __init__(self, brand, turnsignal, honk):
        self.number_of_doors = 4
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


 
# ----Object Instantiation----
volkswagen_brand = CarBrand('Volkswagen', 'Volkswage AG.')
volkswagen_model = CarModel('Jetta', 21000, 2022)
volkswagen_car = Car(volkswagen_model, True, True)

print('\n----Acessing class attributes and methods through objects----')
print(volkswagen_brand.name)
print('{} are own by {}'.format(volkswagen_brand.name, volkswagen_brand.parent_company))
print('{} {}s are typically ${}'.format(volkswagen_brand.name, volkswagen_model.model_name, volkswagen_model.model_price))
print('{} horn made a {}'.format(volkswagen_model.model_name, volkswagen_car.honk_horn()))
print('The car price after tax is ${}'.format(Car.price_after_car_tax(volkswagen_model.model_price)))


toyota_brand = CarBrand('Toyota', 'Toyota Motor Corp.')
toyota_model = CarModel('Corrola', 24000, 2022)
toyota_car = Car(toyota_brand, True, True)

