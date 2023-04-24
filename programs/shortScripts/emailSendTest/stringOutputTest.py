def stringResult(restultDict):
    if isinstance(restultDict, dict):
        print('\nHere is the results of your calculations bellow:\n')
        for i, v in restultDict.items():
            print(i + '\t', v)

    body ='\nHere is a example on how to display data onto a string. Here is test to put into this string.\nThis is one way I can fomat data into a email so I can send it to user & myself!\n'
    print(body)
    
    return

def math(x, y):
    resultAdd = x + y 
    resultSub = x - y 
    resultMulti = x * y 
    resultDiv = x / y 

    return resultAdd, resultSub, resultMulti, resultDiv


x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))
resultAdd, resultSub, resultMulti, resultDiv = math(x, y)

restultList = []
restultDict = {}
restultDict['Addition']         = resultAdd
restultDict['Subtraction']      = resultSub
restultDict['Multiplcation']    = resultMulti
restultDict['Division']         = resultDiv

print(restultList)
print(type(restultList))

print(restultDict)
print(type(restultDict))


stringResult(restultDict)