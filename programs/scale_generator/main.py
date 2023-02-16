'''
Most of this code is from Kai tbh but at this moment I have a handful of items to test! It is getting late so I am stopping for now lol

'''
def scaleIntervals(userScaleInput):
    
    majorInterval = [2, 2, 1, 2, 2, 2, 1] # major scale by interval
    minorInterval = [2, 1, 2, 2, 1, 2, 2] # minor scale by interval 

    scale = userScaleInput.lower()
    if scale == 'major':
        interval = majorInterval
    elif scale == 'minor':
        interval = minorInterval
    else:
        print('This scale does not exist! {}'.format(userNoteInput))
        return

    return interval

def findNotes(userNoteInput, interval):

    if userSharpOrFlat == 'sharp':
        scaleView = sharpNotes
    elif userSharpOrFlat == 'flat':
        scaleView = flatNotes
    else: 
        print('Entered incorrect value: {}'.format(userSharpOrFlat))

    note = userNoteInput
    generatedScale = [] # Creating an empty list
    generatedScale.append(note) # add user inputted note to list
    for i in range(6):
        note = scaleView[(scaleView.index(note) + interval[i]) % 12]
        generatedScale.append(note)
    return generatedScale

sharpNotes  = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # All notes in western music in sharps 
flatNotes   = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'] # All notes in western music in flats 

userScaleInput  = input('Pick a Scale: ')
userNoteInput   = input('Pick a Note: ')
userSharpOrFlat = input('Show Sharp or Flat? Enter "Sharp" or "Flat": ').lower()

