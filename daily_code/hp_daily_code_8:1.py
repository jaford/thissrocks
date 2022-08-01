"""
Here I want to loop and count through a list! 
Lets hope this works and makes sense! 

The code bellow is able to list out the contents of a list using a loop.
"""

print('-----------Practice 1-----------')

list_1 = ['Apple', 'Cherry', 'Banana']
for x in list_1:
    print(x)

"""
Here I will use a while loop to print out the contents of this
list as well as use a len to list out the length of the list!

NOTE THE i = i + 1. This tells (I think lol) the list to stop
printing once it has counted all that is in the list! 
"""

print('-----------Practice 2-----------')
list_2 = ['Apple', 'Cherry', 'Banana', 'Mellon', 'Mango', 'Blueberry']
i = 0 
while i < len(list_2):
    print(list_2[i])
    i = i + 1
print('-----------Length of list_2!-----------')
print(len(list_2))


"""
My attempt at list comprension using the same list in list 2! 
"""
print('-----------Practice 3-----------')

list_3 = ['Apple', 'Cherry', 'Mango', 'Blueberry']
[print(x) for x in list_3]
