import json
import pprint

def parseData(data):
    if ('Sharps' and 'Flats') in data:
        notes = {}
        sharpNotes  = data['Sharps']
        flatNotes   = data['Flats']
        notes['Sharps'] = sharpNotes
        notes['Flats']  = flatNotes
        # pprint.pprint(notes)
        # print(type(notes))
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
        # pprint.pprint(scaleNames)
        # print(type(scaleNames))
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
        # pprint.pprint(chordsInKeys)
        # print(type(chordsInKeys))

    return notes, scaleNames, chordsInKeys

fileRead = open('json_data/data.json')
data = json.load(fileRead)
print(data)
print(type(data))
notes, scaleNames, chordsInKeys = parseData(data)

print('Here are the notes. {}'.format(notes))
testVar = 'sharp'
if 'Sharps' in notes:
    note = notes['Sharps']
    print(note)
else: 
    print('Error 1')

if 'Flats' in notes:
    note = notes['Flats']
    print(note)
else: 
    print('Error 2')

if testVar == 'sharp':
    note = notes['Sharps']
    print(note)
else: 
    print('Error 3')


'''
JUST TESTING THINGS OUT
userInput = input('Enter "Major": ').lower()

if userInput == 'major' in scaleNames:
    print('You have enterd {}'.format(userInput))
else: 
    print('You did not read what I asked you to do! :(')

userInput2 = input('Do you want to see the list of notes of Flats? (Y/N)').lower()

if userInput2 == 'y':
    scaleView = notes['Flats']
    print('Here are your flats that you wanted.\n{}\nuwu'.format(scaleView))
else: 
    print('Entered incorrect value: {}'.format(userInput2))
'''


fileRead.close()
