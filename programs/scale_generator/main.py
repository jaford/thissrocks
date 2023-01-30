def scaleNoteValues(user_note_input):

    if user_note_input == 'A':
        root_note = user_note_input
    elif user_note_input == 'Bb':
        root_note = user_note_input
    elif user_note_input == 'B':
        root_note = user_note_input
    elif user_note_input == 'C':
        root_note = user_note_input
    elif user_note_input == 'Db':
        root_note = user_note_input
    elif user_note_input == 'D':
        root_note = user_note_input
    elif user_note_input == 'Eb':
        root_note = user_note_input
    elif user_note_input == 'E':
        root_note = user_note_input
    elif user_note_input == 'F':
        root_note = user_note_input
    elif user_note_input == 'Gb':
        root_note = user_note_input
    elif user_note_input == 'G':
        root_note = user_note_input
    elif user_note_input == 'Ab':
        root_note = user_note_input
    else:
        print('Some sort of error catchs')
    
    return root_note

def scaleKeyValue(root_note):

    if user_scale_input == 'chromatic':
        scale_type = user_scale_input
    elif user_scale_input == 'major':
        scale_type = user_scale_input
    elif user_scale_input == 'minor':
        scale_type = user_scale_input
    else:
        print('Some sort of error catchs')
    return scale_type

notes_flat_name = ['A', 'Bb', 'B', 'C', 'Dd', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
notes_sharp_name = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

user_note_input = input('Enter a Note: ')
if user_note_input == 'q' or user_note_input == 'Q':
        print('You have quit the program.\n')       
        exit()
user_scale_input = input('Enter a Scale: ').lower()
if user_scale_input == 'q':
        print('You have quit the program.\n')       
        exit()

root_note   = scaleNoteValues(user_note_input)
scale_type  = scaleKeyValue(root_note) 
