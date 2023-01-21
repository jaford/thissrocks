# THIS WORKS!?!?
def metronome_help(info_list):
    """
    Start by entering a BPM. Choose a note value bellow:\n"Quarter" \n"Eighth"\n"Sixteenth"    
    """ 
    return info_list
user_input = input('Type in help: ').lower()
if user_input == 'help': 
    help(metronome_help)


# def metronome_help2(info_list):
#     """
#     Start by entering a BPM. Choose a note value bellow:\n"Quarter" \n"Eighth"\n"Sixteenth"    
#     """     
#     return info_list

# help(metronome_help2)