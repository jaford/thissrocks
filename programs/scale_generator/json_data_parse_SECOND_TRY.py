import json

def parseData(data):
    for i in data:
        if (i == 'Sharps' and i == 'Flats'):
            notes = {}
            sharpNotes  = data['Sharps']
            flatNotes   = data['Flats']
            notes['Shaprs'] = sharpNotes
            notes['Flats'] = flatNotes
            print(notes)
            print(type(notes))
        if (i == 'majorIntervals' and i == 'minorIntervals' and i == 'dorianIntervals' and i == 'phrygianIntervals' and i == 'lydianIntervals' and i == 'mixolydianIntervals' and i == 'locrianIntervals' and i == 'majorPentatonics' and i == 'minorPentatonics'):
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
            print(scaleNames)
            print(type(scaleNames))
        if (i == 'major' and i == 'minor' and i == 'dorian' and i == 'phrygian' and i == 'liydian' and i == 'mixoliydian' and i == 'locrian'):
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
            print(chordsInKeys)
            print(type(chordsInKeys))

    return notes, scaleNames, chordsInKeys

fileRead = open('data.json')
data = json.load(fileRead)
print(data)
print(type(data))
notes, scaleNames, chordsInKeys = parseData(data)
fileRead.close()