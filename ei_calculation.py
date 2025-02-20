import Calculations

def run_ei_calculation():
    """Runs the EI calculation with predefined data."""
    T = 3600.0  # Total time in seconds

    dUL = [[0.004, 0.005], [0.003, 0.002]]
    dDL = [[0.003, 0.004], [0.002, 0.001]]
    f = [[0.5, 0.5], [0.6, 0.4]]
    PTX = [[1.0, 0.8], [0.7, 0.6]]
    Sinc = [[0.2, 0.3], [0.1, 0.2]]

    EI = Calculations.calculate_ei(T, dUL, dDL, f, PTX, Sinc)

    # Save result to file for main.ipynb
    with open("ei_result.txt", "w") as file:
        file.write(str(EI))
    
    return EI
