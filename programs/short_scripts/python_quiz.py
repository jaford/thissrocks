# Print a characters from a string. 
# Only print the even number index.

user_string = input('Enter a string here: ' + '\n')
print('Here is your string: {}'.format(user_string))

length = len(user_string)
print(length)

for i in range(0, length - 1, 2):
    print('index {}'.format(user_string[i]))
    