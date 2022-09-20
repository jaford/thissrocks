"""
New code to practice some nested if statements! 
"""

print('----Practice 1----')
while True:
    grade_input = input('Enter Students grade: ')
    try:
        if grade_input.lower().startswith('q'):
            print('You have quit the program!')
            break
        grades = float(grade_input)
        if grades > 100:
            print('This number is to high')
        if grades == 100:
            print('Studnets grade: A+')
        elif grades > 90 and grades <= 99:
            print('Studnets grade: A')
        elif grades > 80 and  grades <= 89:
            print('Studnets grade: B')
        elif grades > 70 and grades <= 79:
            print('Studnets grade: C')                        
        elif grades > 60 and grades <= 69:
            print('Studnets grade: D')
        elif grades <= 59:
            print('Studnets grade: F')
        else:
            pass
    except Exception as err:
        grades_error = str(grade_input)
        print(f'"{grades_error}" is not a number. Please enter a number between 0 to 100')
