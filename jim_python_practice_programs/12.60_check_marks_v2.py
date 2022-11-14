# Replace ___ with your code

def marks_2():
    marks = int(input('Enter a grade. 1-100.: '))

# check if user has entered valid marks or not
# also check if the student passed or failed
    if marks >= 100 or marks <= 0:
        print('Invalid Marks')
    elif marks > 40:
        print('Pass')
    else:
        print('Fail')

marks_2()