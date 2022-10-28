#You're given the string, 'Hi {Bob} How are you?
#Write a function that would print out Hi, How are you and Hi {Bob}, How are you?
import re

def optional_print(template):

    result = re.sub('{Bob}','', template)
    print(result)
    print(template)

optional_print('Hi {Bob} How are you?')

def optional_print2(template):
    x=template.replace("{Bob}", "")
    print(x)
    print(template)

optional_print2(("Hi {Bob} How are you?"))



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key,value in thisdict.items():
    print(key,value)


for num in range(1,100):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

#print(thisdict.values())

    #print(template.split(','))






# list1 = [12,23,45,67,89]
# list2 = [12,23,6,45,67,89]
#
# def missing_number(arg1, arg2):
#   difference = sum(list2) - sum(list1)
#   print(difference)
#
# missing_number(list1,list2)