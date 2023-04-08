from module2 import varImport, subtractionImport 

randomVar = varImport()
print('Here is you result: {}'.format(randomVar))

userNumber1 = input('Enter Number: ')
userNumber2 = input('Enter Number: ')

num = subtractionImport(userNumber1, userNumber2)
print('Here is you result: {}'.format(num))
