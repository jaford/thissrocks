'''
This is finally the workable version that prints line by line

Important notes as of (15.02.2023):
Must run in sudo to have keyboard module work!
File for the click sound for metronome is the absolute path! #Must address in the future!
Current issues are that that I can not seem to import the sound module. So far it crashes and states that time delta is negative? Not to sure what in tarnation is happening. :(

Module List to install:
pip3 install keyboard
pip3 install colorlog
pip3 install playsound
'''
import time
import datetime
import colorlog
import logging
import os
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

    return sec_val, beat_val

def metronomeMath(user_bpm_input, user_note_val, sec_val, beat_num, beat_val):

    print('\n----Here are some cool math things that correlate with beat duration & conversions!----\n(This is for the current inputed items)\n')
    user_bpm = int(user_bpm_input)
    quarter_val = (60/user_bpm)
    eighth_val = (30/user_bpm)
    sixteenth_val = (15/user_bpm)
    thirty_second_val = (7.5/user_bpm)
    milisec = sec_val / 1000
    tstep = datetime.timedelta(seconds=sec_val)
    tstep.total_seconds()

    print('----Here is a list of the second duration for some note values----\nQuarter Note: {}\nEighth Note: {}\nSixteenth Note: {}\nThirty Second Note: {}\n'.format(quarter_val, eighth_val, sixteenth_val, thirty_second_val))
    print('----The second duration of your entered values ({} & {})----\nBeat length in seconds: {}\nBeat length in mili-seconds: {}\n'.format(user_note_val, beat_num, sec_val, milisec))
    print('----Here is the timeDelta numbers of your selected input----\nSeconds of each beat: {}\n'.format(tstep))
    print('----Here is the fancy music terms that your BPM is definded as!----\nTemp: {}\nTime Signiture: {}/{}'.format(user_bpm_input, beat_num, beat_val))
    if user_bpm < 24:
        print('Marking: Larghissimo\nMeaning: Extremely slow\n')
    elif 25 <= user_bpm <= 40:
        print('Marking: Grave\nMeaning: Very slow\n')
    elif 40 <= user_bpm <= 60:
        print('Marking: Largo\nMeaning: Slow\n')
    elif 60 <= user_bpm <= 66:
        print('Marking: Larghetto\nMeaning: Moderately slow\n')
    elif 66 <= user_bpm <= 76:
        print('Marking: Adagio\nMeaning: Slow and expressive\n')
    elif 76 <= user_bpm <= 108:
        print('Marking: Andante\nMeaning: At a walking pace\n')       
    elif 108 <= user_bpm <= 120:
        print('Marking: Moderato\nMeaning: At a moderate speed\n')
    elif 120 <= user_bpm <= 156:
        print('Marking: Allegro\nMeaning: Fast (or bright)\n')
    elif 156 <= user_bpm <= 176:
        print('Marking: Vivace\nMeaning: Fast (or lively)\n')
    elif 168 <= user_bpm <= 200:
        print('Marking: Presto\nMeaning: Very fast\n')
    else: 
        print('Marking: Prestissimo\nMeaning: Extremely fast\n')

    print('----The metronome has restarted----\n')
    return quarter_val, eighth_val, sixteenth_val, thirty_second_val, tstep

def metronomeCounter(user_bpm_input, user_note_val, beat_num, beat_val):
    print('\nBPM: {}\nNote Value: {}\nTime signature: {}/{}\n'.format(user_bpm_input, user_note_val, beat_num, beat_val))
    tstep = datetime.timedelta(seconds=sec_val)
    tnext = datetime.datetime.now() + tstep
    try:
        while True:
            if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
                print('\n----You have restarted the Metronome----\nTo exit, enter "Q"\n')    
                break
            for x in range(0,beat_num):
                # Leaving this here for future implacation! 
                # playsound('programs/metronome/metronomeSounds/metronome-85688.mp3')
                # playsound('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/metronome/metronomeSounds/metronome-85688.mp3')  
                tdiff = tnext - datetime.datetime.now()
                time.sleep(tdiff.total_seconds())
                tnext = tnext + tstep
                y = '\r' + 'Beep ' + 'Boop ' * x
                sys.stdout.write("\033[K") #Clear to the end of line
                print(y, end='\r')
    except KeyboardInterrupt as key_err:
        print('----You have restarted Metronome----\n'.format(key_err))
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
        'To access some more info of the current entered fields, type in "!info" after entering all the values\n'\

    print('\n----♪ Welcome to my Metronome Program! ♪----\n')
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
            time_sign_list  = [4, 8, 16, 32] # Probably get rid of this list since I do not really to access it. Maybe the other branch can over engineer it! 

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

            print('\nHere are your values!\nBPM: {}\nNote Value: {}\nNumber of beats per measure: {}'.format(user_bpm_input, user_note_val, user_beat_num))
            user_start = input('Are you ready to continue?(Y/N)\n').lower()
            if user_start == 'y':
                sec_val, beat_val   = metronomeValues(user_note_val)
                tstep, tnext        = metronomeCounter(user_bpm_input, user_note_val, beat_num, beat_val)
            elif user_start == '!info':
                sec_val, beat_val   = metronomeValues(user_note_val)
                metronomeMath(user_bpm_input, user_note_val, sec_val, beat_num, beat_val)
            elif user_start == 'n':
                print('\n----You have quit the metronome!----\n')
                exit()
            else:
                print('\n----You have restarted the metronome!----\n')

        except Exception as err: 
            colorlog.error('\nA error occured --> : "{}"\n'.format(err))
            colorlog.warning('You have entered a non-supported format for BPM: {}\n'.format(user_bpm_input))
            colorlog.warning('You have entered a non-supported format Note Value: {}\n'.format(user_note_val))
            colorlog.warning('You have entered a non-supported format Beat Value: {}\n'.format(beat_val))
            pass
