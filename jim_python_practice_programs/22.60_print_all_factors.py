# Write a program that will list the factors of a given number
def factors():
    n = int(input('What number do you want to get factors for? '))

# create a for loop that iterates from 1 to number
    for i in range(1,n + 1):
    # check if number is perfectly divisible (remainder 0)
        if n % i == 0:
    # If yes, print i
            print(i)

factors()