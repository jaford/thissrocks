print('Enter "q" to quit this program!\n')
user_input = input('Type in a number: ')
user_input_2 = input('Type in a number: ')
# This "or" statement needs some more thought tbh
if user_input or user_input_2 == 'q': 
    print('You are on the first "if"')
else:
    print('You are at the else')
