#find the missing number

list_a = [1,2,3,4,5,7,8,9]
list_b = [1,2,3,4,5,6,7,8,9]

num = set(list_b) - set(list_a)
print('Your missing number is ',num)

#try list comprehension

string_a = 'Convert this string into a list'
new_list = string_a.split(' ')
print(list(new_list))




#Is there a way to do it with a for loop?
for num in list_a,list_b:
    if num not in list_b:
        print(num)