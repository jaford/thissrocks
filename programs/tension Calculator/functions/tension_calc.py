# Define the function to calculate string tension
def calculate_tension(frequency, scale_length_in_inches, linear_density_in_lb_per_inch):
    
    gravitational_acceleration = 9.80665
    # Convert scale length from inches to meters
    scale_length_in_meters = scale_length_in_inches * 0.0254
    
    # Convert linear density from pounds per inch to kilograms per meter
    linear_density_in_kg_per_meter = linear_density_in_lb_per_inch * 17.857
    
    # Calculate tension using the provided formula
    tension_in_newtons = (frequency * 2 * scale_length_in_meters) ** 2 * gravitational_acceleration * linear_density_in_kg_per_meter
    
    # Convert tension from Newtons to pounds-force
    tension_in_pounds = tension_in_newtons * 0.224809
    
    return tension_in_pounds

# Function to calculate the total tension of the guitar
def calculate_guitar_tension(scale_length_in_inches, tuning, linear_density_in_lb_per_inch):
    total_tension = 0
    string_tensions = {}

    for note in tuning:
        freq = all_frequencies[note]
        tension = calculate_tension(freq, scale_length_in_inches, linear_density_in_lb_per_inch)
        string_tensions[note] = tension
        total_tension += tension

    return string_tensions, total_tension