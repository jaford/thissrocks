#random number guessing game
import random

correct_guess = random.randint(1,10)
print("Random number is", correct_guess) #error checking for number
guess = int(input("I'm thinking of a number between 1 and 10, what's your guess?"))
while correct_guess != guess:
    print('Keep Guessing')
    guess = int(input("I'm thinking of a number between 1 and 10, what's your guess?"))
    # break
if guess == correct_guess:
    print('You guessed my number! Good job!')

