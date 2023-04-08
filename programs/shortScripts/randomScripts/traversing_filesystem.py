"""
Traversing a file system. 

Python has a build in function called os.walk

Similar to os.path, this os.walk function allows python to 
generate the file names in a directory tree.

The os.walk function generates the results in a tuples. 
the path, the directory, and the files present. 

Dirpath: A string that is the path to the directory
Dirnames: All the sub-directories from root
Filenames: All the files from the root and directories 
"""
#Import the OS module
import os 

# List and store all directories 
list = []

#Will have to put direct path to a certain directory to have this work
for root, dirs, files in os.walk('/Volumes/Workspace/CEDocs/TimeCard'):
    # The append() method adds an element to the end of a list
    list.append((root, dir, files))

print("List of all sub-directories and files:")
for i in list:
    print(i)

