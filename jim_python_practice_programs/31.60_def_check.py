# Write a program that checks if a grade is Pass or Fail

# define a function named check with argument marks
def check():
    # inside the function, check Pass or Fail using if...else statement
    if marks > 40:
        print('Pass')
    else:
        print('Fail')

marks = int(input())

#call the function
check()