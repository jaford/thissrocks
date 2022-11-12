# Write a program that prints a formatted date with user input

def date():
# get inputs

    day = int(input('Enter a day: '))
    month = int(input('Enter a month: '))
    year = int(input('Enter a year: '))


# print the date in the given format
    print(month+'/'+ day +'/' + year)

date()