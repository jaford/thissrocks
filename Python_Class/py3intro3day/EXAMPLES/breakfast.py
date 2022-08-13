#!/usr/bin/env python
'''
Spam -- provides a tasty breakfast
'''

# separator for toast toppings
TOPSEP = " and "


def eggs(how):
    '''cook some eggs'''
    print("Cooking up some lovely {} eggs".format(how))


def toast(*toppings):
    '''cook some toast'''
    print("Toasting up some toast with ", TOPSEP.join(toppings))
