#Write a program that swaps variables
def swap_variables():

# get the integer inputs for n1 and n2
    n1 = int(input('Enter the first variable: '))
    n2 = int(input('Enter the second variable: '))

# create a temporary variable and swap the values
    temp = n1
    n1 = n2
    n2 = temp

# print the values of n1 and n2
    print(f'The first swapped variable is: {n1}.')
    print(f'The second swapped variable is {n2}.')

swap_variables()