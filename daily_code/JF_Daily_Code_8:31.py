# def addition(a, b):
#     result = a + b
#     print(result)
#
#
# addition(5, 5)
#
#
# def addition2(*args):
#     result = 0
#     # Iterating over the Python args tuple
#     for x in args:
#         result += x
#     return result
#
#
# (addition2(3, 3, 3))
#
#
# def addition3(*args):
#     result = 0
#     # Iterating over the Python args tuple
#     for x in args:
#         result += x
#
#         print(type(result))
#     convert = str(result)
#     print(type(convert))
#     stripped = convert.strip('\n')
#
#     return stripped
#

def addition4(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    #print(result)
    if result < 0:
        print('This is a negative number! :)')


(addition4(-6, 5))