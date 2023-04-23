def stringResult(result):
    if isinstance(result, int):
        body = 'Test string reslut output: {}'.format(result)
        print(body)

def addition(x, y):
    result = x + y 

    return result

def subtraction(x, y):
    result = x - y 

    return result

x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))

result = addition(x, y)
stringResult(result)

result = subtraction(x, y)
stringResult(result)
