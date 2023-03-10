import json
import pprint
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
