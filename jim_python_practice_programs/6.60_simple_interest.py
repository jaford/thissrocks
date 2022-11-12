#Write a program to calculate simple interest
# Replace ___ with your code

def simple_interest():
# take float input for principal, rate, and time
    P = float(input("Enter the principal amount: "))
    R = float(input("Enter the interest rate: "))
    T = float(input("Enter the time in years: "))
# calculate the simple interest
    interest = P * R * T * .01

# calculate the final amount
    total_sum = P + interest

# print interest and total_sum in separate lines
    print(f'The amount paid in interest is: {interest}')
    print(f'The total amount paid is: {total_sum}')

simple_interest()