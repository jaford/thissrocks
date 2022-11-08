#Create a program that will split the bill between friends

def bill_split():
# get input value for total number of friends
    friends_total = int(input('What is the total number of friends?'))

# get input value for total bill
    bill = float(input('What is the total cost of the bill?'))

# calculate the tax amount
    bill_total_and_tax = bill * 1.20

# divide bill among friends
    bill_total_and_tax / friends_total

# print the split amount
    print(f'Each friend owes: {bill_total_and_tax/friends_total}')

bill_split()