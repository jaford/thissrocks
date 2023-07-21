
# Enter a string that starts with a $ for this example
# userInput = input('Enter random characters that check how many numbers and symbols there are! ---> ')
# Test strings
# $samh51jcj
# $143718ash
userInput = '$143718ash'

for i in userInput:
    print('CHECK 1')
    print(i)
    if i[0] == "$":
        for v in range(1, len(userInput)):
            print('CHECK 2')
            print(userInput[v])
            if userInput[1].isdigit:
                print('CHECK 3')
                print(userInput[v])
                print(userInput(1:))


        if not userInput[1].isdigit:
            print('skippings') 
# for i in userInput:
#     if i[0] == '$': 
#         for char in i(): 
#             if char.isdigit():
#                 print(char)
#         if not i[1].isdigit():
#             print('Skipping')