import json

# THIS ONE FUCKING WORKS
f = open('json_data/data.json')
# f = open('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/scale_generator/json_tests/json_data/data.json')
file_contents = json.load(f)
print(file_contents)
print(type(file_contents))
dictKeys = list(file_contents.keys())
print('Here are the keys in the JSON file: {}\n'.format(dictKeys))

if 'Sharps' and 'Flats' in file_contents:
    sharps = file_contents['Sharps']
    print(sharps)
    print(type(sharps))
    flats = file_contents['Flats']
    print(flats)
    print(type(flats))
else:
    print('This does not exist in data')
notes = {}
notes['Sharps'] = sharps
notes['Flats'] = flats
print(notes)
print(type(notes))


