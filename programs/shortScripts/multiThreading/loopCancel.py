import datetime 
import threading
import sched, time

def printLines():
    x = int(input('Enter how many seconds: '))
    secInterval = datetime.timedelta(seconds=x)
    for i in range(0,x):
        print('You are printing a new line every {} times.'.format(x))
    return

def printTimer():
    userInput = float(input('Enter a number to represent seconds: '))
    t = threading.Timer(2, printTimer)
    t.daemon = True 
    t.start()
    print('Hello!')

def printit():
    threading.Timer(5.0, printit).start()
    print("Hello, World!")

def doSomething(scheduler):
    scheduler.enter(2, 1, doSomething, (scheduler,))
    print("Doing stuff...")

def timeSleep(userInput):
    sec = int(userInput)
    print('Waiting for {} amount of seconds. Please wait...'.format(sec))
    time.sleep(sec)
    print('Sleep has ended...')

userInput = input('Enter a number in seconds: ')
timeSleep(userInput)
'''
These are function calls that I attemtped to make work above for printing a new line every x amounf of seconds. 
# printTimer()
# printit()
userInput = int(input('Enter user amount of seconds: '))
myScheduler = sched.scheduler(time.time, time.sleep)
myScheduler.enter(userInput, 1, doSomething, (myScheduler,))
myScheduler.run(userInput)
'''


