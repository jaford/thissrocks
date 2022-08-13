#!/usr/bin/env python

'''
   Provide functions for temperature conversions
'''


def c2f(celsius):
    '''
    Convert a Celsius temperature to Fahrenheit
    :param celsius: the Celsius temperature (float, int, or numeric string)
    :return: The Fahrenheit temperature as a float
    '''
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32

    return fahrenheit


def f2c(fahrenheit):
    '''
    Convert a Fahrenheit temperature to Celsius
    :param fahrenheit: the Fahrenheit temperature (float, int, or numeric string)
    :return: The Celsius temperature as a float
    '''
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5.0 / 9)

    return celsius
