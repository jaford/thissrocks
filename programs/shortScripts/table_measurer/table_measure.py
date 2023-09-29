import time
import sys

def delete_last_line(line_amount):
    for x in range(line_amount + 1):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')


def calc_table_fixtures(a, b, c):

    calc1 = (a - b)
    solution_distance = calc1 / c
    solution_start_distance = solution_distance / 2
    

    result = f'Here are your results\nThe distance between each solution --> {solution_distance} inches\nThe distance of the first solution from the edge of the table --> {solution_start_distance} inches'

    return result

while True:
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

    while True:
        table_length = input('\nEnter the length of the table: ')
        line_amount = len(table_length.splitlines())
        delete_last_line(line_amount)

        solution_length = input('\nEnter the length of all solutions: ')
        line_amount = len(solution_length.splitlines())
        delete_last_line(line_amount)

        solution_amount = input('\nEnter the amount of solutions: ')
        line_amount = len(solution_amount.splitlines())
        delete_last_line(line_amount)

        print(f'\n\nHere are the inputs entered:\nTable Length --> {table_length}\nTotal Length of all solutions --> {solution_length}\nTotal amonut of solutions --> {solution_amount}\n\n')
        try:
            if table_length.isdigit():
                a = int(table_length)
            if solution_length.isdigit():
                b = int(solution_length)
            if solution_amount.isdigit():
                c = int(solution_amount)
            else: 
                print(f'"{table_length}", "{solution_length}", and "{solution_amount}" is not a supported input. Leaving the program.\n')
                exit()

            results = calc_table_fixtures(a, b, c)
            print(results)
            print('\nRun the program again in order to create new fixture solutions!\n')
            exit()

        except ValueError as err:
            print(f'"{err}" <--- is your current error!\n')

