import os

def folderStructure(directoryMap, indent=''):
    folderStruc = ''
    for root, dirs, files in os.walk(directoryMap):
        folderName = os.path.basename(root)
        folderStruc += f"{indent}+-- {folderName}\n"
        subIndent = indent + '|   '
        for file in files:
            folderStruc += f"{subIndent}+-- {file}\n"
        for dir in dirs:
            subDirectory = os.path.join(root, dir)
            folderStruc += folderStructure(subDirectory, indent=subIndent)
    return folderStruc

# Hard code whatever directory!
directoryMap = '/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/weather'
folderStruc = folderStructure(directoryMap)
print(folderStruc)
