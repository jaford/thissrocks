#Write a program that will divide chocolates and display the remainder

def chocolate_divide():

# take two integer inputs for chocolates and children
    chocolates = int(input('Enter a number of chocolates: '))
    children = int(input('Enter the number of children: '))

# find chocolates each children will get and print it
    split_chocolates = chocolates // children   #Uses floor division to calculate whole number
    remainder = chocolates % children           #Uses modules operator to calculate remainder
# find remaining chocolates and print it
    print(f'Each child will get {split_chocolates} pieces of chocolate.')
    print(f'The leftover chocolate is {remainder} pieces.')

chocolate_divide()