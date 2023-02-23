'''
The creation of looping through the notes was done by Kai! I changed a section where you can have it diveded by groups of 5 and 7 note scales. 
I have only included a handful of scales for the sake of simplifying. Possibly add more in the future. 
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

def creatingChords(scale, keySignatures):

    chordAppending = '\n'.join('{} {}'.format(scale, majorKeyChords) for scale, majorKeyChords in zip(scale, majorKeyChords))

    return chordAppending

def findChords(scale, userScaleInput):
    '''
    Chord degrees for keys. 
    Example: 
    Minor Key
    I   = minor 
    II  = diminished or minor seventh flat five 
    III = major or major seventh 
    IV  = minor
    VI  = minor
    VI  = major 
    VII = major
    '''

    majorKeyChords = ['Major', 'Minor', 'Minor', 'Major', 'Major', 'Minor', 'Diminished']
    minorKeyChords = ['Minor', 'Diminished', 'Major', 'Minor', 'Minor', 'Major', 'Major']

    keySignatures = userScaleInput.lower() 
    if keySignatures == 'major' or keySignatures == 'ionian':
        chords = '\n'.join('{} {}'.format(scale, majorKeyChords) for scale, majorKeyChords in zip(scale, majorKeyChords))
        # chords = chordAppending(scale, keySignatures)
    elif keySignatures == 'minor' or keySignatures == 'aeolian':
        chords = '\n'.join('{} {}'.format(scale, minorKeyChords) for scale, minorKeyChords in zip(scale, minorKeyChords))
    else:
        print('If you got here I would be very surprized! But here is your condition that would get you here! {}'.format(keySignatures))

    return chords

while True:
    intro_text = '\n----♪ Welcome to my Scale Program! ♪----\n\n----How to use----\nStep 1: Start by entering a Scale. Type in info to list out the differnt scales aviable!\n'\
        'Step 2: Choose your note! This can be any note in the western scale.\n'\
        'Step 3: Enter how you want to see the notes! Either in sharps (#) or flats (b)\n'\
        '\n----♪ Current Scales in program ♪----\n'\
        'Major (Ionian)\nMinor (Aeolian)\nDorian\nPhrygian\nLydian\nMixolydian\nLocrian\nMajor Pentatonic\nMinor Pentatonic\n'\
        '\n----Extra Info----\nYou can even type in "help" at anypoint to show extra instructions! (This is a feature later in time)\n'\
        'To quit the program press "CTRL + C" or "q"\n'\

    print(intro_text)
    while True:
        try:
            tcflush(sys.stdin, TCIFLUSH)
            userScaleInput  = None
            userNoteInput   = None
            userSharpOrFlat = None
            sharpNotes      = None
            flatNotes       = None
            interval        = None
            scale           = None

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
            userStart = input('Are you ready to continue? (Y/N)\n').lower()
            if userStart == 'y':
                interval    = scaleIntervals(userScaleInput)
                scale       = findNotes(userNoteInput, userScaleInput, interval)
                if isinstance(scale, list):
                    scale = ', '.join(scale)
                    print('\nHere are the notes in the {} {} scale: \n{}\n'.format(userNoteInput, userScaleInput, scale))
                userStartChords = input('Do you want to see the Chords? (Y/N)\n').lower()
                if userStartChords == 'y':
                    scale   = findNotes(userNoteInput, userScaleInput, interval) # Calling this again in order to get the scale as a list
                    chords,   = findChords(scale, userScaleInput)
                    print('\nHere are your chrods in the {} {} scale!\n{}\n----Enter another scale----\n'.format(userNoteInput, userScaleInput, chords))
                elif userStartChords == 'n' or userStartChords == 'q':
                    print('\n----Enter another Scale! If you wish to exit, press "q"----\n')
                else:
                    print('\n----You have entered a incorrect statement "{}"----\n'.format(userStartChords))
            elif userStart == '!info':
                print('WILL ADD THIS LATER BUT SINCE ITS NOT HERE...\nBYE BYE...\n')
                exit()
            elif userStart == 'n' or userStart == 'q':
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
