'''
The creation of looping through the notes was done by Kai! I changed a section where you can have it diveded by groups of 5 and 7 note scales. 
I have only included a handful of scales for the sake of simplifying. Possibly add more in the future. 

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

Chord degrees for keys. 
Example: 
Minor Key
I   = minor 
II  = diminished or minor seventh flat five 
III = major or major seventh 
IV  = minor
VI  = minor
VI  = major 
VII = major–

sharpNotes              = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # All notes in western music in sharps 
flatNotes               = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'] # All notes in western music in flats 
majorIntervals          = [2, 2, 1, 2, 2, 2, 1] # major scale by intervals W W H W W W H
minorIntervals          = [2, 1, 2, 2, 1, 2, 2] # minor scale by intervals W H W W H W W
dorianIntervals         = [2, 1, 2, 2, 2, 1, 2] # Dorian mode by intervals W H W W W H W
phrygianIntervals       = [1, 2, 2, 2, 1, 2, 2] # Phrygian mode by intervals H W W W H W W
lydianIntervals         = [2, 2, 2, 1, 2, 2, 1] # Lydian mode by intervals W W W H W W H 
mixolydianIntervals     = [2, 2, 1, 1, 2, 1, 2] # Mixolydian mode by intervals W W H W W H W
locrianIntervals        = [1, 2, 2, 1, 2, 2, 2] # Locrian mode by intervals H W W H W W W 
majorPentatonics        = [2, 2, 3, 2, 3] # M2 M2 m3 M2 m3
minorPentatonics        = [3, 2, 2, 3, 2] # m3 M2 M2 m3 M2
majorKeyChords          = ['Major', 'Minor', 'Minor', 'Major', 'Major', 'Minor', 'Diminished']
minorKeyChords          = ['Minor', 'Diminished', 'Major', 'Minor', 'Minor', 'Major', 'Major']
dorianKeyChords         = ['Minor', 'Minor', 'Major', 'Major', 'Minor', 'Diminished', 'Major']
phrygianKeyChords       = ['Minor', 'Major', 'Major', 'Minor', 'Diminished', 'Major', 'Minor']
lydianKeyChords         = ['Major', 'Major', 'Minor', 'Diminished', 'Major', 'Minor', 'Minor']
mixolydianKeyChords     = ['Major', 'Minor', 'Diminished', 'Major', 'Minor', 'Minor', 'Major']
locrianKeyChords        = ['Major', 'Major', 'Minor', 'Diminished', 'Major', 'Minor', 'Minor']

chordsInKeys = dict(
    {
        'major'                 : majorKeyChords,
        'minor'                 : minorKeyChords,
        'dorian'                : dorianKeyChords,
        'phrygian'              : phrygianKeyChords,
        'liydian'               : lydianKeyChords,
        'mixoliydian'           : mixolydianKeyChords,
        'locrian'               : locrianKeyChords
    }
)
# Possibly for practice put this another file.
scaleNames = dict(
        {
                'major'                 : majorIntervals,
                'minor'                 : minorIntervals,
                'dorian'                : dorianIntervals,
                'phrygian'              : phrygianIntervals,
                'liydian'               : lydianIntervals,
                'mixoliydian'           : mixolydianIntervals,
                'locrian'               : locrianIntervals,
                'major pentatonic'      : majorPentatonics,
                'minor pentatonic'      : minorPentatonics
        }
)
notes = dict(
    {
        'Sharps': sharpNotes,
        'Flats': flatNotes
    }
)
'''
import colorlog
import os
import sys, signal
import json
from termios import tcflush, TCIFLUSH

def parseData(data):
    if ('Sharps' and 'Flats') in data:
        notes = {}
        sharpNotes  = data['Sharps']
        flatNotes   = data['Flats']
        notes['Sharps'] = sharpNotes
        notes['Flats']  = flatNotes
    if ('majorIntervals' and 'minorIntervals' and 'dorianIntervals' and 'phrygianIntervals' and 'lydianIntervals' and 'mixolydianIntervals' and 'locrianIntervals' and 'majorPentatonics' and 'minorPentatonics') in data:
        scaleNames = {}
        majorIntervals      = data['majorIntervals']
        minorIntervals      = data['minorIntervals']
        dorianIntervals     = data['dorianIntervals']
        phrygianIntervals   = data['phrygianIntervals']
        lydianIntervals     = data['lydianIntervals']
        mixolydianIntervals = data['mixolydianIntervals']
        locrianIntervals    = data['locrianIntervals']
        majorPentatonics    = data['majorPentatonics']   
        minorPentatonics    = data['minorPentatonics']  
        scaleNames['major']             = majorIntervals
        scaleNames['minor']             = minorIntervals
        scaleNames['dorian']            = dorianIntervals
        scaleNames['phrygian']          = phrygianIntervals
        scaleNames['liydian']           = lydianIntervals
        scaleNames['mixoliydian']       = mixolydianIntervals
        scaleNames['locrian']           = locrianIntervals
        scaleNames['major pentatonic']  = majorPentatonics
        scaleNames['minor pentatonic']  = minorPentatonics
    if ( 'major' and 'minor' and 'dorian' and 'phrygian' and 'liydian' and 'mixoliydian' and 'locrian') in data:
        chordsInKeys = {}
        majorKeyChords      = data['major']
        minorKeyChords      = data['minor']
        dorianKeyChords     = data['dorian']
        phrygianKeyChords   = data['phrygian']
        lydianKeyChords     = data['liydian']
        mixolydianKeyChords = data['mixoliydian']
        locrianKeyChords    = data['locrian']
        chordsInKeys['major']       = majorKeyChords
        chordsInKeys['minor']       = minorKeyChords
        chordsInKeys['dorian']      = dorianKeyChords
        chordsInKeys['phrygian']    = phrygianKeyChords
        chordsInKeys['liydian']     = lydianKeyChords
        chordsInKeys['mixoliydian'] = mixolydianKeyChords
        chordsInKeys['locrian']     = locrianKeyChords

    return notes, scaleNames, chordsInKeys
    
def scaleIntervals(userScaleInput, scaleNames):
    scale = userScaleInput.lower()
    while True:
        if scale == 'major' in scaleNames or scale == 'ionian' in scaleNames:
            intervals = scaleNames['major']
            break
        elif scale == 'minor' in scaleNames or scale == 'aeolian' in scaleNames:
            intervals = scaleNames['minor']
            break
        elif scale == 'dorian' in scaleNames:
            intervals = scaleNames['dorian']
            break
        elif scale == 'phrygian' in scaleNames:
            intervals = scaleNames['phrygian']
            break
        elif scale == 'lydian'in scaleNames:
            intervals = scaleNames['lydian']
            break
        elif scale == 'mixolydian'in scaleNames:
            intervals = scaleNames['mixolydian']
            break
        elif scale == 'locrian'in scaleNames:
            intervals = scaleNames['locrian']   
            break
        elif scale == 'major pentatonic' in scaleNames or scale == 'major-pentatonic' in scaleNames:
            intervals = scaleNames['major pentatonic'] 
            break
        elif scale == 'minor pentatonic' in scaleNames or scale == 'minor-pentatonic' in scaleNames:
            intervals = scaleNames['minor pentatonic']         
        else:
            print('This "{}" scale does not exist or has not been added!'.format(userNoteInput))
            break

    return intervals

def scaleAppending(scaleView, note, scaleLength):
    scale = [] # Creating an empty list
    scale.append(note) # add user inputted note to list
    for i in range(scaleLength - 1):
        note = scaleView[(scaleView.index(note) + intervals[i]) % 12]
        scale.append(note)

    return scale

def findScale(userNoteInput, userSharpOrFlat, intervals, notes):

    if userSharpOrFlat == 'sharp':
        scaleView = notes['Sharps']
    elif userSharpOrFlat == 'flat':
        scaleView = notes['flats']
    else: 
        print('Entered incorrect value: {}'.format(userSharpOrFlat))
        
    note = userNoteInput
    scaleLength = len(intervals)
    if scaleLength == 5:
        scale = scaleAppending(scaleView, note, scaleLength)
    elif scaleLength == 7:
        scale = scaleAppending(scaleView, note, scaleLength)
    else:
        print('If you got here I would be very surprized! But here is your condition that would get you here! {}'.format(scaleLength))

    return scale

def chordsList(scale, key):
    chordAppending = '\n'.join('{} {}'.format(scale, key) for scale, key in zip(scale, key))
    return chordAppending 

def findChords(scale, intervals, userScaleInput, chordsInKeys):
    keySignatures = userScaleInput.lower() 
    while True:
        if keySignatures == 'major' or keySignatures == 'ionian':
            key = chordsInKeys['major']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'minor' or keySignatures == 'aeolian':
            key = chordsInKeys['minor']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'dorian':
            key = chordsInKeys['dorian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'phrygian':
            key = chordsInKeys['phrygian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'lydian':
            key = chordsInKeys['lydian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'mixolydian':
            key = chordsInKeys['mixolydian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'locrian':
            key = chordsInKeys['locrian']
            chords = chordsList(scale, key)
            break
        else:
            print('This is not a supported scale or mode in this program yet! {}'.format(keySignatures))
            
    return chords
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
            fileRead = open('data.json')
            # This absolute path is used to debug in VSCODE for whatever reason
            # fileRead = open('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/scale_generator/data.json')
            data = json.load(fileRead)
            notes, scaleNames, chordsInKeys = parseData(data)

            userSharpOrFlat = input('Show Sharp or Flat? Enter "Sharp" or "Flat": ').lower()
            if userSharpOrFlat == 'q':
                print('You have quit the program.\n')
                exit()
            userScaleInput = input('Pick a Scale or Mode: ')
            if userScaleInput == 'q':
                print('You have quit the program.\n')       
                exit()
            userNoteInput = input('Pick a Note: ').strip()
            if userNoteInput == 'q':
                print('You have quit the program.\n')
                exit()

            print('\nHere are your values!\nScale: {}\nNote: {}\nSharp (#) or Flat (b): {}'.format(userScaleInput, userNoteInput, userSharpOrFlat))
            userStart = input('Are you ready to continue? (Y/N)\n').lower()
            if userStart == 'y':
                intervals   = scaleIntervals(userScaleInput, scaleNames)
                scale       = findScale(userNoteInput, userSharpOrFlat, intervals, notes)
                if isinstance(scale, list):
                    scale = ', '.join(scale)
                    print('\nHere are the notes in the {} {} scale: \n{}\n'.format(userNoteInput, userScaleInput, scale))
                userStartChords = input('Do you want to see the Chords? (Y/N)\n').lower()
                if userStartChords == 'y':
                    scale   = findScale(userNoteInput, userSharpOrFlat, intervals, notes) # Calling this again in order to get the scale as a list
                    chords  = findChords(scale, intervals, userScaleInput, chordsInKeys)
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
            fileRead.close()
        except Exception as err: 
            colorlog.error('\nA error occured --> : "{}"\n'.format(err))
            colorlog.warning('\nThis is not a supported Scale: {}'.format(userScaleInput))
            colorlog.warning('\nThis is not a supported Note: {}'.format(userNoteInput))
            colorlog.warning('\nThis is not a Sharp or Flat: {}\n'.format(userSharpOrFlat))
            pass
