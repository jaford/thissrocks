# Write a program that will list if a user has entered a positive number
def positive_number():
# run a while loop that is always True
    while True:
    # take integer input for number
        number = int(input('Enter a number: '))

    # check if user input is less than 0. If yes, skip the number
        if number < 0:
            print('Your number is less than or equal to 0.  Terminating program')
        continue

        print(number)

positive_number()