#try and except block practice
print('----------This is practice with the try except with Python----------')
print('''Syntax is as follows:
try:
    # Some Code
except:
    # Executed if error in the
    # try block
''')
def divide(x,y):
    try:
        result = x // y
        print('Your numbers divide, the answer is:', result)
    except ZeroDivisionError:
        print('Sorry, you are trying to divide by 0!')
    else:
        print('This is the else block code')
    finally:
        print('This is the end of the program')


divide(5,0)

#Try this with different numbers and note the results!