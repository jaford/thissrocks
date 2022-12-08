# Create a program that will check if the user likes cars or bikes
def car_bike():
    choice = input('Which do you prefer? Car or bike? ')

# check if user entered "Car" or "car"
    if choice == 'car' or choice == 'Car':
        print('I like Car')

# check if user entered "Bike" or "bike"
    elif choice == 'bike' or choice == 'Bike':
        print('I like Bike')

car_bike()