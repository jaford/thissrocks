import json
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
print(data, '\n')
print(type(data))

# Iterating through the json
# list
for i in data['majorIntervals']:
    print(i, '\n')
    majorIntervals = i
    print(type(i))
    print(majorIntervals)
  
# Closing file
f.close()

# Test
# geek = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'
# geek_dict = json.loads(geek)
# print(geek_dict)
# print(type(geek_dict))

# with open('data.json') as json_file:
#     file_contents = json_file.read()

# print(file_contents)
# print(type(file_contents))


# for i in data:
#     if i == 'Sharps' or i == 'Flats':
#         sharps = data['Sharps']
#         flats = data['Flats']
#         print(sharps)
#         print(type(sharps))
#         print(flats)
#         print(type(flats))
#         notes = dict(zip(sharps, flats))
#         print(notes)
#         print(type(notes))
#         notes = {}
#         notes['Sharps'] = sharps
#         notes['Flats'] = flats
#         print(notes)
#         print(type(notes))
#         break
f = open('data.json')
file_contents = json.load(f)
print(file_contents)
for i in file_contents:
    if (i == 'Sharps' and i == 'Flats'):
        sharps = file_contents['Sharps']
        flats = file_contents['Flats']
        notes = {}
        notes['Sharps'] = sharps
        notes['Flats'] = flats
        print('In IF STATEMENT')
        print(notes)
        print(type(notes))
    break
print('OUT OF LOOP')
print(notes)

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

notes = testFunc(file_contents)
print('CALLING FROM FUNC')
print(notes)

f.close()
