class scales:
    scaleName   = ''
    intervals   = []
    Sharps      = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"] 
    Flats       = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    def userInput(self):
        userInput = input('Enter the scale you would like to see: ').lower()
        if userInput == 'minor': 
            print('You are here 1\n')
        elif userInput == 'major':
            print('You are here 2\n')
        else:
            print('You are here 3\n') 


# create objects of class
minorScale = scales()
# modify the scaleName attribute
minorScale.scaleName = "Minor Scale"
# access the intervals attribute
minorScale.intervals = [2, 1, 2, 2, 1, 2, 2] 
print('Here is the "{}" and the intervals are "{}"\n'.format(minorScale.scaleName, minorScale.intervals))
minorScale.userInput()

majorScale = scales()
majorScale.scaleName = 'Major Scale'
majorScale.intervals = [2, 2, 1, 2, 2, 2, 1]
print('Here is the "{}" and the intervals are "{}"\n'.format(majorScale.scaleName, majorScale.intervals))
