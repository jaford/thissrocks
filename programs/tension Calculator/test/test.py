import numpy as np
import math

# Reference note A4
A4_frequency = 440.0

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

# Function to calculate the frequency of a given note
def calculate_frequency(note, octave):
    # Calculate number of half steps from A4
    n = note_positions[note] - note_positions['A'] + 12 * (octave - 4)
    return A4_frequency * (2 ** (n / 12))

# Generate frequencies for notes in a given range
def generate_frequencies(start_octave, end_octave):
    frequencies = {}
    for octave in range(start_octave, end_octave + 1):
        for note in notes:
            freq = calculate_frequency(note, octave)
            frequencies[f'{note}{octave}'] = round(freq, 2)
    return frequencies

# Define the function to calculate string tension
def calculate_tension(frequency, scale_length_in_inches, linear_density_in_lb_per_inch):
    
    gravitational_acceleration = 9.80665
    # Convert scale length from inches to meters
    scale_length_in_meters = scale_length_in_inches * 0.0254
    
    # Convert linear density from pounds per inch to kilograms per meter
    linear_density_in_kg_per_meter = linear_density_in_lb_per_inch * 17.857
    
    # Calculate tension using the provided formula
    tension = (frequency * 2 * scale_length_in_meters) ** 2 * gravitational_acceleration * linear_density_in_kg_per_meter
    
    # Convert tension from Newtons to pounds-force
    tension_in_pounds = tension_in_newtons * 0.224809
    
    return tension

# Example: Calculate frequencies from C0 to B8
all_frequencies = generate_frequencies(0, 8)
for note, freq in all_frequencies.items():
    print(f'{note}: {freq} Hz')

# Example usage
# Define the scale length in inches (e.g., 25.5 inches for a typical guitar)
scale_length_in_inches = 25.5  # inches

# Define the linear density in pounds per inch (e.g., 0.00028 lb/in for a typical guitar string)
linear_density_in_lb_per_inch = 0.00028  # lb/in

# Use the frequencies dictionary generated previously
all_frequencies = generate_frequencies(0, 8)

# Calculate and print the tension for each note
tensions = {}
for note, freq in all_frequencies.items():
    tension = calculate_tension(freq, scale_length_in_inches, linear_density_in_lb_per_inch)
    tensions[note] = tension
    print(f'{note}: {tension:.2f} lbs')  # Tension in pounds-force (lbf)

# If you want to return the tensions dictionary as well
# return tensions