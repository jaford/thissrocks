#Create a program that will check someone's grade based on int provided'

def marks():

    marks = int(input('Enter a grade integar: '))

# check if Pass or Fail using if…else statement
    if marks >= 40:
        print('Pass')
    else:
        print('Fail')

marks()