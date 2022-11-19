# Write a program that will let the user know if they can vote or not
def voting():
    age = int(input('How old are you? '))

# check if eligible to vote
    if age >= 18:
        print('Can Vote')
    else:
        print('Cannot Vote')

voting()