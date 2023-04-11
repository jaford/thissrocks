# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import os 

def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))
    print("Cube task assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running cube task: {}\n".format(os.getpid()))
 
def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))
    print("Square task assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running cube square: {}\n".format(os.getpid()))


print("ID of process running main program: {}".format(os.getpid()))

valCube = int(input('Put down a int that you can cube: '))
valSquare = int(input('Put down a int that you can Square: '))
# creating thread
t1 = threading.Thread(target=print_square, args=(valCube,))
t2 = threading.Thread(target=print_cube, args=(valSquare,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
print("Done!\n")