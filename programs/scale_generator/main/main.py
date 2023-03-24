'''
The creation of looping through the notes was done by Kai! I changed a section where you can have it diveded by groups of 5 and 7 note scales. 
I have only included a handful of scales for the sake of simplifying. Possibly add more in the future. 
'''
import sys, signal
import os
import colorlog
import json
from termios import tcflush, TCIFLUSH

# This worked in my test script but for some reason it does not here? Using the same syntax and calling the function is the same regaurdless? 
# Might need to ask for hekp on this. This may be a VsCode thing? I am not to sure.
'''
Error that I get on the line above in VSCode. It still runs somehow even with the error? May need to ask someone for help!
Unable to import 'functions.parseData'pylint(import-error)
(New note as of 03.21)
Based upon what I had found online these are some things to try to fix this VSCODE Error.
Update Python3 (DONE)
Create a virtual environment to see if I can change the interpating path. The create page does not show since I may not have the correct things installed. 
Spend some time creating a environment to run this program correctly without errors.

This still works just vscode is reading these lines bellow as errors rather than being a actual error when I run the program. 
'''
sys.path.append('..')
from functions.parseData    import parseData
from functions.chords       import chordsList, findChords
from functions.scales       import scaleIntervals, intervalConv, scaleAppending, findScale
from functions.lineRomove   import deleteLastLine
# List of global varibles possibly used once in a class?
# userSharpOrFlat = None
# userScaleInput  = None
# userNoteInput   = None
# sharpNotes      = None
# flatNotes       = None
# intervals       = None
# scale           = None
# notes           = None
while True:
    intro_text = '\n----♪ Welcome to my Scale Program! ♪----\n\n----How to use----\n'\
        'Step 1: Enter how you want to see the notes! Either in sharps (#) or flats (b)\n'\
        'Step 2: Enter a Scale. Type in info to list out the differnt scales aviable!\n'\
        'Step 3: Choose your note! This can be any note in the western scale.\n'\
        '\n----♪ Current Scales in program ♪----\n'\
        'Major (Ionian)\nMinor (Aeolian)\nDorian\nPhrygian\nLydian\nMixolydian\nLocrian\nMajor Pentatonic\nMinor Pentatonic\n'\
        '\n----Extra Info----\nYou can even type in "help" at anypoint to show extra instructions! (This is a feature later in time)\n'\
        'To quit the program press "CTRL + C" or "q"\n'\

    print(intro_text)
    while True:
        try:
            tcflush(sys.stdin, TCIFLUSH)
            # open('data.json') works only in terminal?
            # This absolute path is used to debug in VSCODE for whatever reason
            # fileRead = open('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/scale_generator/main/data.json')
            fileRead = open('data.json')
            data = json.load(fileRead)
            notes, scaleNames, chordsInKeys = parseData(data)

            userSharpOrFlat = input('Show Sharp or Flat? Enter "Sharp" or "Flat": ').lower().strip()
            if userSharpOrFlat == 'q':
                print('You have quit the program.\n')
                exit()
            breakFlag = False
            while True:
                while True:     
                    print('\nEnter "!info" for a list of all the current scales!')
                    userScaleInput = input('Pick a Scale or Mode: ')
                    if userScaleInput == '!info':
                        if isinstance(scaleNames, dict):
                            print('\nUseable scales in this program:\n--------')
                            for x, y in scaleNames.items():
                                scaleInfo = x.capitalize() 
                                print('{}'.format(scaleInfo))
                            print('--------')
                            break
                    elif userScaleInput == 'q':
                        print('You have quit the program.\n')       
                        exit()
                    elif isinstance(userSharpOrFlat, str):
                        breakFlag = True
                        break 
                    else: 
                        print('Using "{}" is not reconizable'.format(userScaleInput))
                if breakFlag:
                    break
            userNoteInput = input('Pick a Note: ').strip()
            if userNoteInput == 'q':
                print('You have quit the program.\n')
                exit()

            print('\nHere are your values!\nScale: {}\nNote: {}\nSharp (#) or Flat (b): {}'.format(userScaleInput, userNoteInput, userSharpOrFlat))
            userStart = input('Are you ready to continue? (Y/N)\n').lower().strip()
            if isinstance(userStart, str):
                lineAmount = len(userStart.splitlines()) + 2
                deleteLastLine(lineAmount)
            if userStart == 'y':
                intervals   = scaleIntervals(userScaleInput, scaleNames)
                scale       = findScale(userNoteInput, userSharpOrFlat, intervals, notes)
                if isinstance(scale, list):
                    scaleStr = ', '.join(scale)
                    print('\nHere are the notes in the {} {} scale: \n{}\n'.format(userNoteInput, userScaleInput, scaleStr))
                    
                userStartChords = input('Do you want to see the Chords? (Y/N)\n').lower().strip()
                if isinstance(userStartChords, str):
                    lineAmount = len(userStartChords.splitlines()) + 2
                    deleteLastLine(lineAmount)
                if userStartChords == 'y':
                    chords  = findChords(scale, intervals, userScaleInput, chordsInKeys)
                    print('\nHere are your chrods in the {} {} scale:\n{}\n'.format(userNoteInput, userScaleInput, chords))
                elif userStartChords == 'n' or userStartChords == 'q':
                    print('\n----Enter another Scale! If you wish to exit, press "q"----\n')
                else:
                    print('\n----You have entered a incorrect statement "{}"----\n'.format(userStartChords))
                userShowIntervals = input('Do you want to see the Intervals? (Y/N)\n').lower().strip()

                if isinstance(userShowIntervals, str):
                    lineAmount = len(userShowIntervals.splitlines()) + 2
                    deleteLastLine(lineAmount)
                if userShowIntervals == 'y':
                    intervalDistance = intervalConv(intervals, scale)
                    if isinstance(intervalDistance, list):
                        intervals = ('\n'.join(map(str, intervalDistance)))
                        print('\nHere are the note distances: {} {} scale: \n{}'.format(userNoteInput, userScaleInput, intervals))
                        print('\n\n----Find a new scale----\n\n')
                elif userShowIntervals == 'n' or userShowIntervals == 'q':
                    print('\n----Enter another Scale! If you wish to exit, press "q"----\n')
                else:
                    print('\n----You have entered a incorrect statement "{}"----\n'.format(userShowIntervals))
            elif userStart == '!info':
                print('WILL ADD THIS LATER BUT SINCE ITS NOT HERE...\nBYE BYE...\n')
                exit()
            elif userStart == 'n' or userStart == 'q':
                print('\n----You have quit the program!----\n')
                exit()
            else:
                print('\n----You have entered a incorrect input! "{}"----\n'.format(userStart))
            fileRead.close()
        except Exception as err: 
            colorlog.error('\nA error occured --> : "{}"\n'.format(err))
            print('Re-enter you values once more!\n')
            pass
