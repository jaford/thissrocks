#!/usr/bin/env python

def c2f(celsius):
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32

    return fahrenheit

while True:
    raw_celsius = input('Enter Celsius temp: ')
    if raw_celsius.lower().startswith('q'):
        break
    c = float(raw_celsius)
    f = c2f(c)
    print('{:.1f} C is {:.1f} F\n'.format(c, f))

