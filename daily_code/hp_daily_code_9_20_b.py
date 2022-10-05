"""
Lets see how I can extract items from a dictionary and list 

Also combining two lists as well! 
"""

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.milage = mileage

# Class inheritance
class Bus(Vehicle):
    pass

print('----Practice 1----')
Tesla = Vehicle('ModelX', 240, 18)
print(Tesla.name, Tesla.max_speed, Tesla.milage)