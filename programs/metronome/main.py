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

def metronome_help(info_list):
    """
    You have entered the help page for the Metronome App!\n
    To leave this page press "q" to return back to the metronome.\n
    Start by entering a BPM. Choose a note value bellow:\n"Quarter" \n"Eighth"\n"Sixteenth"    
    """ 
    return info_list

while True:
    print('\nWelcome to my simple metronome program!')
    print('Start by entering a BPM.\nChoose a note value bellow: \n"Quarter"\n"Eighth"\n"Sixteenth"\n')
    print('Enter the amount of beats in each measure. This can be any whole number!\n')
    print('To restart program press "CTRL + C" or "Q"')
    print('You can even type in "help" at anypoint to show instructions!')
    print('(May need to press "Q" multiple times in order for metronome while it is running!\n')

    while True:
        try:
            # Attempted to clear keyboard inputs by setting the variable to None. Did not work :(
            tcflush(sys.stdin, TCIFLUSH)
            user_bpm_input  = None
            user_note_val   = None
            user_time_sign  = None 
            beat_val        = None 
            time_sign_list  = [4, 8, 16]

            user_bpm_input = input('Enter BPM: ').lower()
            if user_bpm_input == 'q':
                print('You have quit the program.\n')       
                exit()
            if user_bpm_input == 'help':
                help(metronome_help)
                break

            user_note_val = input('Enter a note value: ').lower()
            if user_note_val == 'q':
                print('You have quit the program.\n')       
                exit()
            if user_note_val == 'help':
                help(metronome_help)
                break
                
            user_beat_num = input('Enter your how many beats per measure: ').lower()
            if user_beat_num == 'q':
                print('You have quit the program.\n')       
                exit()
            if user_beat_num == 'help':
                help(metronome_help)
                break
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
                    print('You have choosen a incorrect value: {}\nAlso it would surprise me if you got here tbh.'.format(beat_val))
                    break
            
            print('\nBPM: {}\nNote Value: {}\nYour time signature is {}/{}\n'.format(user_bpm_input, user_note_val, beat_num, beat_val))
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
