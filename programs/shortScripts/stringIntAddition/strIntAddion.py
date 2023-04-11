
additionStr = '2+5+10+20'
print('Here is the string given. "{}"\nConvert this to add to 37.\nYou can do this by splitting the "+" from the string.\nTHere you can take the list of strings and convert them into a int. Then do the sum of that converted list!\n\n'.format(additionStr))

strList = additionStr.split('+')
print('Here is the fist string list: \n{}'.format(strList))
print(type(strList))

for i in range(0, len(strList)):
    strList[i] = int(strList[i])
sumList = sum(strList)
print('\nHere is the converted stringed list to a integer list: \n{}\nHere is the sum of all the values from the integer list: \n{}\n'.format(strList, sumList))

