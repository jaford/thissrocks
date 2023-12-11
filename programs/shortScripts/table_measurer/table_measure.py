import time
import sys
from tabulate import tabulate


def delete_last_line(line_amount):
    for x in range(line_amount + 1):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

def calc_table_fixtures(a, b, c):

    calc1 = (a - b)
    solution_distance = calc1 / c
    solution_start_distance = solution_distance / 2
    
    result_table = [
        ['Parameter', 'Value'],
        ['Distance of each solution (x)', f'{solution_distance:.1f} inches'],
        ['Distance from the edge of the table to the first solution (x/2)', f'{solution_start_distance:.1f} inches']
    ]

    return result_table

intro_text = '\n---- Table Fixture Calculator ----\n\n----How to use----\n'\
    'All of the units that are bellow are assumed in inches.\n'\
    'Here is the base equation to use if you want to follow along.\n'\
    '(a - b)/c = x\n'\
    'a = length of table\n'\
    'b = length of all solutions\n'\
    'c = the quanity of solutions on the fixture\n'\
    'Step 1: Enter the length on the fixture.\n'\
    'Step 2: Length of all solutions (Follow guide to see if you need to add spacing for things such as Apple Pencil, Watch Chargers, etc...\n'\
    'Step 3: The amount of the solutions on the fixture.\n'\
    'Step 4: Once all the information has been entered, view the results that populated..\n'\

print(intro_text)

a = None
b = None
c = None

while True:
    while True:
        table_length = input('\nEnter the length of the table: ')
        if table_length.lower() == 'q':
            print('You have quit the program!')
            quit()

        solution_length = input('\nEnter the length of all solutions: ')
        if solution_length.lower() == 'q':
            print('You have quit the program!')
            quit()

        solution_amount = input('\nEnter the amount of solutions: ')
        if solution_amount.lower() == 'q':
            print('You have quit the program!')
            quit()

        print(f'\n\nHere are the inputs entered:\nTable Length --> a = {table_length}\nTotal Length of all solutions --> b = {solution_length}\nTotal amonut of solutions --> c = {solution_amount}\n\n')
        try:
            if table_length.replace('.', '', 1).isdigit() and solution_length.replace('.', '', 1).isdigit() and solution_amount.isdigit():
                a = float(table_length)
                b = float(solution_length)
                c = int(solution_amount)
            else: 
                print(f'"{table_length}", "{solution_length}", and "{solution_amount}" is not a supported input. Leaving the program.\n')
                exit()

            result_table = calc_table_fixtures(a, b, c)
            print("\n---- Your Results ----\n")
            print(tabulate(result_table, tablefmt="fancy_grid"))
            print('\n-----Enter new values if needed. if not press Q to quit the program!-----')    
            break

        except ValueError as err:
            print(f'Here is your error ----> "{err}"\n')

