#Practicing data type conversion
#
print('----------This is a dictionary----------')
dict1 = {'MA':'BOS', 'NJ':'EWR','CA':'SFO','GA':'ATL'}
print(type(dict1))
print(dict1)

print('----------Printing just the keys----------')
for key in dict1.keys():
    print(key)

print('----------Printing just the values----------')
for value in dict1.values():
    print(value)

print('----------Converting dict{} into a list[] using list and .items()----------')
list_dict = list(dict1.items())
print(type(list_dict))
print(list_dict)


print('----------Converting dict{} into a str using using str()----------')
dict_str = str(dict1)
print(type(dict_str))
print(dict_str)

print('----------Converting list[] into back into a dict using dict()----------')
dict2 = list_dict
print(type(dict2))
print(dict2)
new_dict = dict(dict2)
print(type(new_dict))
print(new_dict)