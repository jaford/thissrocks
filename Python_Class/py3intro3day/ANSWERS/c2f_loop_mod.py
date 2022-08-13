#!/usr/bin/env python

from temp_conv import c2f

while True:
    user_input = input('Enter Celsius temp: ')
    if user_input.lower() == 'q':
        break
    if user_input == '':
        continue
    celsius = float(user_input)
    fahrenheit = c2f(celsius)
    print('{:.1f} C is {:.1f} F\n'.format(celsius, fahrenheit))

