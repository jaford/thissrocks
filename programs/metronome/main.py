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

def metronomeHelp(info_txt):
    """
    \n----Welcome to the help page----\n\
Step 1: Start by entering a BPM. (This can be any positive value)\n
Step 2: Choose a note value bellow: \n"Quarter"   = Counts of 4ths\n"Eighth"    = Counts in 8ths\n"Sixteenth" = Counts in 16ths\n"Thirty-second" = Counts in 32nds\n
Step 3: Enter the amount of beats in each measure.\n(This can be any whole number)\n
    \n----Current Known Bugs (as of 1/23/2023)----\n\
While metronome is running, you can press "Q" or "q" to restart the metronome but it does not always reconize the input.\n
The current fix is to use "CTRL + C" to break the loop.\n
Using this help method is not really a good idea for a more info page. Just thought it was a cool idea.
    """
    return info_txt

def metronomeValues(user_note_val):
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
        elif user_note_val == 'thirty-second' or user_note_val == 'thirty second':
            user_bpm = float(user_bpm_input)
            sec_val = (7.5/user_bpm)
            beat_val = 32
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
            elif beat_val == 32:
                break        
            else:   
                print('You have choosen a incorrect value: {}\nAlso it would surprise me if you got here tbh.'.format(beat_val))
                break
    return sec_val, beat_val

def metronomeCounter(user_bpm_input, user_note_val, beat_num, beat_val):
    print('\nBPM: {}\nNote Value: {}\nYour time signature is {}/{}\n'.format(user_bpm_input, user_note_val, beat_num, beat_val))
    tstep = datetime.timedelta(seconds=sec_val)
    tnext = datetime.datetime.now() + tstep
    try:
        while True:
            if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
                print('\n----You have restarted the Metronome----\nTo exit, enter "Q"\n')    
                break
            for x in range(0,beat_num):
                tdiff = tnext - datetime.datetime.now()
                time.sleep(tdiff.total_seconds())
                tnext = tnext + tstep
                y = '\r' + 'Beep ' + 'Boop ' * x
                sys.stdout.write("\033[K") #Clear to the end of line
                print(y, end='\r')
    except KeyboardInterrupt as key_err:
        print('\nKeyboard Interrupt Error: {}\n----You have restarted Metronome----\n'.format(key_err))
    return tstep, tnext

while True:
    intro_text = '----How to use----\nStep 1: Start by entering a BPM. (This can be any positive value)\n'\
        'Step 2: Choose a note value bellow: \n"Quarter"   = Counts of 4ths\n"Eighth"    = Counts in'\
        ' 8ths\n"Sixteenth" = Counts in 16ths\n"Thirty-second" = Counts in 32nds\n'\
        'Step 3: Enter the amount of beats in each measure. (This can be any whole number)\n'\
        '\n----Extra Info----\nYou can even type in "help" at anypoint to show extra instructions!'\
        'To restart program press "CTRL + C" or "Q"\n'\
        'May need to press "Q" multiple times to quit \n'\
        'This is a current bug and it is being addressed! (01/21/2023)\n'\

    print(u'\n---- Welcome to my Metronome Program! ----\n')
    print(intro_text)
    while True:
        try:
            # Attempted to clear keyboard inputs by setting the variable to None. Did not work :(
            tcflush(sys.stdin, TCIFLUSH)
            user_bpm_input  = None
            user_note_val   = None
            user_time_sign  = None 
            sec_val         = None
            beat_val        = None 
            time_sign_list  = [4, 8, 16, 32]

            user_bpm_input = input('Enter BPM: ').lower()
            if user_bpm_input == 'q':
                print('You have quit the program.\n')       
                exit()
            if user_bpm_input == 'help':
                help(metronomeHelp)
                break

            user_note_val = input('Enter a note value: ').lower()
            if user_note_val == 'q':
                print('You have quit the program.\n')       
                exit()
            if user_note_val == 'help':
                help(metronomeHelp)
                break
                
            user_beat_num = input('Enter your how many beats per measure: ').lower()
            if user_beat_num == 'q':
                print('You have quit the program.\n')       
                exit()
            if user_beat_num == 'help':
                help(metronomeHelp)
                break
            beat_num = int(user_beat_num)

            sec_val, beat_val   = metronomeValues(user_note_val)
            tstep, tnext        = metronomeCounter(user_bpm_input, user_note_val, beat_num, beat_val)
   
        except Exception as err: 
            colorlog.error('\nA error occured --> : "{}"\n'.format(err))
            colorlog.warning('You have entered a non-supported format for BPM: {}\n'.format(user_bpm_input))
            colorlog.warning('You have entered a non-supported format Note Value: {}\n'.format(user_note_val))
            colorlog.warning('You have entered a non-supported format Beat Value: {}\n'.format(beat_val))
            pass
