import datetime

# Hard coded in
# This will be yyyy/mm/dd format. 
d1 = datetime.datetime(2018, 5, 3)
d2 = datetime.datetime(2022, 10, 3)

# Comparing the dates will return either True or False
x = d1 > d2
y = d1 != d2
z = d1 < d2
print('d1 is greater than d2: ', x)
print('d1 is equal to d2: ', y)
print('d1 is less than d2: \n', z)
