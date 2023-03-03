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
    print(type(i))
  
# Closing file
f.close()

# Test
# geek = '{"Name": "nightfury1", "Languages": ["Python", "C++", "PHP"]}'
# geek_dict = json.loads(geek)
# print(geek_dict)
# print(type(geek_dict))

