'''Attemping to make a random number picker!'''
import random

min_val = 1 
max_val = 6

# Variable that stores the users decision
roll_again = 'yes'
print('Rolling...')

# Dice roll loop if the user wants to continiue
while roll_again == 'yes' or roll_again == 'y':
    result = random.randint(min_val, max_val)   
    print('The dice roll is: {}\n'.format(result))
    roll_again = input('Roll dice again? \n')
    if roll_again == 'no' or roll_again == 'n':
        print('No more dice rolling! \n')
        break