# This program is desgined to convert fahrenheit to celcius
print('-'*20,'This will convert fahrenheit to celcius','-'*20)
fahrenheit_temp =int(input('Enter a temperature in fahrenheit: '))
c_to_f_temp = (fahrenheit_temp - 32) * 5/9
print(f'The temperature in celcius is: {c_to_f_temp}')

print('-'*20,'This will convert celcius to fahrenheit','-'*20)
celcius_temp = int(input('Enter a temperature in Celcius: '))
f_to_c_temp = (celcius_temp * 9/5) + 32
print(f'{celcius_temp} degrees celcius is equal to {f_to_c_temp} degrees fahrenheit.')