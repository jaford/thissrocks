'''
This is finally the workable version that prints line by line 
in seconds the quarter notes in BPM! A lot easier than I thought! 

Task --> Make text error a red color to stand out!

Had to use "pip install colorlog"! For me "pip3 install colorlog" since I am on a 
newer version of python!

'''
import time
import datetime
import colorlog
import logging

while True:
    user_input = input('Enter BPM: ')
    print('(To quit program press "Q" )')
    try:
        if user_input.capitalize().startswith('Q'):
            print('You have quit the program! ')       
            break
        print('This metronme is in quarter notes only! So far :)\n')   
        user_bpm = float(user_input)
        quarter_seconds = (60/user_bpm)

        tstep = datetime.timedelta(seconds=quarter_seconds)
        tnext = datetime.datetime.now() + tstep
        while True: 
            tdiff = tnext - datetime.datetime.now()
            time.sleep(tdiff.total_seconds())
            tnext = tnext + tstep
            print('Boop')
            # Need to add where I can close program while it runs!
            # if user_input.capitalize().startswith('Q'):
            #     print('You have quit the program! ')       
            #     break

    except Exception as err: 
        user_input_error = str(user_input)
        # print('Entered a incorrect format: {}'.format(user_input_error))
        # print('An error occured --> : {}\n'.format(err))
        colorlog.warning('You have entered a non-supported format: {}'.format(user_input))
        colorlog.error('A error occured --> : {}\n'.format(err))
        pass
