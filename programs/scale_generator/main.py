'''
Most of this code is from Kai tbh but at this moment I have a handful of items to test! 
It is getting late so I am stopping for now lol

'''
import colorlog
import os
import sys, signal
from termios import tcflush, TCIFLUSH

def scaleIntervals(userScaleInput):
    '''
    Note:
    Wholestep   = 2
    Halfstep    = 1
    Example:
    Dorian = W H W W W H W 
    Which is = 2 1 2 2 2 1 2 in the indexing list! 

    Pentatonics only have 5 notes in their scale. These next lists will be in orders of 5
    Example: 
    M = Major
    m = Minor
    major pentatonic scale = M2 M2 m3 M2 m3
    '''
    majorInterval       = [2, 2, 1, 2, 2, 2, 1] # major scale by interval W W H W W W H
    minorInterval       = [2, 1, 2, 2, 1, 2, 2] # minor scale by interval W H W W H W W
    dorianInterval      = [2, 1, 2, 2, 2, 1, 2] # Dorian mode by interval W H W W W H W
    phrygianInterval    = [1, 2, 2, 2, 1, 2, 2] # Phrygian mode by interval H W W W H W W
    lydianInterval      = [2, 2, 2, 1, 2, 2, 1] # Lydian mode by interval W W W H W W H 
    mixolydianInterval  = [2, 2, 1, 1, 2, 1, 2] # Mixolydian mode by interval W W H W W H W
    locrianInterval     = [1, 2, 2, 1, 2, 2, 2] # Locrian mode by interval H W W H W W W 
    majorPentatonic     = [2, 2, 3, 2, 3] # M2 M2 m3 M2 m3
    minorPentatonic     = [3, 2, 2, 3, 2] # m3 M2 M2 m3 M2

    scale = userScaleInput.lower()
    if scale == 'major' or scale == 'ionian':
        interval = majorInterval
    elif scale == 'minor' or scale == 'aeolian':
        interval = minorInterval
    elif scale == 'dorian':
        interval = dorianInterval
    elif scale == 'phrgian':
        interval = phrygianInterval
    elif scale == 'lydian':
        interval = lydianInterval
    elif scale == 'mixolydian':
        interval = mixolydianInterval 
    elif scale == 'locrian':
        interval = locrianInterval    
    elif scale == 'major pentatonic' or scale == 'major-pentatonic':
        interval = majorPentatonic 
    elif scale == 'minor pentatonic' or scale == 'minor-pentatonic':
        interval = minorPentatonic          
    else:
        print('This "{}" scale does not exist or has not been added!'.format(userNoteInput))
        return

    return interval

def findNotes(userNoteInput, userScaleInput, interval):

    if userSharpOrFlat == 'sharp':
        scaleView = sharpNotes
    elif userSharpOrFlat == 'flat':
        scaleView = flatNotes
    else: 
        print('Entered incorrect value: {}'.format(userSharpOrFlat))
        
    note = userNoteInput
    scaleLength = len(interval)
    if scaleLength == 5:
        scale = [] # Creating an empty list
        scale.append(note) # add user inputted note to list
        for i in range(scaleLength - 1):
            note = scaleView[(scaleView.index(note) + interval[i]) % 12]
            scale.append(note)
    elif scaleLength == 7:
        scale = [] # Creating an empty list
        scale.append(note) # add user inputted note to list
        for i in range(scaleLength - 1):
            note = scaleView[(scaleView.index(note) + interval[i]) % 12]
            scale.append(note)
    else:
        print('If you got here I would be very surprized! But here is your condition that would get you here! {}'.format(scaleLength))

    return scale

while True:
    intro_text = '\n----♪ Welcome to my Scale Program! ♪----\n\n----How to use----\nStep 1: Start by entering a Scale. Type in info to list out the differnt scales aviable!\n'\
        'Step 2: Choose your note! This can be any note in the western scale.\n'\
        'Step 3: Enter how you want to see the notes! Either in sharps (#) or flats (b)\n'\
        '\n----♪ Current Scales in program ♪----\n'\
        'Major\nMinor\nDorian\nPhrygian\nLydian\nMixolydian\nLocrian\nMajor Pentatonic\nMinor Pentatonic\n'\
        '\n----Extra Info----\nYou can even type in "help" at anypoint to show extra instructions! (This is a feature later in time)\n'\
        'To quit the program press "CTRL + C" or "q"\n'\
        'As of now, add more scales, create a pentatonics list, and maybe a info page that shows relative minor or major.\n'\

    print(intro_text)
    while True:
        try:
            tcflush(sys.stdin, TCIFLUSH)
            userScaleInput  = None
            userNoteInput   = None
            userSharpOrFlat = None
            sharpNotes      = None
            flatNotes       = None

            sharpNotes  = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # All notes in western music in sharps 
            flatNotes   = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'] # All notes in western music in flats 
            userScaleInput  = input('Pick a Scale or Mode: ')
            if userScaleInput == 'q':
                print('You have quit the program.\n')       
                exit()
            userNoteInput = input('Pick a Note: ')
            if userNoteInput == 'q':
                print('You have quit the program.\n')
                exit()
            userSharpOrFlat = input('Show Sharp or Flat? Enter "Sharp" or "Flat": ').lower()
            if userSharpOrFlat == 'q':
                print('You have quit the program.\n')
                exit()

            print('\nHere are your values!\nScale: {}\nNote: {}\nSharp (#) or Flat (b): {}'.format(userScaleInput, userNoteInput, userSharpOrFlat))
            userStart = input('Are you ready to continue?(Y/N)\n').lower()
            if userStart == 'y':
                interval    = scaleIntervals(userScaleInput)
                scale       = findNotes(userNoteInput, userScaleInput, interval)
                scale = ', '.join(scale)
                print('\nHere are the notes in the {} {} scale: \n{}\n\n----Pick another scale!----\nEnter "q" at anytime to close program!\n'.format(userNoteInput, userScaleInput, scale))
            elif userStart == '!info':
                print('WILL ADD THIS LATER BUT SINCE ITS NOT HERE...\nBYE BYE...\n')
                exit()
            elif userStart == 'n':
                print('\n----You have quit the program!----\n')
                exit()
            else:
                print('\n----You have entered a incorrect input! "{}"----\n'.format(userStart))
            
        except Exception as err: 
            colorlog.error('\nA error occured --> : "{}"\n'.format(err))
            colorlog.warning('\nThis is not a supported Scale: {}'.format(userScaleInput))
            colorlog.warning('\nThis is not a supported Note: {}'.format(userNoteInput))
            colorlog.warning('\nThis is not a Sharp or Flat: {}\n'.format(userSharpOrFlat))
            pass
