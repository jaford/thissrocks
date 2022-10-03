# This program is desgined to convert fahrenheit to celcius

user_choice = int(input('Choose 1 or 2. CHOICE 1 will convert Celcius to Fahrenheit. CHOICE 2 will convert Fahrenheit to Celcius.'))
if user_choice == 1:
    celcius_temp = int(input('Enter a temperature in Celcius: '))
    f_to_c_temp = (celcius_temp * 9 / 5) + 32
    print(f'{celcius_temp} degrees celcius is equal to {f_to_c_temp} degrees fahrenheit.')

if user_choice == 2:
    fahrenheit_temp = int(input('Enter a temperature in fahrenheit: '))
    c_to_f_temp = (fahrenheit_temp - 32) * 5 / 9
    print(f'The temperature in celcius is: {c_to_f_temp}')

else:
    user_choice < 2 or user_choice == str
    print('You entered an invalid choice')