
def stringResult(restultDict):
    if isinstance(restultDict, dict):
        print('\nHere is the results of your calculations bellow:\n')

        keyList = list(restultDict.keys())
        valueList = list(restultDict.values())
        emptyList = []
        for i, v in restultDict.items():
            emptyList.append((i, v))
            # print(i + '\t', v)
        print(emptyList)

    mailSigniture = '\nKindly,\nHunter Pimparatana.\nEmail: hunterpimparatana@gmail.com\nMobile: (505)-918-4031'
    body ='\nHere is a example on how to display data onto a string. Here is test to put into this string.\nThis is one way I can fomat data into a email so I can send it to user & myself!\nCompiled data:\t{}\n{}\n'.format(emptyList, mailSigniture)
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

restultDict = {}
restultDict['Addition']         = str(resultAdd)
restultDict['Subtraction']      = str(resultSub)
restultDict['Multiplcation']    = str(resultMulti)
restultDict['Division']         = str(resultDiv)

stringResult(restultDict)