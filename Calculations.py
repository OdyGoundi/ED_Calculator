import numpy as np

def calculate_ei(T, dUL, dDL, f, PTX, Sinc):
    """Calculate the Exposure Index (EI)."""
    EI = np.sum(np.array(f) * (np.array(dUL) * np.array(PTX) + np.array(dDL) * np.array(Sinc))) 
    return EI / T  # Normalize by total time

def calculate_daily_dose(EI, T):
    """Calculate the daily dose from EI."""
    seconds_per_day = 86400  # Total seconds in a day
    return EI * seconds_per_day / T

def calculate_bmi(height, weight):
    """Calculate the BMI given height (in meters) and weight (in kg)."""
    return weight / (height ** 2)


def calculate_sar(electric_field_strengths, tissue_masses, power_densities):
    """Calculate Specific Absorption Rate (SAR)."""
    if len(electric_field_strengths) != len(tissue_masses) or len(tissue_masses) != len(power_densities):
        raise ValueError("Input data dimensions do not match!")
    
    sar_values = (np.array(power_densities) / np.array(tissue_masses)) * (np.array(electric_field_strengths) ** 2)
    return np.mean(sar_values)  # Return average SAR

