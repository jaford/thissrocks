#Create a function that will take in any number of args to tell whether a number is a leap year
#
year, year2 = input('Enter a year:').split()
year = int(year)
year2 = int(year2)

if year % 4 == 0 or year2 % 4 == 0:
    print(year or year2, "is a leap year!")
else:
    print(year or year2,"is not a leap year")

# def func1(arg1, *argv):
#     # printing first arg is just with a print statement
#     print('First arguement is', arg1)
#     #printing the rest of the args is done with a for loop because it needs to iterate through *argv
#     for arg in argv:
#         print('The next arg is', arg)
#
# func1('Agrument number 1','Agrument number 2','Agrument number 3', 'Agrument number 4')

# def leap_year(*argv):
#     for arg in argv:
#         #print(arg)
#         if arg % 4 == 0 or arg % 100 and 400 == 0:
#             print(arg, 'is a leap year')
#         else:
#             print(arg, 'is not a leap year')
#
# leap_year(1899,1911,1944,1948,1954,1968, 2000, 2004, 2008, 2012, 2020, 2022)