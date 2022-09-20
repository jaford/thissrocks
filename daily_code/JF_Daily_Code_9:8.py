#Create a function that will take in any number of args to tell whether a number is a leap year
#
# year = int(input('Enter a year:'))
# print(f'The year you entered was ',year)
# if year % 4:
#     print(year, "is a leap year!")
# else:
#     print(year,"is not a leap year")

def func1(arg1, *argv):
    # printing first arg is just with a print statement
    print('First arguement is', arg1)
    #printing the rest of the args is done with a for loop because it needs to iterate through *argv
    for arg in argv:
        print('The next arg is', arg)

func1('Agrument number 1','Agrument number 2','Agrument number 3', 'Agrument number 4')