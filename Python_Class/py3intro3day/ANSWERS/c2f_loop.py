#!/usr/bin/env python

while True:
    celsius = input('Enter Celsius temp: ')
    if celsius.lower().startswith('q'):
        break
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32
    print('{:.1f} C is {:.1f} F\n'.format(celsius, fahrenheit))

while True:
    celsius = input('Enter Celsius temp: ')
    try:
        if celsius.lower().startswith('q'):
            break
        celsius = float(celsius)
        fahrenheit = ((9 * celsius) / 5) + 32
        print('{:.1f} C is {:.1f} F\n'.format(celsius, fahrenheit))
    except Exception as err:
        celsius_error = str(celsius)
        print(f'{celsius_error} is not a number!')