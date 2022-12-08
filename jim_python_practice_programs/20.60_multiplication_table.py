#Write a program that will print the multiplication table of a number based on user input

def multiplication_table():

    n = int(input('Enter your number: '))

# use for loop and range() function to loop from 1 to 5
    for i in range(1, 6):

# multiply user input n with each value of i and print it
        print(n*i)

multiplication_table()