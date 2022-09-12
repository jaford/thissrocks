"""
Took a course yesterday and had a section on how to make a 
string calculator, wanting to add this to our own repo by making sure I can 
make my own with my own resources as well as seeing how the pair programming 
made me think about code in a group setting!

All this code was a walk through on a stackoverflow page! 
"""
from sre_parse import DIGITS
import operator
from webbrowser import get


DIGITS = set('0123456789')
OPERATIONS = {
    '+' : operator.add,
    '-' : operator.add,
    '*' : operator.add,
    '/' : operator.add,
    '^' : operator.add,
}

def is_digit(var):
    return var in DIGITS

def get_number(varstr):
    s = ''
    for c in varstr:
        if not is_digit(c):
            break
        s += c
    return (int(s), len(s)) 


def perform_operation(string, num1, num2):
    op = OPERATIONS.get(string, None)
    if op is not None:
        return op(num1, num2)
    else:
        return None 

def eval_math_expr(expr):
    negate = False
    while True:
        try:
            if expr[0] == '-': # This is for negative numbers
                negate = True
                expr = expr[1]
            number1, end_number1 = get_number(expr)
            expr = expr[end_number1:]
            if negate == True:
                number1 = -number1
                negate = False 
            if expr == '':
                return number1
            op = expr[0]
            expr = expr[1:]
            number2, end_number2 = get_number(expr)
            result = perform_operation(op, number1, number2)
            number1 = result
            expr = str(number1) + expr[end_number2:]
        except Exception as error:
            print(error)
            break
        return number1
