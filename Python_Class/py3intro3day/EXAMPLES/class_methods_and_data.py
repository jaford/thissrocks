#!/usr/bin/env python

class Rabbit:
    LOCATION = "the Cave of Caerbannog"  # <1>

    def __init__(self, weapon):
        self.weapon = weapon

    def display(self):
        print("This rabbit guarding {} uses {} as a weapon".
              format(self.LOCATION, self.weapon))  # <2>

    @classmethod  # <3>
    def get_location(cls):  # <4>
        return cls.LOCATION  # <5>


r = Rabbit("a nice cup of tea")
print(Rabbit.get_location())  # <6>
print(r.get_location())  # <7>
