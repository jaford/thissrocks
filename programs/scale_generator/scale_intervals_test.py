
majorInterval       = [2, 2, 1, 2, 2, 2, 1] # major scale by interval W W H W W W H
minorInterval       = [2, 1, 2, 2, 1, 2, 2] # minor scale by interval W H W W H W W
dorianInterval      = [2, 1, 2, 2, 2, 1, 2] # Dorian mode by interval W H W W W H W
phrygianInterval    = [1, 2, 2, 2, 1, 2, 2] # Phrygian mode by interval H W W W H W W
lydianInterval      = [2, 2, 2, 1, 2, 2, 1] # Lydian mode by interval W W W H W W H 
mixolydianInterval  = [2, 2, 1, 1, 2, 1, 2] # Mixolydian mode by interval W W H W W H W
locrianInterval     = [1, 2, 2, 1, 2, 2, 2] # Locrian mode by interval H W W H W W W 
majorPentatonic     = [2, 2, 3, 2, 3] # M2 M2 m3 M2 m3
minorPentatonic     = [3, 2, 2, 3, 2] # m3 M2 M2 m3 M2

scaleIntervals = dict(
        {
                'Major'                 : majorInterval,
                'Minor'                 : minorInterval,
                'Dorian'                : dorianInterval,
                'Phrygian'              : phrygianInterval,
                'Liydian'               : lydianInterval,
                'Mixoliydian'           : mixolydianInterval,
                'Locrian'               : locrianInterval,
                'Major Pentatonic'      : majorPentatonic,
                'Minor Pentatonic'      : minorPentatonic
        }
)

print('\nHere is the list of keys in the dictionary: {}\n'.format(scaleIntervals.keys()))

scale = 'Major'
for scale in scaleIntervals:
    if scale == 'Major':
        print('Here 0.5')
        intervals = majorInterval
        print(intervals)
        print(type(intervals)) 
        break

while True:
    if scale == 'Major' in scaleIntervals:
        print('Here 0.75')
        intervals = majorInterval
        print(intervals)
        print(type(intervals)) 
        break


for i in scaleIntervals:
    print('Here 1')
    print(scaleIntervals)
    print(type(scaleIntervals))
    if 'Minor' in scaleIntervals:
        print('Here 2')
        print(minorInterval)
        print(type(minorInterval))
        scale = minorInterval
        if 2 in minorInterval:
            print('Here 3')
            index = minorInterval.index(1) 
            print(index)
            print(type(index))
        if 2 in dorianInterval:
            print('Here 2.5')
            index = dorianInterval.index(2, 0, 7)
            print(index)
            print(type(index))
            break

print('Outside Loop!')
print(scale)
print(type(scale))
