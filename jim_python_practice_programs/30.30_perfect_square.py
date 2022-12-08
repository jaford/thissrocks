# Write a program that will calculate if a number is a perfect square or not

# import math module
import math

def perfect_square():

    number = int(input('Enter a number to see if it is a perfect square: '))

    # use sqrt() to find the square root of the number
    square_root = math.sqrt(number)

    # get remainder of the square root by using % with 1
    check_remainder = square_root % 1

    # if the remainder is equal to 0, print "Perfect Square" Else print "Not a Perfect Square"
    if check_remainder == 0:
        print("Perfect Square")
    else:
        print("Not a Perfect Square")