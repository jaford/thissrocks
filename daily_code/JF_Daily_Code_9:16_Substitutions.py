#code to substitute arithmetic operators

operator = input('Choose a math function. add , subtract, multiply, divide. ')
x = int(input('Enter a value for x: '))
y = int(input('Enter a value for y: '))

def math_func(operator, x,y):
    if operator == 'add':
        print('Your answer is:', x + y)
    elif operator == 'subtract':
        print('Your answer is:', x - y)
    elif operator == 'multiply':
        print('Your answer is:', x * y)
    elif operator == 'divide':
        print('Your answer is:', x / y)
    else:
        print("You didn't chooose a valid option")

math_func(operator, x,y)