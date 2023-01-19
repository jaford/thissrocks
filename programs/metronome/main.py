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
pip3 install playsound
'''
import time
import datetime
import colorlog
import logging
import sys, signal
import keyboard
from termios import tcflush, TCIFLUSH
from playsound import playsound

while True:
    print('\nWelcome to my simple metronome program!')
    print('Choose the note value bellow: \n"Quarter" \n"Eighth" \n"Sixteenth"\n')
    print('Also enter the number of beats per measure! This can be any whole number!\n')
    print('To restart program press "CTRL + C" or "Q"')
    print('(You may need to press "Q" multiple times in order for metronome while it is running!\n')

    while True:
        try:
            # Attempted to clear keyboard inputs by setting the variable to None. Did not work :(
            user_bpm_input  = None
            user_note_val   = None
            user_time_sign  = None 
            beat_val        = None 
            time_sign_list  = [4, 8, 16]

            tcflush(sys.stdin, TCIFLUSH)
            user_bpm_input = input('Enter BPM: ')
            if user_bpm_input == 'Q' or user_bpm_input == 'q':
                print('You have quit the program.\n')       
                exit()
            user_note_val = input('Enter a note value: ').lower()
            if user_note_val == 'Q' or user_note_val == 'q':
                print('You have quit the program.\n')       
                exit()
            user_beat_num = input('Enter your how many beats per measure: ')
            if user_beat_num == 'Q' or user_beat_num == 'q':
                print('You have quit the program.\n')       
                exit()
            beat_num = int(user_beat_num)
            while True:
                if user_note_val == 'quarter':
                    user_bpm = float(user_bpm_input)
                    sec_val = (60/user_bpm)
                    beat_val = 4
                    break
                elif user_note_val == 'eighth':
                    user_bpm = float(user_bpm_input)
                    sec_val = (30/user_bpm)
                    beat_val = 8
                    break
                elif user_note_val == 'sixteenth':
                    user_bpm = float(user_bpm_input)
                    sec_val = (15/user_bpm)
                    beat_val = 16
                    break
                else: 
                    print('Note value was not reconized: {}\n'.format(user_note_val))
                    break     
            while beat_val in time_sign_list:
                if beat_val == 4:
                    break
                elif beat_val == 8:
                    break
                elif beat_val == 16:
                    break              
                else:   
                    print('You have choosen a incorrect value: {}'.format(beat_val))
                    break
            
            print('\nBPM: {}\nNote Value: {}\nYour time signature is {}/{}\n'.format(user_bpm_input, user_note_val, beat_num, beat_num))
            tstep = datetime.timedelta(seconds=sec_val)
            tnext = datetime.datetime.now() + tstep
            try:
                while True:
                    if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
                        print('\nYou have restarted the Metronome\nTo exit, enter "Q"\n')
                        break
                    for x in range(0,beat_num):
                        tdiff = tnext - datetime.datetime.now()
                        time.sleep(tdiff.total_seconds())
                        tnext = tnext + tstep
                        y = 'Beep ' + 'Boop ' * x
                        sys.stdout.write("\033[K") #Clear to the end of line
                        print(y, end='\r')
            except KeyboardInterrupt as key_err:
                print('\nKeyboard Interrupt Error: {}\nYou have restarted Metronome.\n'.format(key_err))    

        except Exception as err: 
            colorlog.error('A error occured --> : "{}"\n'.format(err))
            colorlog.warning('You have entered a non-supported format for BPM: {}\n'.format(user_bpm_input))
            colorlog.warning('You have entered a non-supported format Note Value: {}\n'.format(user_note_val))
            colorlog.warning('You have entered a non-supported format Beat Value: {}\n'.format(beat_val))
            pass
