import sys
from .scales     import scaleIntervals, intervalConv, scaleAppending, findScale
from .chords     import chordsList, findChords
from .lineRemove import deleteLastLine

def userValueInputs(scaleNames):
    userSharpOrFlat = input('Show Sharp or Flat? Enter "Sharp" or "Flat": ').lower().strip()
    if userSharpOrFlat == 'q':
        print('You have quit the program.\n')
        exit()
    breakFlag = False
    while True:
        while True:     
            print('Enter "!info" for a list of all the current scales!')
            userScaleInput = input('Pick a Scale or Mode: ')
            if userScaleInput == '!info':
                if isinstance(scaleNames, dict):
                    print('\nUseable scales in this program:\n--------')
                    for x, y in scaleNames.items():
                        scaleInfo = x.capitalize() 
                        print('{}'.format(scaleInfo))
                    print('--------')
                    break
            elif userScaleInput == 'q':
                print('You have quit the program.\n')       
                exit()
            elif isinstance(userSharpOrFlat, str):
                breakFlag = True
                break 
            else: 
                print('Using "{}" is not reconizable'.format(userScaleInput))
        if breakFlag:
            break
    userNoteInput = input('Pick a Note: ').strip()
    if userNoteInput == 'q':
        print('You have quit the program.\n')
        exit()

    return userSharpOrFlat, userScaleInput, userNoteInput

def userInitiation(notes, scaleNames, chordsInKeys, userSharpOrFlat, userScaleInput, userNoteInput): 
    print('\nHere are your values!\nScale: {}\nNote: {}\nSharp (#) or Flat (b): {}'.format(userScaleInput, userNoteInput, userSharpOrFlat))
    userStart = input('Are you ready to continue? (Y/N)\n').lower().strip()
    if isinstance(userStart, str):
        lineAmount = len(userStart.splitlines()) - 1 
        deleteLastLine(lineAmount)
    if userStart == 'y':
        intervals   = scaleIntervals(userScaleInput, scaleNames)
        scale       = findScale(userNoteInput, userSharpOrFlat, intervals, notes)
        if isinstance(scale, list):
            scaleStr = ', '.join(scale)
            print('\nHere are the notes in the {} {} scale: \n{}\n'.format(userNoteInput, userScaleInput, scaleStr))
            
        userStartChords = input('Do you want to see the Chords? (Y/N)\n').lower().strip()
        if isinstance(userStartChords, str):
            lineAmount = len(userStartChords.splitlines())
            deleteLastLine(lineAmount)
        if userStartChords == 'y':
            chords  = findChords(scale, intervals, userScaleInput, chordsInKeys)
            print('\nHere are your chords in the {} {} scale:\n{}\n'.format(userNoteInput, userScaleInput, chords))
        elif userStartChords == 'n' or userStartChords == 'q':
            print('\n----Enter another Scale! If you wish to exit, press "q"----\n')
        else:
            print('\n----You have entered a incorrect statement "{}"----\n'.format(userStartChords))

        userShowIntervals = input('Do you want to see the Intervals? (Y/N)\n').lower().strip()
        if isinstance(userShowIntervals, str):
            lineAmount = len(userShowIntervals.splitlines())
            deleteLastLine(lineAmount)
        if userShowIntervals == 'y':
            intervalDistance = intervalConv(intervals, scale)
            if isinstance(intervalDistance, list):
                intervals = ('\n'.join(map(str, intervalDistance)))
                print('\nHere are the note distances in the {} {} scale: \n{}'.format(userNoteInput, userScaleInput, intervals))
                print('\n\n----Find a new scale----\n\n')
        elif userShowIntervals == 'n' or userShowIntervals == 'q':
            print('\n----Enter another Scale! If you wish to exit, press "q"----\n')
        else:
            print('\n----You have entered a incorrect statement "{}"----\n'.format(userShowIntervals))
    elif userStart == '!info':
        print('WILL ADD THIS LATER BUT SINCE ITS NOT HERE...\nBYE BYE...\n')
        exit()
    elif userStart == 'n' or userStart == 'q':
        print('\n----You have quit the program!----\n')
        exit()
    else:
        print('\n----You have entered a incorrect input! "{}"----\n'.format(userStart))

    return 