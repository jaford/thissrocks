'''
Starting a timer that can print a line every second. (Done)
Convert this to inputing a time. (Done)

Resources: 
Use the site bellow as referance to make BPM calculation based upon input
https://www.omnicalculator.com/other/bpm

Task --> It looks like I can calculate the input and use that to maybe set the BPM?
Task --> Possibly look at how to calculate BPM using seconds? 
Task --> I could also change timedelta() to set for minutes rather than seconds?  
Task --> Later once I am able to put in x amount of time, change to BPM!  
'''
import time
import datetime 

try: 

    # This bellow allows to take in desited bpm to calc the actual printing time.
    # if t_input == str(""):
    #     print("This is not a number")
    # if t_input == int:
    # bpm = t_input
    # bps = float(bpm) / 60

    '''
    (OLD as of 11/13)
    Task --> Find a way to convert the timedelta into a int
    You can use either minutes or seconds for duration of measure. 
    s_time = datetime.timedelta(seconds=60)
    m_time = datetime.timedelta(minutes=1)
    '''
    # Input in seconds for duration of 1 measure.
    t_input = float(input("Enter measure duration (In seconds): "))
    beat_duration = t_input / 4
    s_time = None
    m_time = None

    s_time = 60 # This is in seconds
    bpm = s_time / beat_duration
    print('This is your BPM: {}\n'.format(bpm))

    # Beat duration in seconds 
    w_beat  = beat_duration
    h_beat  = 2 * beat_duration
    q_beat  = 4 * beat_duration
    e_beat  = 8 * beat_duration
    s_beat  = 16 * beat_duration
    th_beat = 32 * beat_duration

    print('Seconds duration of whole note: {} seconds'.format(w_beat))
    print('Seconds duration of half note note: {} seconds'.format(h_beat))
    print('Seconds duration of quarter note: {} seconds'.format(q_beat))
    print('Seconds duration of eighth note: {} seconds'.format(e_beat))
    print('Seconds duration of sixteenth note: {} seconds'.format(s_beat))
    print('Seconds duration of thirty-second note: {} seconds'.format(th_beat))

    '''
    Notes per second = (Notes per beat x tempo) / 60
    Task --> Work on the logic more to understand if I am getting the seconds of each
    beat division length or the duration of the beat.
    '''
    user_bpm = float(input("Enter BPM: "))
    bpm_quarter = (1 * user_bpm) / 60
    print('{}'.format(bpm_quarter))
    bpm_eighth = (2 * user_bpm) / 60
    print('{}'.format(bpm_eighth))
    bpm_sixth = (4 * user_bpm) / 60
    print('{}'.format(bpm_sixth))
    bpm_thirty = (8 * user_bpm) / 60
    print('{}'.format(bpm_thirty))

    '''
    Task --> Attempt to use new logic that supports the statement bellow
    As of Dec 8th. Found this resource online about calculating BPM to 
    seconds. 

    To find the length in seconds of each beat for any given metronome 
    marking in beats-per-minute (bpm), you would divide 60 (the number of 
    seconds in a minute) by the bpm marking. For instance, if a piece has 
    a metronome marking of crotchet (quarter-note) = 120, each crotchet beat 
    is 0.5 seconds long (60/120).
    '''

    user_bpm = float(input("Enter BPM: "))
    bpm_seconds = (60/user_bpm)
    print(bpm_seconds)

    '''
    Logic bellow is setup for print a line for x amount of time in seconds.
    Could possibly use this logic to transcribe the BPM into second duration of 
    each beat to make a sound for said each beat

    tstep = datetime.timedelta(seconds=bpm_quarter)
    tnext = datetime.datetime.now() + tstep
        
    while True: 
        print('{} second has passed!'.format(tstep))
        print('Boop')
        tdiff = tnext - datetime.datetime.now()
        time.sleep(tdiff.total_seconds())
        tnext = tnext + tstep
    '''

except Exception as err: 
    print("An error occured --> : {}".format(err))
        