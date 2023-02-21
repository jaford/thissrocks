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
        'Minor', 
        'Diminished', 
        'Major',
        'Minor',
        'Minor',
        'Major',
        'Major'
]

majorInterval = [2, 2, 1, 2, 2, 2, 1]

majorChordList = '\n'.join('{} {}'.format(majorInterval, majorKeyChords) for majorInterval, majorKeyChords in zip(majorInterval, majorKeyChords))

print(majorChordList)



