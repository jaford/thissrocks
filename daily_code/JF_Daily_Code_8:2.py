#random number guessing game
#TODO: add guess counter
import random
correct_guess = random.randint(1,10)
print("Random number is", correct_guess) #error checking for number
guess = 0
attempts = 3
while correct_guess != guess:
    guess = int(input("I'm thinking of a number between 1 and 10, can you guess it in three guesses or less?"))
    attempts -= 1
    if guess > correct_guess:
        print("Keep guessing! Your guess is too high!")
    if guess < correct_guess:
        print("Keep guessing! Your guess is too low!")
    if attempts == 0 :
            print("You've used too many guesses! My secret number was", str(correct_guess),"!")
            break
    if guess == correct_guess:
        print('Good job! You guessed my number!')