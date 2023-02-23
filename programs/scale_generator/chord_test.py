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

aMajorKeyNotes = [        
        'A', 
        'B', 
        'C#',
        'D',
        'E',
        'F',
        'G#'
]

majorInterval = [2, 2, 1, 2, 2, 2, 1]

majorChordList = '\n'.join('{} {}'.format(aMajorKeyNotes, majorKeyChords) for aMajorKeyNotes, majorKeyChords in zip(aMajorKeyNotes, majorKeyChords))

print(majorChordList)



