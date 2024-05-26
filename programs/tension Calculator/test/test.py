import numpy as np

# Reference note A4
A4_frequency = 440.0

# Number of half steps for each note from A4
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
note_positions = {note: pos for pos, note in enumerate(notes)}
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

# Example: Calculate frequencies from C0 to B8
all_frequencies = generate_frequencies(0, 8)
for note, freq in all_frequencies.items():
    print(f'{note}: {freq} Hz')
t