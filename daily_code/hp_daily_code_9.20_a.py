"""
Lets see how I can extract items from a dictionary and list 

Also combining two lists as well! 
"""

print('----Practice 1----\n')

keys = ['Ten', 'Twenty', 'Thirty',]
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

print('----Practice 2----\n')
# Merging two dictionaries

dict_1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict_2 = {'Fourty': 40, 'Fifty':50, 'Sixty': 60}

dict_3 = {**dict_1, **dict_2}
print(dict_3)

