# #This program is degsigned to calculate the average grade of a student and give the user what the grade is

n1 = int(input('Enter the first grade: '))
n2 = int(input('Enter the second grade: '))
n3 = int(input('Enter the third grade: '))
n4 = int(input('Enter the fourth grade: '))
grade_average = (n1 + n2 +n3 + n4)/4

def average_grade(n1, n2, n3, n4):
#     print('Calculating average grade....')
# grade_average = (n1 + n2 +n3 + n4)/4
    print(f"You're GPA is: {grade_average}")

if grade_average <= 100 and grade_average >= 90:
    print('You get an A!')
elif grade_average <= 89 and grade_average >= 80:
    print('You get an B!')
elif grade_average <= 79 and grade_average >= 70:
    print('You get an C!')
elif grade_average <= 69 and grade_average >= 60:
    print('You get an D!')
else:
    print('Sorry, you get an F')

#Similar Program but passing in a list

# scores = [85, 80, 90, 88]
# def average_grade(scores):
#     print("Calculating average score...")
#
# total = sum(scores)
# count = len(scores)
# avg_score = total/count
#
# print(avg_score)
#
# print(f"You're GPA is: {avg_score}")
#
# if avg_score <= 100 and avg_score >= 90:
#     print('You get an A!')
# elif avg_score <= 89 and avg_score >= 80:
#     print('You get an B!')
# elif avg_score <= 79 and avg_score >= 70:
#     print('You get an C!')
# elif avg_score <= 69 and avg_score >= 60:
#     print('You get an D!')
# else:
#     print('Sorry, you get an F')