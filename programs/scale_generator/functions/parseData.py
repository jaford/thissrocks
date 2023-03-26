import json

def fileRead():
    # I beleive this is correct for reading in a file? Not to sure about the close method! 
    fileRead = open('data.json')
    data = json.load(fileRead)
    fileRead.close()

    return data

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