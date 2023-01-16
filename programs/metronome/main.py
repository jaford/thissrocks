'''
This is finally the workable version that prints line by line 
in seconds the quarter notes in BPM! A lot easier than I thought! 

Had to use "pip install colorlog"! For me "pip3 install colorlog" since I am on a 
newer version of python!

Used module "keyboard" pip3 install keyboard.

Important notes:
Must run in sudo to have keyboard module work!

Module List to install:
pip3 install keyboard
pip3 install colorlog
'''
import time
from termios import tcflush, TCIFLUSH
import datetime
import colorlog
import logging
import sys, signal
import keyboard

while True:
    print('\nWelcome to my simple metronome program!')
    print('Choose the ones bellow: \n"Quarter" \n"Eighth" \n"Sixteenth"\n')
    print('(To restart program press "CTRL + C" or "Q")\n')

    while True:
        try:
            user_bpm_input = None
            user_note_val = None
            quarter_sec = None
            eighth_sec = None
            sixteenth_sec = None

            tcflush(sys.stdin, TCIFLUSH)
            user_bpm_input = input('Enter BPM: ')
            if user_bpm_input == 'Q' or user_bpm_input == 'q':
                print('You have quit the program.\n')       
                exit()
            user_note_val = input('Pick a note value: ').lower()
            if user_note_val == 'Q' or user_note_val == 'q':
                print('You have quit the program.\n')       
                exit()
            while True:
                if user_note_val == 'quarter':
                    user_bpm = float(user_bpm_input)
                    sec_val = (60/user_bpm)
                    break
                elif user_note_val == 'eighth':
                    user_bpm = float(user_bpm_input)
                    sec_val = (30/user_bpm)
                    break
                elif user_note_val == 'sixteenth':
                    user_bpm = float(user_bpm_input)
                    sec_val = (15/user_bpm)
                    break
                else: 
                    print('Note value was not reconized: {}\n'.format(user_note_val))
                    break
            
            print('\nCurrent BPM and note value:\nBPM: {}\nNote Value: {}\n'.format(user_bpm_input, user_note_val))
            tstep = datetime.timedelta(seconds=sec_val)
            tnext = datetime.datetime.now() + tstep
            try:
                while True: 
                    tdiff = tnext - datetime.datetime.now()
                    time.sleep(tdiff.total_seconds())
                    tnext = tnext + tstep
                    if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
                        print('\nYou have restarted the Metronome\n')
                        break
                    print('Boop')

                    '''
                    This code could possible be used to make a time signiture and print on one line! 
                    for x in range(0,4):
                        tdiff = tnext - datetime.datetime.now()
                        time.sleep(tdiff.total_seconds())
                        tnext = tnext + tstep
                        if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
                            print('\nYou have restarted the Metronome\n')
                            break
                        y = 'Beep ' + 'Boop ' * x
                        print(y, end='\r')
                    '''
            except KeyboardInterrupt as key_err:
                print('\nKeyboard Interrupt Error: {}\nYou have restarted Metronome.'.format(key_err))    

        except Exception as err: 
            bpm_error = str(user_bpm_input)
            note_val_error = user_note_val
            colorlog.error('A error occured --> : {}\n'.format(err))
            colorlog.warning('\nYou have entered a non-supported format for BPM: {}'.format(user_bpm_input))
            colorlog.warning('\nYou have entered a non-supported format Note Value: {}'.format(note_val_error))
            pass
