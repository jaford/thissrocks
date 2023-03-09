from itertools import chain

notes_flat_name = ['A', 'Bb', 'B', 'C', 'Dd', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
# notes_sharp_name = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

user_key = input('Enter your Key: ')
# JUST CHECKING
if user_key in notes_flat_name:
    indexed_user_key = notes_flat_name.index(user_key)
    converted_indexed_user_key = indexed_user_key + 1 
    print('List contains this string')
    print(indexed_user_key)
    print(converted_indexed_user_key)

# Trying to make a new list based upon the postion of the notes_flat_name
new_list_all_notes = list(chain(notes_flat_name[converted_indexed_user_key:]))
new_list_all_remainder_notes = list(chain(notes_flat_name[:indexed_user_key]))
print(new_list_all_notes)
print(new_list_all_remainder_notes)
chormatic_scale = new_list_all_notes + new_list_all_remainder_notes
print(chormatic_scale)

'''
Other ways to append the list together just a note for myself
Adding it togher makes sense too and is litterally only one line as well.
for x in new_list_all_remainder_notes:
  new_list_all_notes.append(x)

new_list_all_notes.extend(new_list_all_remainder_notes)
'''

# for notes_flat_name, indexed_user_key in enumerate(notes_flat_name, indexed_user_key):
#     print(notes_flat_name, indexed_user_key)


# Possible Solution later (01.29)
# user_scale = input('Enter your Scale: ').lower()

# if user_scale == 'major':
#     notes_list = [indexed_string]
#     for x in notes_flat_name:
#         notes_list.append(x[0])
#         print(x)
