#random number guessing game
#TODO: add guess counter
import random

correct_guess = random.randint(1,10)
print("Random number is", correct_guess) #error checking for number
guess = int(input("I'm thinking of a number between 1 and 10, what's your guess?"))
guesses = 1
while correct_guess != guess:
    print('Keep Guessing')
    if guess > correct_guess:
        print("Your guess is too high!")
    if guess < correct_guess:
        print("Your guess is too low!")
    guess = int(input("I'm thinking of a number between 1 and 10, what's your guess?"))
    # break
    guesses += 1
if guess == correct_guess:
    print('Good job! You guessed my number in ', (guesses), 'guesses!')