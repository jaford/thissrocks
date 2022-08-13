#!/usr/bin/env python

class Person():

    def __init__(self, firstname=None, lastname=None):
        self._first_name = None
        self._last_name = None
        self.first_name = firstname  # <1>
        self.last_name = lastname

    @property
    def first_name(self):  # <2>
        return self._first_name

    @first_name.setter  # <3>
    def first_name(self, value):  # <4>
        if value is None or value.isalpha():
            self._first_name = value
        else:
            raise ValueError("First name may only contain letters")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value is None or value.isalpha():
            self._last_name = value
        else:
            raise ValueError("Last name may only contain letters")


if __name__ == '__main__':
    person1 = Person('Ferneater', 'Eulalia')

    person2 = Person()
    person2.last_name = 'Pepperpot'  # <5>
    person2.first_name = 'Hortense'

    print("{} {}".format(person1.first_name, person1.last_name))
    print("{} {}".format(person2.first_name, person2.last_name))

    try:
        person3 = Person("R2D2")
    except ValueError as err:
        print(err)
    else:
        print("{} {}".format(person3.first_name, person3.last_name))
