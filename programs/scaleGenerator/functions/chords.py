def chordsList(scale, key):
    chordAppending = '\n'.join('{} {}'.format(scale, key) for scale, key in zip(scale, key))
    return chordAppending 

def findChords(scale, intervals, userScaleInput, chordsInKeys):
    keySignatures = userScaleInput.lower() 
    while True:
        if keySignatures == 'major' or keySignatures == 'ionian':
            key = chordsInKeys['major']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'minor' or keySignatures == 'aeolian':
            key = chordsInKeys['minor']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'dorian':
            key = chordsInKeys['dorian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'phrygian':
            key = chordsInKeys['phrygian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'lydian':
            key = chordsInKeys['lydian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'mixolydian':
            key = chordsInKeys['mixolydian']
            chords = chordsList(scale, key)
            break
        elif keySignatures == 'locrian':
            key = chordsInKeys['locrian']
            chords = chordsList(scale, key)
            break
        else:
            print('This is not a supported scale or mode in this program yet! {}'.format(keySignatures))
            
    return chords