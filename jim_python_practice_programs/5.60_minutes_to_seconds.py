# Write a program that converts minutes to seconds

def minutestoseconds():
# get an input integer
    time_minutes = int(input('Enter how many minutes you want to convert into seconds: '))

# convert time_minutes into second
    time_seconds = time_minutes * 60

# print the result
    print(f"{time_minutes} minutes is equal to {time_seconds} seconds.")

minutestoseconds()