import os
import shutil
# Enter file name into old_file_name
# print('-----File_Renaming_&_Moving-----')
source_folder = '/Volumes/Workspace/CEDocs/TimeCard/'
directory_path = '/Users/hunterpimparatana/Desktop/'

all_files = os.listdir(source_folder)

for file in all_files:
    source = source_folder + file
    destination = directory_path + file
    if os.path_isfile(source): 
        shutil.move(source, destination)