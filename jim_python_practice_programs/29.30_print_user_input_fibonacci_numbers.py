# Write a program that will list the Fibonacci sequence less than n
def fib_num_user():

    n = int(input('Enter a number: '))
    t1 = 1
    t2 = 1
    result = 0

    # loop as long as t1 is less than n
    while t1 < n:
        # print t1
        print(t1)

        # assign sum of t1 and t2 to result
        result = t1 + t2

        # assign t2 to t1
        t1 = t2

        # assign result to t2
        t2 = result

fib_num_user()