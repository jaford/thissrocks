#This program is intended to practice try and except blocks
#
try:
    print(x)
except NameError:
    print("You have encountered a NameError.  Check your definitions")
else:
    print("The else statement is executed if the try block had no issies")
finally:
    print("This is the end of the try and except")

#incorporating it into some existing code

list = ['iPhone', 'iPad', 'iMac', 'iPod']
try:
    for i in list:
    # print(i)
        if i == 'iPhone' in list2:
            print(i)
except:
    print('An error occured')