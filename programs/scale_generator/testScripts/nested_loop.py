
while True:
    # Use a break catch that is set to false and once true it can help you break out of a nested loop! 
    breakFlag = False
    while True:
        while True:
            userInput = input('Pick a number: ')
            if userInput == '1':
                print('You are here 1\n')
                breakFlag = True
                break
            elif userInput == '2':
                print('You are here 2\n')     
                breakFlag = True
                break
            elif userInput == '3':
                print('You are here 3\n')
                breakFlag = True
                break 
            else: 
                print('Using "{}" is not reconizable'.format(userInput))
                break
        if breakFlag:
            break
    breakFlag = False
    while True:
        while True:
            userStringInput = input('Enter Yes or No (Y/N): ').lower()
            if userStringInput == 'y':
                print('You are here 1\n')
                breakFlag = True
                break
            elif userStringInput == 'n':
                print('You are here 2\n')     
                breakFlag = True
                break
            else: 
                print('Using "{}" is not reconizable'.format(userStringInput))
                break
        if breakFlag:
            break

