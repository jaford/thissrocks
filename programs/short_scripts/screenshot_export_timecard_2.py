"""
Version 2 of this file moving system I want to do.
I did this to make sure I can move the defult screenshot location to a spefic directory. 

I want to move only .png files 
"""
import os
import shutil

source_path = r'/Users/hunterpimparatana/Desktop//'
destination_path = r'/Volumes/Workspace/CEDocs/TimeCard//'
# put file name into this variable
file_name = 'Screenshot 2022-09-12 at 10.15.01 AM.png'

# checking if file exist in destination
if os.path.exists(destination_path + file_name):
    # Split name and extention
    data = os.path.splitext(file_name)
    only_name = data[0]
    extension = data[1]

    new_base = only_name + '_copy' + extension
    new_name = os.path.join(destination_path, new_base)

    print('----Your file has been moved!----')
    print('----{}: already exist & a copy has been made----'.format(new_name))
    shutil.move(source_path + file_name, new_name)
else: 
    print('----Your file has been moved!----')
    os.rename(file_name, 'September_12th.png')
    shutil.move(source_path + file_name, destination_path + file_name)