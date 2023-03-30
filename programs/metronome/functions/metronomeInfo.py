import time
import datetime

def metronomeHelp(info_txt):
    """
    \n----Welcome to the help page----\n\
Step 1: Start by entering a BPM. (This can be any positive value)\n
Step 2: Choose a note value bellow: \n"Quarter"   = Counts of 4ths\n"Eighth"    = Counts in 8ths\n"Sixteenth" = Counts in 16ths\n"Thirty-second" = Counts in 32nds\n
Step 3: Enter the amount of beats in each measure.\n(This can be any whole number)\n
    \n----Current Known Bugs (as of 1/23/2023)----\n\
While metronome is running, you can press "Q" or "q" to restart the metronome but it does not always reconize the input.\n
The current fix is to use "CTRL + C" to break the loop.\n
Using this help method is not really a good idea for a more info page. Just thought it was a cool idea.
    """
    return info_txt


def metronomeMath(user_bpm_input, user_note_val, sec_val, beat_num, beat_val):

    print('\n----Here are some cool math things that correlate with beat duration & conversions!----\n(This is for the current inputed items)\n')
    user_bpm = int(user_bpm_input)
    quarter_val = (60/user_bpm)
    eighth_val = (30/user_bpm)
    sixteenth_val = (15/user_bpm)
    thirty_second_val = (7.5/user_bpm)
    milisec = sec_val / 1000
    tstep = datetime.timedelta(seconds=sec_val)
    tstep.total_seconds()

    print('----Here is a list of the second duration for some note values----\nQuarter Note: {}\nEighth Note: {}\nSixteenth Note: {}\nThirty Second Note: {}\n'.format(quarter_val, eighth_val, sixteenth_val, thirty_second_val))
    print('----The second duration of your entered values ({} & {})----\nBeat length in seconds: {}\nBeat length in mili-seconds: {}\n'.format(user_note_val, beat_num, sec_val, milisec))
    print('----Here is the timeDelta numbers of your selected input----\nSeconds of each beat: {}\n'.format(tstep))
    print('----Here is the fancy music terms that your BPM is definded as!----\nTemp: {}\nTime Signiture: {}/{}'.format(user_bpm_input, beat_num, beat_val))
    if user_bpm < 24:
        print('Marking: Larghissimo\nMeaning: Extremely slow\n')
    elif 25 <= user_bpm <= 40:
        print('Marking: Grave\nMeaning: Very slow\n')
    elif 40 <= user_bpm <= 60:
        print('Marking: Largo\nMeaning: Slow\n')
    elif 60 <= user_bpm <= 66:
        print('Marking: Larghetto\nMeaning: Moderately slow\n')
    elif 66 <= user_bpm <= 76:
        print('Marking: Adagio\nMeaning: Slow and expressive\n')
    elif 76 <= user_bpm <= 108:
        print('Marking: Andante\nMeaning: At a walking pace\n')       
    elif 108 <= user_bpm <= 120:
        print('Marking: Moderato\nMeaning: At a moderate speed\n')
    elif 120 <= user_bpm <= 156:
        print('Marking: Allegro\nMeaning: Fast (or bright)\n')
    elif 156 <= user_bpm <= 176:
        print('Marking: Vivace\nMeaning: Fast (or lively)\n')
    elif 168 <= user_bpm <= 200:
        print('Marking: Presto\nMeaning: Very fast\n')
    else: 
        print('Marking: Prestissimo\nMeaning: Extremely fast\n')

    print('----The metronome has restarted----\n')
    return quarter_val, eighth_val, sixteenth_val, thirty_second_val, tstep