"""
if/else statements!
"""

print('Practice 1')
a = True

if a:
    print('It is true!')
    print('Also print this')
else:
    print('This is false!')
print('Always print this')

print('Practice 2')
#Change the boolenans here to see what prints! 
a = True
b = True
c = True
if a:
    print('It is true!')
    print('Also print this')
    if b:
        print('Both are true!')
        if c:
            print('All three are true!')
else:
    print('This is false!')
print('Always print this')

"""
We can use loops to make the code above more readable!
"""
#For loop Example!
print('Practice 3')
a = [1,2,3,4,5]
for item in a:
    print(item) 

#While loop Example!
print('Practice 4')
a = 0 
while a < 5:
    print(a)
    a = a + 1

