from module1 import addition
from module2 import userInput

# print('This is a test to see how one calls functions from the same file.\n')

# z = addition(5, 5)
# print('This is the reslt: {}'.format(z))

# def userInput():
#     userNumber1 = input('Enter your first number: ')
#     x  = int(userNumber1)
#     userNumber2 = input('Enter your second number: ')
#     y  = int(userNumber2)
#     z = addition(x, y)

#     return z

z = userInput()
print('Here is the second result: {}'.format(z))