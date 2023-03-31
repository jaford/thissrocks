from module1 import addition, subtraction

def userInput():
    userNumber1 = input('Enter your first number: ')
    x  = int(userNumber1)
    userNumber2 = input('Enter your second number: ')
    y  = int(userNumber2)

    addResult = addition(x, y)
    print('\nHere is the addition result: {}\n'.format(addResult))
    subResult = subtraction(x, y)
    print('Here is the subtraction result: {}\n'.format(subResult))
    z = addResult, subResult

    return z
