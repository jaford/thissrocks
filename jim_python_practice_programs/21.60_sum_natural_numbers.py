# Write a program to find the natural sum of a number
def natural_sum():
    n = int(input('Input a number: '))

# initialize the sum variable with value 0
    sum = 0

# run loop from 1 to n
    for i in range(1, n + 1):
        # add i to sum
        sum = sum + i

# print the value of sum
    print(f'The natural sum of' ,n , 'is' ,sum)

natural_sum()