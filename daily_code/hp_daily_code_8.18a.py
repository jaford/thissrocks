"""
Found online some guides for short hand ways to write If ... Else statements! 

The technique is known as Ternary Operators, or Conditional Expressions
"""
print('----Practice 1----')
a = 10 
b = 15 
print('A') if a > b else print('B')

print('----Practice 2----')
a = float(input('Enter your first number: ')) 
b = float(input('Enter your second number: '))

# Yes, this is all one line LOL
print('"{}" is greater than "{}"'.format(a, b)) if a > b else print('{} and {} are equal'.format(a, b)) if a == b else print('"{}" is greater than "{}"'.format(b, a))

print('----Practice 3----')
a = 300 
b = 200 
c = 1000
if a > b and c > a:
    print('both conditions are true.')

print('----Practice 4----')
a = 300 
b = 200 
c = 1000
if a > b or c > a:
    print('both conditions are true.')
