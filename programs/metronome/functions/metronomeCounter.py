import time
import datetime
import keyboard
import sys, signal

def metronomeValues(user_note_val, user_bpm_input):
    while True:
        if user_note_val == 'quarter':
            user_bpm = float(user_bpm_input)
            sec_val = (60/user_bpm)
            beat_val = 4
            break
        elif user_note_val == 'eighth':
            user_bpm = float(user_bpm_input)
            sec_val = (30/user_bpm)
            beat_val = 8
            break
        elif user_note_val == 'sixteenth':
            user_bpm = float(user_bpm_input)
            sec_val = (15/user_bpm)
            beat_val = 16
            break
        elif user_note_val == 'thirty-second' or user_note_val == 'thirty second':
            user_bpm = float(user_bpm_input)
            sec_val = (7.5/user_bpm)
            beat_val = 32
            break
        else: 
            print('Note value was not reconized: {}\n'.format(user_note_val))
            break 

    return sec_val, beat_val

def metronomeCounter(user_bpm_input, user_note_val, beat_num, beat_val, sec_val):
    print('\nBPM: {}\nNote Value: {}\nTime signature: {}/{}\n'.format(user_bpm_input, user_note_val, beat_num, beat_val))
    tstep = datetime.timedelta(seconds=sec_val)
    tnext = datetime.datetime.now() + tstep
    try:
        while True:
            if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
                print('\n----You have restarted the Metronome----\nTo exit, enter "Q"\n')    
                break
            for x in range(0,beat_num):
                # Leaving this here for future implacation! 
                # playsound('programs/metronome/metronomeSounds/metronome-85688.mp3')
                # playsound('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/metronome/metronomeSounds/metronome-85688.mp3')  
                tdiff = tnext - datetime.datetime.now()
                time.sleep(tdiff.total_seconds())
                tnext = tnext + tstep
                y = '\r' + 'Beep ' + 'Boop ' * x
                sys.stdout.write("\033[K") #Clear to the end of line
                print(y, end='\r')
    except KeyboardInterrupt as key_err:
        print('----You have restarted Metronome----\n'.format(key_err))
    return tstep, tnext