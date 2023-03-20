# Check the first and last number of a list is the same
# Return true if, TRUE and false if false. 


def list_check(numberlist):
    print('Given list: ', numberlist)

    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False

list_1 = [10, 20, 30, 40, 50]
print('result is: ',list_check(list_1))

list_2 = [50, 24, 35, 45, 50]
print('result is: ',list_check(list_2))

