'''
This is finally the workable version that prints line by line 
in seconds the quarter notes in BPM! A lot easier than I thought! 

Task --> Make text error a red color to stand out!

Had to use "pip install colorlog"! For me "pip3 install colorlog" since I am on a 
newer version of python!

Used module "keyboard" pip3 install keyboard.
Must run in sudo! 
'''

import time
import datetime
import colorlog
import logging
import sys, signal
import keyboard

while True:
    quarter_sec = None
    eighth_sec = None
    print('Welcome to my simple metronome program!')
    print('Choose either a "Quarter" or "Eighth" note value')
    print('(To restart program press "CTRL + C" or "Q")\n')

    while True:
        try:
            user_bpm_input = input('Enter BPM: ')
            user_note_val = input('Pick a note value: ').lower()
            while True:
                if user_note_val == 'quarter':
                    user_bpm = float(user_bpm_input)
                    sec_val = (60/user_bpm)
                    break
                elif user_note_val == 'eighth':
                    user_bpm = float(user_bpm_input)
                    sec_val = 0.5 * (60/user_bpm)
                    break
                elif user_note_val.capitalize().startswith('Q'):
                    print('You have quit the program!')       
                    break
                else: 
                    print('Note value was not reconized: {}\n'.format(user_note_val))
                    break

            tstep = datetime.timedelta(seconds=sec_val)
            tnext = datetime.datetime.now() + tstep
            try:
                while True: 
                    tdiff = tnext - datetime.datetime.now()
                    time.sleep(tdiff.total_seconds())
                    tnext = tnext + tstep
                    print('Boop')
                    if keyboard.is_pressed('Q'):
                        print('You have restarted the Metronome\n')
                        break
            except KeyboardInterrupt as key_err:
                print('Keyboard Interrupt Error: {}'.format(key_err))    

        except Exception as err: 
            user_input_error = str(user_bpm_input)
            colorlog.warning('You have entered a non-supported format: {}'.format(user_bpm_input))
            colorlog.error('A error occured --> : {}\n'.format(err))
            pass
