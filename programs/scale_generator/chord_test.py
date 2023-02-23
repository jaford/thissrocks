'''
Chord degrees for keys. 
Display both roman numberals and key names

Example: 
Minor Key
I   = minor 
II  = diminished or minor seventh flat five 
III = major or major seventh 
IV  = minor
VI  = minor
VI  = major 
VII = major

Also attempting to append these list into a single dictionary!
'''
majorKeyChords = [
        'Major', 
        'Minor', 
        'Minor',
        'Major',
        'Major',
        'Minor',
        'Diminished'
]

minorKeyChords = [
        'Minor',
        'Diminished', 
        'Major', 
        'Minor', 
        'Minor', 
        'Major', 
        'Major'
]

aMajorKeyNotes = [        
        'A', 
        'B', 
        'C#',
        'D',
        'E',
        'F',
        'G#'
]

aMinorKeyNotes = [        
        'A', 
        'B', 
        'C',
        'D',
        'E',
        'F',
        'G'
]

majorInterval = [2, 2, 1, 2, 2, 2, 1]


'''
Example:
Values = [18, 20, 25, 29, 30]
Details = dict({"Age": Values})
print(Details)
'''

new_dict = dict(
        {
                'majorKeyChords': aMajorKeyNotes,
                'minorKeyChords': aMinorKeyNotes
        }
)
print(new_dict)
print(type(new_dict))
for x in new_dict:
  print(x)
  print(type(x))
  notes = new_dict[x]
  print(notes)
  print(type(notes))

majorChordList = '\n'.join('{} {}'.format(aMajorKeyNotes, majorKeyChords) for aMajorKeyNotes, majorKeyChords in zip(aMajorKeyNotes, majorKeyChords))
print(majorChordList)