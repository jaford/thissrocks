# Makng a txt file using python

filename = 'text.txt'
filehandler = open(filename, "w")

filehandler.write('Here is some text in the first line!\n')
filehandler.write('Some more text new lines.\n')
filehandler.write('Last but not least, the vert last line.\n')

filehandler.close()

# Open file for reading.
filehandler = open(filename, "r")

for line in filehandler:
    print(line)

filehandler.close()