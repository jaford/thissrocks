#Write a program that will check whether a number is even or odd

def odd_even():
# take input for number
    user_input = int(input('Enter a number to check if it is odd or even: '))

# check Even or Odd using if-else
    if user_input % 2 == 0:
        print('The number is even!')
    else:
        print('The number is odd')

odd_even()