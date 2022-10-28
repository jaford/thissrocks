#print dict keys values
# dict = {'apple':2.5, 'kiwi': 3}
#
# for item in dict:
#     print(dict[item])

# Replace ___ with your code

# # create an empty set
# numbers = set()
#
# # get integer input
# number = int(input())
#
# # add number to the numbers set
# numbers.add(number)
#
# # print numbers
# print(numbers)

#dicsard from set
# animals = {'tiger', 'cat', 'dog'}
# animals.discard('cat')
# print(animals)
#
# print('tiger' in animals)
#
# domestic_animals = {'dog', 'cat', 'elephant'}
# wild_animals = {'lion', 'tiger', 'elephant'}
#
# combined_set = domestic_animals | wild_animals
# print(combined_set)

# combined_set = domestic_animals & wild_animals
# print(combined_set)

# numbers = [10, 45, 61, -6]
#
# # assigning the first value to the largest variable
# # we will update the largest variable inside the loop
# largest = numbers[0]
#
# # loop iterates from 0 to last item of numbers
# for number in numbers:
#     if largest < number:
#         largest =  number
#
# print(f'largest: {largest}')
#
# #or
# numbers = [10, 45, 61, -6]
#
# # get the largest number
# largest = max(numbers)
#
# print(f'largest: {largest}')


frontend_developers = ['Rob', 'Jane', 'Mary', 'Anne']
backend_developers = ['Jane', 'Jack', 'Lily']

combined_developeres = set(frontend_developers) & set(backend_developers)
print(combined_developeres)