# Write a program that will list the Fibonacci sequence
def fib_num():
    n = int(input('Enter a number: '))
    t1 = 1
    t2 = 1
    result = 0

    # loop from 1 to n
    for i in range(1, n + 1):
        # print t1
        print(t1)

        # assign the sum of t1 and t2 to result
        result = t1 + t2

        # assign t2 to t1
        t1 = t2

        # assign result to t2
        t2 = result

fib_num()