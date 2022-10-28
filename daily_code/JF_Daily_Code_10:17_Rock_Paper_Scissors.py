#this is a rock, paper, scissors game played between one user and the computer

import random

def get_computer_choice():
    ramdom_number = random.randint(1, 3)

    #create a dicitionary with 3 items
    options = {1: 'rock', 2:'paper', 3:'scissors'}
    computers_choice = options[ramdom_number]

    return computers_choice

computers_choice =get_computer_choice()
print(computers_choice)

def get_user_input():
    user_input = input("Enter rock, paper or scissors ")
    #Converting the user input into lowercase
    user_input = user_input.lower()
    return user_input
result = get_user_input()
print(result)

def get_result(user_pick, computer_pick):

    #condition for user to draw
    if computer_pick == user_pick:
        return 'draw'

#condition for user to win
    elif user_pick == 'paper' and computer_pick == 'rock':
        return win
    elif user_pick == 'rock' and computer_pick == 'scissors':
        return win
    elif user_pick == 'scissors' and computer_pick == 'paper':
        return win

    #all other conditions result to loss
    else:
        return 'lose'

#oustoed of the function
computer_pick = get_computer_choice()
while True:
    user_pick = get_user_input()
    if user_pick in ['rock','paper','scissors']:
        break
result = get_result(user_pick, computer_pick)

#printing result
print(f"Computer's pick: {computer_pick}")
print(f"Your pick: {user_pick}")
print(f"You {result}")