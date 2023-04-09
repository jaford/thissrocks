import time
import datetime
import keyboard
import logging
import sys, signal
from termios import tcflush, TCIFLUSH
logging.basicConfig(level=logging.DEBUG)
# from metronomeInfo import metronomeHelp, metronomeMath

def userInputs():
    tcflush(sys.stdin, TCIFLUSH)
    bpmInput = input('Enter BPM: ').lower()
    if bpmInput == 'q':
        print('You have quit the program.\n')       
        exit()
    if bpmInput == 'help':
        # help(metronomeHelp)
        print('Will add functionality once error is fixed! :)')

    noteVal = input('Enter a note value: ').lower()
    if noteVal == 'quarter':
        beatVal = 4
    elif noteVal == 'eighth':
        beatVal = 8
    elif noteVal == 'sixteenth':
        beatVal = 16
    elif noteVal == 'thirty-second' or noteVal == 'thirty second':
        beatVal = 32
    
    if noteVal == 'q':
        print('You have quit the program.\n')       
        exit()
    if noteVal == 'help':
        # help(metronomeHelp)
        print('Will add functionality once error is fixed! :)')
        
    userBeatInput = input('Enter your how many beats per measure: ').lower()
    beatNum = int(userBeatInput)
    if beatNum == 'q':
        print('You have quit the program.\n')       
        exit()
    if beatNum == 'help':
        # help(metronomeHelp)
        print('Will add functionality once error is fixed! :)')

    return beatNum, noteVal, bpmInput, beatVal

def metronomeValues(noteVal, bpmInput):
    while True:
        if noteVal == 'quarter':
            userBPM = float(bpmInput)
            secVal = (60/userBPM)
            beatVal = 4
            break
        elif noteVal == 'eighth':
            userBPM = float(bpmInput)
            secVal = (30/userBPM)
            beatVal = 8
            break
        elif noteVal == 'sixteenth':
            userBPM = float(bpmInput)
            secVal = (15/userBPM)
            beatVal = 16
            break
        elif noteVal == 'thirty-second' or noteVal == 'thirty second':
            userBPM = float(bpmInput)
            secVal = (7.5/userBPM)
            beatVal = 32
            break
        else: 
            print('Note value was not reconized: {}\n'.format(noteVal))
            break 

    return secVal, beatVal

def metronomeCounter(bpmInput, noteVal, beatNum, beatVal, secVal):
    print('\nBPM: {}\nNote Value: {}\nTime signature: {}/{}\n'.format(bpmInput, noteVal, beatNum, beatVal))
    tstep = datetime.timedelta(seconds=secVal)
    tnext = datetime.datetime.now() + tstep
    logging.debug('\ntstep: {}\ntnext {}\nbeatVal: {}\nsecVal: {}\n'.format(tstep, tnext, beatVal, secVal))

    try:
        while True:
            if keyboard.is_pressed('Q') or keyboard.is_pressed('q'):
                print('\n----You have restarted the Metronome----\nTo exit, enter "Q"\n')    
                break
            for x in range(0,beatNum):
                # Leaving this here for future implacation! 
                # playsound('programs/metronome/metronomeSounds/metronome-85688.mp3')
                # playsound('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/metronome/metronomeSounds/metronome-85688.mp3')  
                tdiff = tnext - datetime.datetime.now()
                time.sleep(tdiff.total_seconds()) # Using the time.sleep allows you to print in n amount of time
                tnext = tnext + tstep
                y = '\r' + 'Beep ' + 'Boop ' * x
                sys.stdout.write("\033[K") #Clear to the end of line
                print(y, end='\r')
            print('\n\nsecVal: {}\ntstep: {}\ntnext: {}\ntdiff: {}\ny: {}\nx: {}\n'.format(secVal, tstep, tnext, tdiff, y, x))
    except KeyboardInterrupt as key_err:
        print('----You have restarted Metronome----\n'.format(key_err))
    return tstep, tnext