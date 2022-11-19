#Write a program that will print the days of the week based on user input

def days_of_week():

    # get an input integer for num
    num = int(input('Enter a number 1-7: '))

    # print the day of the week based on num
    if num == 1:
        print('Monday')
    if num == 2:
        print('Tuesday')
    if num == 3:
        print('Wednesday')
    if num == 4:
        print('Thursday')
    if num == 5:
        print('Friday')
    if num == 6:
        print('Saturday')
    if num == 7:
        print('Sunday')

days_of_week()