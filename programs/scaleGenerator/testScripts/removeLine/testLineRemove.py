import time
import sys

def deleteLastLine2(lineAmount):
    for x in range(lineAmount):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

def deleteLastLine1():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

x = 'EXAMPLE'
print(x)
lineAmount = len(x.splitlines())
print('This is how many lines you have: {}'.format(lineAmount))

y = 'EXAMPLE 2'
print(y)
lineAmount = len(y.splitlines())
print('This is how many lines you have: {}'.format(lineAmount))

z = 'EXAMPLE 3\nANOTHER LINE\n\n'
print(z)
lineAmount = len(z.splitlines()) + 1
print('This is how many lines you have: {}'.format(lineAmount))

# deleteLastLine1()
deleteLastLine2(lineAmount)