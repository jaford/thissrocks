# Function to calculate the frequency of a given note
def calculate_frequency(note, octave, note_positions):
    # Reference note A4
    A4_frequency = 440.0
    
    # Calculate number of half steps from A4
    n = note_positions[note] - note_positions['A'] + 12 * (octave - 4)
    return A4_frequency * (2 ** (n / 12))

# Generate frequencies for notes in a given range
def generate_frequencies(start_octave, end_octave, note_positions):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    frequencies = {}
    for octave in range(start_octave, end_octave + 1):
        for note in notes:
            freq = calculate_frequency(note, octave, note_positions)
            frequencies[f'{note}{octave}'] = round(freq, 2)
    return frequencies