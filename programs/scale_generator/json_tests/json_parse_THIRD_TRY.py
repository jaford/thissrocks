import json

def testFunc(file_contents):
    f = open('data.json')
    file_contents = json.load(f)
    print(file_contents)
    print(type(file_contents))
    print('CALLING FROM FUNC')
    for i in file_contents:
        if (i == 'Sharps' and i == 'Flats') in file_contents:
            sharps = file_contents['Sharps']
            flats = file_contents['Flats']
        else:
            print('This does not exist in data')
        notes = {}
        notes['Sharps'] = sharps
        notes['Flats'] = flats
        f.close()
    return notes

file_contents = None
notes = testFunc(file_contents)
print(notes)
