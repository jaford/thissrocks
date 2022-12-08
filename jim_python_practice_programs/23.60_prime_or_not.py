# Write a program that will check whether a number is prime or not
def check_prime():
    number = int(input('Enter a number: '))

    flag = 0

# create a for loop that runs from 2 to number, not including number
    for i in range(2, number):
        if (number % i) == 0:
                # if factor is found, set flag to True
            flag = 1
                # break out of loop
            break

    # check if flag is True
    if flag:
        print("Not a Prime Number")
    else:
        print("Prime Number")


check_prime()