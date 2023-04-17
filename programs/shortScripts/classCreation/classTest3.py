import json
import sys, signal
import os
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

def jsonRead():
    tcflush(sys.stdin, TCIFLUSH)
    fileRead = open('data.json')
    data = json.load(fileRead)
    
    return data

class scales:
    #constructor function    
    def __init__(self, notes={}, scaleNames={}, chordsInKeys={}, intervals=[], chords=[]):
        self.notes          = notes
        self.scaleNames     = scaleNames
        self.chordsInKeys   = chordsInKeys
        self.intervals      = intervals
        self.chords         = chords
        self.note           = None
        self.userInput      = None

    def keyIntervals(self):
        userInput = input('Select a scale that you want to use: ').lower()
        if userInput == 'major' or userInput == 'ionian':
            intervals   = scaleNames['major']
            chords      = chordsInKeys['major']
        elif userInput == 'minor' or userInput == 'aeolian':
            intervals   = scaleNames['minor']
            chords      = chordsInKeys['minor']
        elif userInput == 'dorian' in scaleNames:
            intervals   = scaleNames['dorian']
            chords      = chordsInKeys['dorian']    
        elif userInput == 'phrygian' in scaleNames:
            intervals   = scaleNames['phrygian']
            chords      = chordsInKeys['phrygian']    
        elif userInput == 'lydian'in scaleNames:
            intervals   = scaleNames['lydian']
            chords      = chordsInKeys['lydian']    
        elif userInput == 'mixolydian'in scaleNames:
            intervals   = scaleNames['mixolydian']
            chords      = chordsInKeys['mixolydian']    
        elif userInput == 'locrian'in scaleNames:
            intervals   = scaleNames['locrian']   
            chords      = chordsInKeys['locrian']    
        elif userInput == 'major pentatonic' or userInput == 'major-pentatonic':
            intervals   = scaleNames['major pentatonic'] 
            chords      = chordsInKeys['major pentatonic']    
        elif userInput == 'minor pentatonic' or userInput == 'minor-pentatonic':
            intervals   = scaleNames['minor pentatonic']     
            chords      = chordsInKeys['minor pentatonic']    
        else:
            print('\nThis is not a supported scale: "{}"'.format(userInput))
        
        return intervals, chords

    def scaleNotes(self, intervals):
        userInput = input('Show Sharp or Flat? Enter "Sharp" or "Flat": ').lower()
        note = input('Pick a note: ').strip()
        if userInput == 'sharp':
            scaleView = notes['Sharps']
        elif userInput == 'flat':
            scaleView = notes['Flats']
        else:
            print('\nThis is not a supported input: "{}"'.format(userInput))
        
        scaleLength = len(intervals)
        scale = [] # Creating an empty list
        scale.append(note) # add user inputed note to list
        for i in range(scaleLength - 1):
            note = scaleView[(scaleView.index(note) + intervals[i]) % 12]
            scale.append(note)

        return scale

    def displayScale(self, scale):
        if isinstance(scale, list):
            scaleStr = ', '.join(scale)       
            print('\nHere is your scale!\nScale: {}\n'.format(scale))

        return


    '''
    Test this later!
    def chordsList(self, scale, key):
        chordAppending = '\n'.join('{} {}'.format(scale, key) for scale, key in zip(scale, key))
        return chordAppending 

    def createChords(self):
        
        return

    '''
data = jsonRead()
notes, scaleNames, chordsInKeys = parseData(data)

# userStart = input('Are you ready to start? (Y/N)\n').lower().strip()

# if userStart == 'y':
createScale = scales(notes, scaleNames, chordsInKeys)
intervals, chords = createScale.keyIntervals()
scale = createScale.scaleNotes(intervals)
createScale.displayScale(scale)



# elif userStart == 'n' or userStart == 'q':
#     print('You have quit the program.\n')
#     exit()
# else:
#     print('You have entered a incorrect value: {}\nQuiting the program...'.format(userStart))
#     exit()




# minorScale = scales(notes, scaleNames, chordsInKeys)

# Goes into function inside the class
# minorScale.displayDicts()

