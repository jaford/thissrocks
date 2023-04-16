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


class scales:
    #constructor function    
    def __init__(self, notes={}, scaleNames={}, chordsInKeys={}):
        self.notes = notes
        self.scaleNames = scaleNames
        self.chordsInKeys = chordsInKeys

    def displayDicts(self):
        if 'major' in scaleNames and 'major' in chordsInKeys:
            intervals   = scaleNames.get('major')
            chords      = chordsInKeys.get('major')
            print('You are in the major scale\nMajor Scale intervals: {}\nChords in Scale: {}'.format(intervals, chords))
        elif 'minor' in scaleNames and 'minor' in chordsInKeys:
            intervals   = scaleNames.get('minor')
            chords      = chordsInKeys.get('minor')
            print('You are in the minor scale\nMinor Scale intervals: {}\nChords in Scale: {}'.format(intervals, chords))
        else:
            print('Error\n')
        return intervals, chords


tcflush(sys.stdin, TCIFLUSH)
fileRead = open('data.json')
data = json.load(fileRead)
notes, scaleNames, chordsInKeys = parseData(data)

majorScale = scales(notes, scaleNames, chordsInKeys)
minorScale = scales(notes, scaleNames, chordsInKeys)

majorScale.displayDicts()
minorScale.displayDicts()

