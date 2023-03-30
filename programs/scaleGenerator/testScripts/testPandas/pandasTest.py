import sys
import json
import pandas as pd
 
# setting path
sys.path.insert(0, '/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/scale_generator/functions')

# importing
from parseData import parseData
 
fileRead = open('data.json')
data = json.load(fileRead)
notes, scaleNames, chordsInKeys = parseData(data)

print(notes)
# HOLY FUCK THIS WORKS 

myvar = pd.DataFrame(notes)
print(myvar)