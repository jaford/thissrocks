# These where attempts to appends list to antoher based upon a list of intergers
# I believe these are called linked list!

'''
cityStateList = ['ABQ', 'Sante Fe', 'NM', 'Austin', 'Dalas', 'TX']
newMexicoCities = [0, 1]
texasCities = [3, 4]

def findCity(state):

    if state == 'NM':
        city = newMexicoCities
    elif state == 'TX':
        city = texasCities
    else:
        print('This city ({}) was not found!'.format(state))
        return 

    cities = []
    cities.append(state)
    for i in range(2):
        state = cityStateList[(cityStateList.index(state) + city[i]) % 2] # find note by interval
        cities.append(state)
    return cities

state = input('Enter State: ').lower()
print(findCity(cities))
'''

'''
chromaticScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # chromatic scale
majorInterval = [2, 2, 1, 2, 2, 2, 1] # major scale by interval
minorInterval = [2, 1, 2, 2, 1, 2, 2] # minor scale by interval

def findScale(note, scale): # find scale by note and desired scale
    scale = scale.lower() # convert scale to lowercase
    note = note.upper() # convert note to uppercase
    if scale == 'major': 
        interval = majorInterval 
    elif scale == 'minor':
        interval = minorInterval
    else: 
        print('Scale not found') # if scale is not major or minor,
        return
    scale = [] # create empty list
    scale.append(note) # add user inputted note to list
    for i in range(6): 
        note = chromaticScale[(chromaticScale.index(note) + interval[i]) % 12] # find note by interval
        scale.append(note)
    return scale # return scale

note = input('Enter a note: ')
scale = input('Enter a scale: ')
print(findScale(note, scale))
'''

