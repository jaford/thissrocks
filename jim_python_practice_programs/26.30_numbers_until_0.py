# Write a program that will print the number the user enters except 0.

# run a while loop that is always true
while True:
    # take input for number
    number = int(input('Enter a number: '))

    # terminate the loop if the user input is 0
    if number == 0:
        break

    # print the number
    print(number)