from calculations import Basic_operations


def run_dose_calculation():
    """Runs the dose calculation based on EI."""
    # Read EI from file
    with open("ei_result.txt", "r") as file:
        EI = float(file.read())

    T = 3600.0  # Same time as before

    daily_dose = Basic_operations.calculate_daily_dose(EI, T)

    # Save result to file
    with open("dose_result.txt", "w") as file:
        file.write(str(daily_dose))
    
    return daily_dose
