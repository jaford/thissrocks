"""
Version 3 of this file moving system I want to do.
I did this to make sure I can move the defult screenshot location to a spefic directory. 

I want to move only .png files 
"""
import glob 
import os 
import shutil

source_path = r'/Users/hunterpimparatana/Desktop'
destination_path = r'/Volumes/Workspace/CEDocs/TimeCard/'
# put file name into this variable
pattern = "\*.png"
files = glob.glob(source_path + pattern)

# Moving the files with .png extention
for file in files: 
    # extracting file name from file path
    file_name = os.path.basename(file)
    new_file_name = r'September_12th.png'
    file_rename = os.rename(new_file_name)
    shutil.move(file, destination_path + file_rename)
    print('----Moved file: {}----'.format(file))

