import colorlog

def scaleIntervals(userScaleInput, scaleNames):
    scale = userScaleInput.lower()
    while True:
        if scale == 'major' in scaleNames or scale == 'ionian' in scaleNames:
            intervals = scaleNames['major']
            break
        elif scale == 'minor' in scaleNames or scale == 'aeolian' in scaleNames:
            intervals = scaleNames['minor']
            break
        elif scale == 'dorian' in scaleNames:
            intervals = scaleNames['dorian']
            break
        elif scale == 'phrygian' in scaleNames:
            intervals = scaleNames['phrygian']
            break
        elif scale == 'lydian'in scaleNames:
            intervals = scaleNames['lydian']
            break
        elif scale == 'mixolydian'in scaleNames:
            intervals = scaleNames['mixolydian']
            break
        elif scale == 'locrian'in scaleNames:
            intervals = scaleNames['locrian']   
            break
        elif scale == 'major pentatonic' in scaleNames or scale == 'major-pentatonic' in scaleNames:
            intervals = scaleNames['major pentatonic'] 
            break
        elif scale == 'minor pentatonic' in scaleNames or scale == 'minor-pentatonic' in scaleNames:
            intervals = scaleNames['minor pentatonic']         
        else:
            colorlog.warning('\nThis is not a supported scale: "{}"'.format(userScaleInput))
            break

    return intervals

def intervalConv(intervals, scales):
    intervalDistance = []
    for x in intervals:
        if x == 1: 
            halfNote = 'Half' 
            intervalDistance.append(halfNote)
        elif x == 2:
            wholeNote = 'Whole'
            intervalDistance.append(wholeNote)
        else:
            print('This list has a value not supported: {}'.format(x))

    return intervalDistance

def scaleAppending(scaleView, note, scaleLength, intervals):
    scale = [] # Creating an empty list
    scale.append(note) # add user inputted note to list
    for i in range(scaleLength - 1):
        note = scaleView[(scaleView.index(note) + intervals[i]) % 12]
        scale.append(note)

    return scale

def findScale(userNoteInput, userSharpOrFlat, intervals, notes):
    if userSharpOrFlat == 'sharp':
        scaleView = notes['Sharps']
    elif userSharpOrFlat == 'flat':
        scaleView = notes['Flats']
    else: 
        colorlog.warning('\nThis is not a supported input: "{}"'.format(userSharpOrFlat))
        
    note = userNoteInput
    if note in scaleView:
        pass
    else:
        colorlog.warning('\nThis is not a supported Note: "{}"'.format(note))
    scaleLength = len(intervals)
    if scaleLength == 5:
        scale = scaleAppending(scaleView, note, scaleLength, intervals)
    elif scaleLength == 7:
        scale = scaleAppending(scaleView, note, scaleLength, intervals)
    else:
        print('If you got here I would be very surprized! But here is your condition that would get you here! {}'.format(scaleLength))

    return scale