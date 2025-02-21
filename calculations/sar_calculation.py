from calculations import Basic_operations 

def run_sar_calculation():
    """Runs the SAR calculation."""
    electric_field_strengths = [1.5, 2.3, 3.1]
    tissue_masses = [0.01, 0.015, 0.02]
    power_densities = [15.0, 25.0, 30.0]

    sar = Basic_operations.calculate_sar(electric_field_strengths, tissue_masses, power_densities)

    # Save result to file
    with open("sar_result.txt", "w") as file:
        file.write(str(sar))
    
    return sar

