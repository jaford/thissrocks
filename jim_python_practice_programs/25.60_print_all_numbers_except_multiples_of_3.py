# Weite a program that will list the multiples of a number except if its divisible by 3
def multiples_of_three():
    n = int(input('Enter a number: '))

# run a for loop from 1 to n
    for i in range (1, n + 1):
# check whether i is divisible by 3
        if i % 3 == 0:
# if yes, skip the current iteration
            continue
# print value of i
        print(f'All numbers between 1 and {n} are {i}.  Except multiples of 3.')

multiples_of_three()
