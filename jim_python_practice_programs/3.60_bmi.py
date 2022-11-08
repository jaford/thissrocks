#Create BMI Calculator

def bmi_calc():
# take float input for weight
    weight = float(input('Enter weight in kg: '))

# take float input for height
    height = float(input('Enter height in meters: '))

# calculate BMI
    bmi = weight / height ** 2

# print the calculated BMI
    print(f'Your bmi is: {bmi}')

bmi_calc()