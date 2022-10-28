#You have two strings 'abcde' and 'abcdXe' write a function that would print the difference

def string_comparison (str1, str2):
    first_set = set(str1)
    second_set = set(str2)
    difference = first_set.symmetric_difference(second_set)
    print(difference)

    string_comparison('abcde', 'abcdXe')

    ## print(first_set.difference(second_set))
    # for i in str1:
    #     for j in str2:
    #         #if str1 != str2:
    #         print(f'The difference is {i},{j}')
    # if str1 != str2:
    #     print('True')

string_comparison('abcde','abcdXe')