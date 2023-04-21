import json
import sys, signal
import os
sys.path.append('..')
from termios import tcflush, TCIFLUSH
from functions.dataRead import parseData, jsonRead

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

    def scaleAppending(self, intervals, note, scaleView):
        scaleLength = len(intervals)
        scale = [] # Creating an empty list
        scale.append(note) # add user inputed note to list
        for i in range(scaleLength - 1):
            note = scaleView[(scaleView.index(note) + intervals[i]) % 12]
            scale.append(note)
        
        return scale

    def scaleNotes(self, intervals):
        userInput = input('Show Sharp or Flat? Enter "Sharp" or "Flat": ').lower()
        note = input('Pick a note: ').strip()
        if userInput == 'sharp':
            scaleView = notes['Sharps']
        elif userInput == 'flat':
            scaleView = notes['Flats']
        else:
            print('\nThis is not a supported input: "{}"'.format(userInput))

        scale = self.scaleAppending(intervals, note, scaleView)
        
        return scale

    def displayScale(self, scale):
        if isinstance(scale, list):
            scaleStr = ', '.join(scale)       
            print('\nHere is your scale!\nScale: {}\n'.format(scaleStr))


if __name__ == "__main__":    
    data = jsonRead()
    notes, scaleNames, chordsInKeys = parseData(data)

    userStart = input('Are you ready to start? (Y/N)\n').lower().strip()
    if userStart == 'y':
        createScale = scales(notes, scaleNames, chordsInKeys)
        intervals, chords = createScale.keyIntervals()
        scale = createScale.scaleNotes(intervals)
        createScale.displayScale(scale)
    elif userStart == 'n' or userStart == 'q':
        print('You have quit the program.\n')
        exit()
    else:
        print('You have entered a incorrect value: {}\nQuiting the program...'.format(userStart))
        exit()
