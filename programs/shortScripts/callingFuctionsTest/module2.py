from module1 import addition

def userInput():
    userNumber1 = input('Enter your first number: ')
    x  = int(userNumber1)
    userNumber2 = input('Enter your second number: ')
    y  = int(userNumber2)
    z = addition(x, y)

    return z
