# celsius to fahrenheit converter
#prompt user
#print out fahrenheit

# user_input=input('What celcius temperatue would you like to convert?')
# temp1= float(user_input)
# celsius = (9*temp1/5) + 32
# print(f'That equals {celsius} degrees fahrenheit')

#john jacob jingleheimer schmidt

# name = input('What is your name?')
# print(f'Hello {name}')
# print(f'Your name in uppercase is {name.upper()}')
# print(f'Your name in lowercase is {name.lower()}')
# print(f"Your name has {name.count('j')} js in it")
# print(f'Your name has {len(name)} characters long')
# print(f"The name 'jacob' starts at index location {name.find('jacob')}")

# prompt user for
#     place
#     somehthing to eat
#     a verb
#     another verb
#     a number
#     something else to eat
# place = input('Where would you like to go?')
# food = input('What is your favorite food?')
# first_verb = input('What is a verb in past tense?')
# second_verb= input('What is another verb in past tense?')
# number = input('What is your favorite number?')
# #number = str(number)
# other_food = input('What is your another favorite food?')
# print(f'There once was a person from {place} who liked to eat {food} '
#       f'He/she {first_verb} all day and {second_verb} all night and then'
#       f'ate {number} huge pieces of {other_food}')
#
# num_of_pizza = int(input('How many pizzas did you eat?'))
#
# if num_of_pizza > 4:
#     print('Wow, thats a lot of pizza')

### Int Check
# user_input = (input('Enter in something!: '))
#
# print('-----Bellow checks to see if the user input is a int, float, or string!-----')
# val_input = user_input
# try:
#     val_input = int(user_input)
#     print(f'"{user_input}" is an int!')
# except Exception as exception1:
#     try:
#         val_input = float(user_input)
#         print(f'"{user_input}" is a float!')
#     except Exception as eception2:
#         pass
# print(f'"{user_input}" is a string!')

# int_type = 5
# float_type = 5.0
# string_type = 'string'
#
# print(f"This is an int '{int_type}', this is a float '{float_type}', this is a string '{string_type}'")
#
# print(type(int_type))
# print(type(float_type))
# print(type(string_type))

# user_input = (input('Enter in something!: '))
#
# print('-----Bellow checks to see if the user input is a int, float, or string!-----')
# if user_input.isdigit():
#     int_val = int(user_input)
#     print(type(int_val))
#     print(f'"{user_input}" is an int!')
# elif (user_input.find('.') != -1):
#     float_val = float(user_input)
#     print(type(float_val))
#     print(f'"{user_input}" is an float!')
# else:
#     print(type(user_input))
#     print(f'"{user_input}" is a string!')



# user_input=input('What celcius temperatue would you like to convert?')
# temp1= float(user_input)
# celsius = (9*temp1/5) + 32
# print(f'That equals {celsius} degrees fahrenheit')

# try:
#     user_input.isdigit():
#     int_val = int(user_input)
#     celsius = (9 * int_val / 5) + 32
#     print(f'That equals {celsius} degrees fahrenheit')
# break
# if user_input.lower() == 'q':
#     print('goodbye')

#
# print('----To exit out of program, type "q" and hit enter to leave----')
# while True:
#     cel = input('What is the Temp in Celsius?: ')
#     if cel == 'q'or 'Q':
#         break
#     try:
#         cel_num = float(cel)
#     except Exception as error:
#         print('An error occured')
#         pass
#     fahr_calc = ((9 * cel_num) / 5) + 32
#     print(f'Here is the Temp in Fahrenheit is: {fahr_calc}')

# celsius to fahrenheit converter
#prompt user
#print out fahrenheit


# print('----Welcome!----')
# print('----To exit out of program, type "q" and hit enter to leave----')
#
# while True:
#     cel = input('What is the Temp in Celsius?: ')
#     if cel == 'q' or 'Q':
#         break
#     try:
#         cel_num = float(cel)
#     except Exception as error:
#         print('----UH OH----')
#         print('This is your error:', error)
#         print('----Please enter a number!----')
#         pass
#     fahr_calc = ((9*cel_num)/5) + 32
#     print(f'Here is the Temp in Fahrenheit is: {fahr_calc}'+'\N{DEGREE SIGN}')
#
# fruits = ['apple','cherry','orange','kiwi', 'banana', 'pear', 'fig']
#
# print("Original List:",fruits)
# fruits.append('lemon')
# fruits.append('lime')
# fruits.pop(3)
# print("New list:",fruits)
#
#
#
# sandwiches = ['Pb&J','Tomato and Cheese','leftover',
#               'grilled cheese','pimento','ham and cheese',
#               'steak','pesto and onion',
#               'PB and honey']
# print(sandwiches[::-1])
# print('Original List', sandwiches)
# print('Entire list but last item:',sandwiches[1:8])
# sandwiches.reverse()
# print('Entire list reversed:', sandwiches)
# sandwiches.reverse()
# print('The second item is: ', sandwiches[1],'.' '  The third item is: ',sandwiches[2], 'and finally, '
#                                                                                        'the fifth item is: '
#                                                                                        '',sandwiches[4])
# print('Print two items skipping every other item',sandwiches[1::2])
# print("Printing every other item start with item at location '0' ",sandwiches[0:9:2])
#
# i = []
# for i in range(1,20):
#     print(i)
#
# j = [i for i in range(1,20)]
# print(j)
#
# cars = 'accord','odyssey','civic','corvette'
# colors = 'red','blue','green','clear'
#
# for car,color in combos:
#     print(f'{car},{color}')

# for car in cars:
#     for color in colors:
#         combo = (str(car), str(color))
#         print(type(combo))
#         print(combo)
# #combos = [(car, color) for car in cars for color in colors]
#
# ty = open('/Users/jim/Downloads/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/alice.txt')
# for line in ty:
#     print(line)
#
# jimsfile = open('/Users/jim/Desktop/python_zen.txt')
# for line in jimsfile:
#      print(line)
#
# new_file = open("new_text.txt", "a")
# write_current_file = new_file.write("""Here is a line
# Here is another line.
# Here is the last line""")
# new_file.close()
#
# new_file = open("new_text.txt", "r")
# print(new_file.read())
# total = 32
# for i in range(total):
#     print('2 rasied to the power of', i, 'is', 2**i)
#
# for i in range(0,33):
#     print(2**i)
#
# counter = 0
# while counter < 33:
#     print(counter**2)
#     counter = counter+1 < - - -Wrong

# ctemps = [-40.0, 0.0, 37.0, 75.0, 100.0]
# for ctemp in ctemps:
#     #print(ctemp)
#     f = ((9*ctemp))/5 +32
#     print(f'Celsius temp is',ctemp,'fahrenheit temp is ',f)

# fruits =[
#     '     MANGO', 'Apple', '    peach   ', '  Apricot',
#     'BaNaNa', 'Persimmon   '
# ]
# lower_fruits = [f.lower() for f in fruits]
# stripped_fruits = [f.strip() for f in lower_fruits]
# clean_fruits=[f.strip().lower() for f in fruits]
#
# # print(lower_fruits)
# # print(stripped_fruits)
# print(clean_fruits)

# file_name = '/Users/jim/Downloads/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/tyger.txt'
# with open(file_name) as file_in:
#      for i, line in enumerate(file_in, 1):
#         print("{:4d}: {}".format(i, line), end='')
# print('-' * 60)


# file_name = open('/Users/jim/Downloads/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/alice.txt')
#
# Alice_counter = 0
#
# with file_name as file_in:
#     for word in file_in:
#         if 'Alice' in word:
#             Alice_counter += 1
#         else:
#             pass
#     print(f'Alice is used {Alice_counter} times')
#
# file_name = open('/Users/jim/Downloads/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/alice.txt')
# file_read = file_name.read()
# i = file_read.count('Alice')
#
# print(f'{i}: is how many times Alice was used!')


# from pprint import pprint
#
# test_scores = {}
#
# with open('/Users/jim/Downloads/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/testscores.dat') as data_in:
#     for line in data_in:
#         # name, score = line.rstrip('\n\r').split(':')
#         name, score = line.split(':')
#         score = int(score)
#         test_scores[name] = score
# pprint(test_scores) # < - - PRINTS DICT
# print()
#
# for name,score in test_scores.items():
#     print(name,score)
# print()

# from pprint import pprint
#
# test_score_info = {}
#
# with open('/Volumes/Workspace/CEDocs/python_class/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/testscores.dat') as score_in:
#     for line in score_in:
#         name, score = line.rstrip('\n\r').split(':')
#         score = int(score)
#         test_score_info[name] = score
# pprint(test_score_info)
# print()
#
# for name, score in test_score_info.items():
#     print(name, score)

# fruit_1 =set()
#
# with open('/Users/jim/Downloads/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/fruit1.txt') as fruit1:
#     for fruit in fruit1:
#         var1 = fruit.strip().lower()
#         fruit_1.add(var1)
#         #print(var1)
#
# fruit_2 = set()
# with open('/Users/jim/Downloads/TTPS4803-APL3_GSPython_FL-Dell-Apple_StudentMaterials_20220727/py3intro3day/DATA/fruit2.txt') as fruit2:
#     for fruit in fruit2:
#         var2 = fruit.strip().lower()
#         fruit_2.add(var2)
#         #print(var2)
#
# print('-'*60)
# combined_fruits = fruit_1 & fruit_2
# print(combined_fruits)


#
# def c2f(num):
#     print((9*num)/5 +32)
#
# c2f(100)
# c2f(0)
# c2f(37)
# c2f(40)

# fruits = ['apple','cherry',
#         'lemon','orange',
#           'lime','kiwi','banana',
#           'pear','fig']
#
# for fruit in fruits:
#     upper_fruits= fruit.title()
#     print(f'List with upper case: {upper_fruits}')
#     print('-' *60)
# for item in upper_fruits
#print(f"List without 'Orange:' {upper_fruits}") < - - - - - how to get rid of orange?


try:
    print(x)
except:
    print('Something bad happened')