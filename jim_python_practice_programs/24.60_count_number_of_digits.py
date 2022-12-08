# Replace ___ with your code

number = int(input('Enter a number: '))

count = 0

# run loop as long as number != 0
while number != 0:
    # divide number by 10
    number //= 10

    # increase count by 1
    count += 1

# print count
print(f'The number is {count} digits long.')