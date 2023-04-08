import sys
sys.path.append('..')
from functions.module1 import multiply, divide, addition, subtraction

print('Showing example how to call functions from other directories!\nPlease enter if you would like to add, subtract, multiply, or divide two numbers!\n')

userInput   = input('Enter a operator or type what you want to do: ')
userNumber1 = int(input('Pick your first number: '))
userNumber2 = int(input('Pick your second number: '))

if userInput == 'addition' or userInput == 'add' or userInput == '+':
    result = addition(userNumber1, userNumber2)
elif userInput == 'subtraction' or userInput == 'sub' or userInput == '-':
    result = subtraction(userNumber1, userNumber2)
elif userInput == 'multiply' or userInput == 'multiplaction' or userInput == '*':
    result = multiply(userNumber1, userNumber2)
elif userInput == 'division' or userInput == 'divide' or userInput == '/':
    result = divide(userNumber1, userNumber2)
else:
    print('This is a incorrect statement\nInput one: "{}"\nInput two: "{}"'.format(userNumber1, userNumber2))

if isinstance(result, int) or isinstance(result, float):
    print('Here is your result: {}\n'.format(result))
else:
    print('SOMTHING WENT BAD!\n')




