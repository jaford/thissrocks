import os
import shutil

# Enter file name into old_file_name
#print('-----File_Renaming_&_Moving-----')
directory_path = '/Users/hunterpimparatana/Desktop'

x = os.listdir(directory_path)
# print(x)

for root, dirs, filenames in os.walk(directory_path):
    print(root)
    for filename in filenames:
        file_path = os.path.join(root, filename)
        print(file_path)
        if filename == '.DS_Store':
            pass




    # a = (root, dirs, filenames)
    # print(a[0])



# old_file_name = '/Users/hunterpimparatana/Desktop/Screenshot 2022-08-11 at 3.34.12 PM.png'
# new_file_name = '/Volumes/Workspace/CEDocs/TimeCard/August_11th.png'

# # os.rename(old_file_name, new_file_name)
# # We can also check whether it the file already exists!
# if os.path.isfile(new_file_name):
#     print('-----This file already exists!-----')
# else:
#     # Renames file 
#     shutil.move(old_file_name, new_file_name)
#     print('-----File has been renamed & moved-----')

# # Next is to make this more dynamic! 
