import json

def testFunc(file_contents):
    for i in file_contents:
        if (i == 'Sharps' and i == 'Flats'):
            sharps = file_contents['Sharps']
            flats = file_contents['Flats']
        else:
            print('This does not exist in data')
        notes = {}
        notes['Sharps'] = sharps
        notes['Flats'] = flats
    return notes


f = open('data.json')
file_contents = json.load(f)
print(file_contents)
print(type(file_contents))

notes = testFunc(file_contents)
print('CALLING FROM FUNC')
print(notes)

f.close()
