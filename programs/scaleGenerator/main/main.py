'''
The creation of looping through the notes was done by Kai! I changed a section where you can have it diveded by groups of 5 and 7 note scales. 
I have only included a handful of scales for the sake of simplifying. Possibly add more in the future. 

IMPORTANT NOTE:
File read function is not being used! :(
'''
import sys, signal
import os
import colorlog
import json
sys.path.append('..')
from termios import tcflush, TCIFLUSH
from functions.parseData    import parseData
from functions.userInputs   import userValueInputs, userInitiation
from functions.lineRemove   import deleteLastLine
# from functions.chords       import chordsList, findChords
# from functions.scales       import scaleIntervals, intervalConv, scaleAppending, findScale

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
    introText = '\n----♪ Welcome to my Scale Program! ♪----\n\n----How to use----\n'\
        'Step 1: Enter how you want to see the notes! Either in sharps (#) or flats (b)\n'\
        'Step 2: Enter a Scale. Type in info to list out the differnt scales aviable!\n'\
        'Step 3: Choose your note! This can be any note in the western scale.\n'\
        '\n----♪ Current Scales in program ♪----\n'\
        'Major (Ionian)\nMinor (Aeolian)\nDorian\nPhrygian\nLydian\nMixolydian\nLocrian\nMajor Pentatonic\nMinor Pentatonic\n'\
        '\n----Extra Info----\nYou can even type in "help" at anypoint to show extra instructions! (This is a feature later in time)\n'\
        'To quit the program press "CTRL + C" or "q"\n'\

    print(introText)
    userStart = input('Are you ready to start? (Y/N)\n').lower().strip()
    if isinstance (userStart, str):
        lineAmount = len(userStart.splitlines())
        deleteLastLine(lineAmount)
        if isinstance (introText, str):
            lineAmount = len(introText.splitlines())
            deleteLastLine(lineAmount)
    if userStart == 'y':
        while True:
            try:
                '''
                open('data.json') works only in terminal?
                This absolute path is used to debug in VSCODE for whatever reason
                fileRead = open('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/scale_generator/main/data.json')
                '''
                tcflush(sys.stdin, TCIFLUSH)
                fileRead = open('data.json')
                data = json.load(fileRead)
                notes, scaleNames, chordsInKeys = parseData(data)
                userSharpOrFlat, userScaleInput, userNoteInput = userValueInputs(scaleNames)
                userInitiation(notes, scaleNames, chordsInKeys, userSharpOrFlat, userScaleInput, userNoteInput)
                
                # print('\nHere are your values!\nScale: {}\nNote: {}\nSharp (#) or Flat (b): {}'.format(userScaleInput, userNoteInput, userSharpOrFlat))
                # userStart = input('Are you ready to continue? (Y/N)\n').lower().strip()
                # if isinstance(userStart, str):
                #     lineAmount = len(userStart.splitlines()) - 1 
                #     deleteLastLine(lineAmount)
                # if userStart == 'y':
                #     intervals   = scaleIntervals(userScaleInput, scaleNames)
                #     scale       = findScale(userNoteInput, userSharpOrFlat, intervals, notes)
                #     if isinstance(scale, list):
                #         scaleStr = ', '.join(scale)
                #         print('\nHere are the notes in the {} {} scale: \n{}\n'.format(userNoteInput, userScaleInput, scaleStr))
                        
                #     userStartChords = input('Do you want to see the Chords? (Y/N)\n').lower().strip()
                #     if isinstance(userStartChords, str):
                #         lineAmount = len(userStartChords.splitlines())
                #         deleteLastLine(lineAmount)
                #     if userStartChords == 'y':
                #         chords  = findChords(scale, intervals, userScaleInput, chordsInKeys)
                #         print('\nHere are your chords in the {} {} scale:\n{}\n'.format(userNoteInput, userScaleInput, chords))
                #     elif userStartChords == 'n' or userStartChords == 'q':
                #         print('\n----Enter another Scale! If you wish to exit, press "q"----\n')
                #     else:
                #         print('\n----You have entered a incorrect statement "{}"----\n'.format(userStartChords))

                #     userShowIntervals = input('Do you want to see the Intervals? (Y/N)\n').lower().strip()
                #     if isinstance(userShowIntervals, str):
                #         lineAmount = len(userShowIntervals.splitlines())
                #         deleteLastLine(lineAmount)
                #     if userShowIntervals == 'y':
                #         intervalDistance = intervalConv(intervals, scale)
                #         if isinstance(intervalDistance, list):
                #             intervals = ('\n'.join(map(str, intervalDistance)))
                #             print('\nHere are the note distances in the {} {} scale: \n{}'.format(userNoteInput, userScaleInput, intervals))
                #             print('\n\n----Find a new scale----\n\n')
                #     elif userShowIntervals == 'n' or userShowIntervals == 'q':
                #         print('\n----Enter another Scale! If you wish to exit, press "q"----\n')
                #     else:
                #         print('\n----You have entered a incorrect statement "{}"----\n'.format(userShowIntervals))
                # elif userStart == '!info':
                #     print('WILL ADD THIS LATER BUT SINCE ITS NOT HERE...\nBYE BYE...\n')
                #     exit()
                # elif userStart == 'n' or userStart == 'q':
                #     print('\n----You have quit the program!----\n')
                #     exit()
                # else:
                #     print('\n----You have entered a incorrect input! "{}"----\n'.format(userStart))
            except Exception as err: 
                colorlog.error('\nA error occured --> : "{}"\n'.format(err))
                print('Re-enter you values once more!\n')
                pass
    elif userStart == 'n' or userStart == 'q':
        print('You have quit the program.\n')
        exit()
    else:
        print('You have entered a incorrect value: {}\nQuiting the program...'.format(userStart))
        exit()

