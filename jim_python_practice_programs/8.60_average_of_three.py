#Write a program that will find the average of three numbers

def average_numbers():
# take three float input for number1, number2, number3 respectively
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    c = float(input('Enter the third number: '))

# find the average using formula
    average = (a + b + c)/3

# print calculated average
    print(f'The average of the numbers is: {average}.')

average_numbers()