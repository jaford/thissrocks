class scales:
    #constructor function    
    def __init__(self, name = '', intervals = [], sharps = [], flats = [], chords=[]):
        self.name       = name
        self.intervals  = intervals
        self.sharps     = sharps
        self.flats      = flats
        self.chords     = chords

        def userInput(self):
            userInput = input('Enter the scale you would like to see: ').lower()
            if userInput == 'minor': 
                print('You are here 1\n')
            elif userInput == 'major':
                print('You are here 2\n')
            else:
                print('You are here 3\n') 



minorScale = scales(name='Minor Scale', intervals=[2, 1, 2, 2, 1, 2, 2], sharps=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], flats=["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"])
print('Here is your "{}" and the intervals are "{}".\nHere are some notes yout can use in the westernscale:\nSharps: {}\nFlats: {}'.format(minorScale.name, minorScale.intervals, minorScale.sharps, minorScale.flats))