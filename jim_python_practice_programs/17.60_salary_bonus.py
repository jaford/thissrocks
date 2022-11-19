# Calculate the bonus of an employee if they have worked for more than 5 years

def salary_calc():

# take float input for salary
    salary = float(input('Enter Salary: '))

# take integer input for years
    years = int(input('Enter years of service: '))

# check if years worked is greater than 5 or not
    if years > 5:
# calculate bonus using 5 * salary / 100
        bonus = salary * 5 /100
# print bonus
        print(bonus)
    else:
        print('You have not worked for more than 5 years.')

salary_calc()