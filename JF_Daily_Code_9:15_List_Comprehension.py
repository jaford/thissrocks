#list comprehension plractice and explination

#using a for loop
cities = ['Albuquerque', 'Cupertino', 'San Jose','Las Vegas','Carlisle']
filtered_list = []
for i in cities:
    if 'a' in i or 'A' in i:
        filtered_list.append(i)
print(filtered_list)

#using list comprehension
cities2 = ['Albuquerque', 'Cupertino', 'San Jose','Las Vegas','Carlisle']
filtered_list2 = [i for i in cities2 if 'a' in i or 'A' in i]
print(filtered_list2)

products = ['Mac', 'iPhone', 'iPad','iPod','AppleWatch']
filtered_list3 = []
for i in products:
    if 'a' in i or 'A' in i:
        filtered_list3.append(i)
print(filtered_list3)

filtered_list3 = [i for i in products if 'a' in i or 'A' in i]
print((filtered_list3))