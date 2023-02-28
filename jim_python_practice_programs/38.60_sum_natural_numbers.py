#Write a program to find the sum of N natural numbers by creating a function.

def find_sum():
    n = int(input('Enter a number: '))
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    print(sum)


find_sum()