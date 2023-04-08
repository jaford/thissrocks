import logging


print('Enter a animal')
x = input('HINT: (Enter "cat"): ')

if x == 'cat':
    print('There is a cat!')
else:
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('There has been a error from the input. Value of x = "{}"'.format(x))