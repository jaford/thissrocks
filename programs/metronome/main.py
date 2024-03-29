'''
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

sys.path.append('..')
from functions.metronomeCounter import metronomeCounter, metronomeValues, userInputs
from functions.metronomeInfo    import metronomeHelp, metronomeMath
from functions.deleteLastLine   import deleteLastLine

bpmInput    = None
NoteVal     = None
secVal      = None
beatVal     = None 
introText = '\n----♪ Welcome to my Metronome Program! ♪----\n'\
    '----How to use----\nStep 1: Start by entering a BPM. (This can be any positive value)\n'\
    'Step 2: Choose a note value bellow: \n"Quarter"   = Counts of 4ths\n"Eighth"    = Counts in'\
    ' 8ths\n"Sixteenth" = Counts in 16ths\n"Thirty-second" = Counts in 32nds\n'\
    'Step 3: Enter the amount of beats in each measure. (This can be any whole number)\n'\
    '\n----Extra Info----\nYou can even type in "help" at anypoint to show extra instructions!'\
    'To restart program press "CTRL + C" or "Q"\n'\
    'May need to press "Q" multiple times to quit \n'\
    'This is a current bug and it is being addressed! (01/21/2023)\n'\
    'To access some more info of the current entered fields, type in "!info" after entering all the values\n'  

while True:                              
    print(introText)
    userStart = input('Are you ready to start? (Y/N)\n').lower().strip()
    if userStart == 'y':
        if isinstance(userStart, str):
            lineAmount = len(userStart.splitlines())
            deleteLastLine(lineAmount)
            if isinstance(introText, str):
                lineAmount = len(introText.splitlines())
                deleteLastLine(lineAmount)
        while True:
            try:
                beatNum, noteVal, bpmInput, beatVal= userInputs()

                print('\nHere are your values!\nBPM: {}\nNote Value: {}\nTime signature: {}/{}'.format(bpmInput, noteVal, beatNum, beatVal))
                userStart = input('Are you ready to continue?(Y/N)\n').lower()
                if isinstance(userStart, str):
                    lineAmount = len(userStart.splitlines())
                    deleteLastLine(lineAmount + 3)
                if userStart == 'y':
                    secVal, beatVal = metronomeValues(noteVal, bpmInput)
                    tstep, tnext    = metronomeCounter(bpmInput, noteVal, beatNum, beatVal, secVal)
                elif userStart == '!info':
                    secVal, beatVal   = metronomeValues(noteVal, bpmInput)
                    metronomeMath(bpmInput, noteVal, secVal, beatNum, beatVal)
                elif userStart == 'n':
                    print('\n----You have quit the metronome!----\n')
                    exit()
                else:
                    print('\n----You have restarted the metronome!----\n')

            except Exception as err: 
                colorlog.error('\nA error occured --> : "{}"\n'.format(err))
                colorlog.warning('You have entered a non-supported format for BPM: {}\n'.format(bpmInput))
                colorlog.warning('You have entered a non-supported format Note Value: {}\n'.format(noteVal))
                colorlog.warning('You have entered a non-supported format Beat Value: {}\n'.format(beatNum))
                pass
    elif userStart == 'n':
        print('\nYou have quit the program\n')
        exit()
    else: 
        colorlog.error('\nA error occured --> : "{}" is a non supported input.\n'.format(userStart))
        break

