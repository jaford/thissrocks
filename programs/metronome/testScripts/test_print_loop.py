'''
Wrote a short loading script to show how to delete a line in terminal to simulate a loading sequance!
'''
import time
import sys
import keyboard

while True:
    for x in range(0,5):
        if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
            print('\nYou have restarted the Metronome\n')
            break
        y = 'loading' + '.' * x
        print(y, end='\r')
        sys.stdout.write("\033[K") #Clear to the end of line
        time.sleep(1)

    

