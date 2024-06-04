import sys, signal
import os
import numpy as np
import math
sys.path.append('..')
from functions.frequencies  import calculate_frequency, generate_frequencies
# from functions.notes        import NOT BEING USED JUST YET
from functions.tension_calc import calculate_tension, calculate_guitar_tension

# Number of half steps for each note from A4
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
# Initialize an empty dictionary to store note positions
note_positions = {}

# Use a for loop to populate the dictionary
for pos, note in enumerate(notes):
    note_positions[note] = pos
    
# Print the resulting dictionary
print(note_positions)
octave_offset = 4

# Example: Calculate frequencies from C0 to B8
all_frequencies = generate_frequencies(0, 8, note_positions)
for note, freq in all_frequencies.items():
    print(f'{note}: {freq} Hz')


# Define the scale length in inches (e.g., 25.5 inches for a typical guitar)
scale_length_in_inches = 25.5  # inches

# Define the linear density in pounds per inch (e.g., 0.00028 lb/in for a typical guitar string)
linear_density_in_lb_per_inch = 0.00028  # lb/in

# Use the frequencies dictionary generated previously
all_frequencies = generate_frequencies(0, 8, note_positions)

print('Note/Octive Tenstion in Pounds for in this range\n')
# Calculate and print the tension for each note
tensions = {}
for note, freq in all_frequencies.items():
    tension = calculate_tension(freq, scale_length_in_inches, linear_density_in_lb_per_inch)
    tensions[note] = tension
    print(f'{note}: {tension:.2f} lbs')  # Tension in pounds-force (lbf)

# If you want to return the tensions dictionary as well
# return tensions


'''
All the code above is testing to see if I can just organize the code the best way possible. 
So far it works but the code is hella messy. WILL CLEAN UP! :)

'''

# Function to get user input for scale length and tuning
def get_user_input():
    # Get scale length from the user
    scale_length_in_inches = float(input("Enter the scale length of the guitar in inches (e.g., 25.5): "))

    # Get the tuning for each string from the user
    tuning = []
    for i in range(6):
        note = input(f"Enter the note for string {i+1} (e.g., E2 for the low E string): ")
        tuning.append(note)

    return scale_length_in_inches, tuning

# Main script
if __name__ == "__main__":
    print('User inputed ')
    # Get user input
    scale_length_in_inches, tuning = get_user_input()

    # Define the linear density in pounds per inch (e.g., 0.00028 lb/in for a typical guitar string)
    linear_density_in_lb_per_inch = 0.00028  # lb/in

    # Calculate the guitar tension
    string_tensions, total_tension = calculate_guitar_tension(scale_length_in_inches, tuning, linear_density_in_lb_per_inch)

    # Print the tension for each string and the total tension
    print("\nString Tensions:")
    for note, tension in string_tensions.items():
        print(f'{note}: {tension:.2f} lbs')

    print(f"\nTotal Tension: {total_tension:.2f} lbs")