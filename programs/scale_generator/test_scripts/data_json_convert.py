import json

sharpNotes              = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] # All notes in western music in sharps 
flatNotes               = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'] # All notes in western music in flats 
majorIntervals          = [2, 2, 1, 2, 2, 2, 1] # major scale by intervals W W H W W W H
minorIntervals          = [2, 1, 2, 2, 1, 2, 2] # minor scale by intervals W H W W H W W
dorianIntervals         = [2, 1, 2, 2, 2, 1, 2] # Dorian mode by intervals W H W W W H W
phrygianIntervals       = [1, 2, 2, 2, 1, 2, 2] # Phrygian mode by intervals H W W W H W W
lydianIntervals         = [2, 2, 2, 1, 2, 2, 1] # Lydian mode by intervals W W W H W W H 
mixolydianIntervals     = [2, 2, 1, 1, 2, 1, 2] # Mixolydian mode by intervals W W H W W H W
locrianIntervals        = [1, 2, 2, 1, 2, 2, 2] # Locrian mode by intervals H W W H W W W 
majorPentatonics        = [2, 2, 3, 2, 3] # M2 M2 m3 M2 m3
minorPentatonics        = [3, 2, 2, 3, 2] # m3 M2 M2 m3 M2
majorKeyChords          = ['Major', 'Minor', 'Minor', 'Major', 'Major', 'Minor', 'Diminished']
minorKeyChords          = ['Minor', 'Diminished', 'Major', 'Minor', 'Minor', 'Major', 'Major']
dorianKeyChords         = ['Minor', 'Minor', 'Major', 'Major', 'Minor', 'Diminished', 'Major']
phrygianKeyChords       = ['Minor', 'Major', 'Major', 'Minor', 'Diminished', 'Major', 'Minor']
lydianKeyChords         = ['Major', 'Major', 'Minor', 'Diminished', 'Major', 'Minor', 'Minor']
mixolydianKeyChords     = ['Major', 'Minor', 'Diminished', 'Major', 'Minor', 'Minor', 'Major']
locrianKeyChords        = ['Major', 'Major', 'Minor', 'Diminished', 'Major', 'Minor', 'Minor']

chordsInKeys = dict(
    {
        'major'                 : majorKeyChords,
        'minor'                 : minorKeyChords,
        'dorian'                : dorianKeyChords,
        'phrygian'              : phrygianKeyChords,
        'liydian'               : lydianKeyChords,
        'mixoliydian'           : mixolydianKeyChords,
        'locrian'               : locrianKeyChords
    }
)
# Possibly for practice put this another file.
scaleNames = dict(
        {
                'majorIntervals'        : majorIntervals,
                'minorIntervals'        : minorIntervals,
                'dorianIntervals'       : dorianIntervals,
                'phrygianIntervals'     : phrygianIntervals,
                'lydianIntervals'       : lydianIntervals,
                'mixolydianIntervals'   : mixolydianIntervals,
                'locrianIntervals'      : locrianIntervals,
                'majorPentatonics'      : majorPentatonics,
                'minorPentatonics'      : minorPentatonics
        }
)
notes = dict(
    {
        'Sharps': sharpNotes,
        'Flats': flatNotes
    }
)

# # Printing the dictionary data
# print("The dictionary is as: \n", sharpNotes, "\nHere is the type:{}\n".format(type(sharpNotes)))


# # json object getting serialised
# json_object = json.dumps(sharpNotes, indent = 8) 

# # to print the json_object and see the output
# print("The json_object is as below:", json_object,  '\n{}\n'.format(type(json_object)))

json_object_with_dict_scaleNames = json.dumps(scaleNames, indent = 8) 
print("The json_object is as below:", json_object_with_dict_scaleNames,  '\n{}\n'.format(type(json_object_with_dict_scaleNames)))

json_object_with_dict_chords = json.dumps(chordsInKeys, indent = 8) 
print("The json_object is as below:", json_object_with_dict_chords,  '\n{}\n'.format(type(json_object_with_dict_chords)))


json_object_with_dict_notes = json.dumps(notes, indent = 8) 
print("The json_object is as below:", json_object_with_dict_notes,  '\n{}\n'.format(type(json_object_with_dict_notes)))

# making JSON using a Tuple equals mutliple list for whatever reason???
music_dicts = chordsInKeys, scaleNames, notes

with open("data.json", "w") as outfile:
    json.dump(chordsInKeys, outfile)
    json.dump(scaleNames, outfile)
    json.dump(notes, outfile)
    print('You have created a Json file with your multiple dicts: {}\n{}\n{}\n'.format(chordsInKeys, scaleNames, notes))

# for x in music_dicts:
#     print(x, '\n')
#     print(type(x))
#     with open("data.json", "w") as outfile:
#         json.dump(music_dicts, outfile)
#         print('You have created a Json file with your Tuple: {}\n'.format(music_dicts))
    # if isinstance(unpackedDicts, dict):
    #     jsonConvert = json.dumps(unpackedDicts, indent=8)
    #     print("The json_object is as below:", jsonConvert,  '\n{}\n'.format(type(jsonConvert)))



