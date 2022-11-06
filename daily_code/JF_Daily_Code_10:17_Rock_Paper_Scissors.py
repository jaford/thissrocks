import random


# returns either 'rock', 'paper' or 'scissors'
def get_computers_choice():
    random_number = random.randint(1, 3)

    options = {1: 'rock', 2: 'paper', 3: 'scissors'}
    computers_choice = options[random_number]

    return computers_choice


# take user input and return it
def get_user_input():
    user_input = input('Enter rock/paper/scissors: ')

    # converting the user input to lowercase
    user_input = user_input.lower()

    return user_input


# return either 'win', 'lose' or 'draw'
def get_result(user_pick, computer_pick):
    if computer_pick == user_pick:
        return 'draw'

    elif user_pick == 'paper' and computer_pick == 'rock':
        return 'win'
    elif user_pick == 'rock' and computer_pick == 'scissors':
        return 'win'
    elif user_pick == 'scissors' and computer_pick == 'paper':
        return 'win'

    else:
        return 'lose'


# outside of the function
computer_pick = get_computers_choice()

# get input until user enters 'rock', 'paper' or scissors
while True:
    users_pick = get_user_input()
    if users_pick in ['rock', 'paper', 'scissors']:
        break

result = get_result(users_pick, computer_pick)

# printing result
print(f"Computer's pick: {computer_pick}")
print(f"Your pick: {users_pick}")
print(f"You {result}")