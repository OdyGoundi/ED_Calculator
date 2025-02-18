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

def human_models_specifications():
    """Return the specifications of the human models, including images."""
    return {
        "Duke": {
            "Mass": 70.2,
            "Height": 1.77,
            "Age": 34,
            "BMI": 22.4,
            "Image": "images/duke.jpg"
        },
        "Eartha": {
            "Mass": 29.9,
            "Height": 1.36,
            "Age": 8,
            "BMI": 16.2,
            "Image": "images/eartha.jpg"
        },
        "Ella": {
            "Mass": 57.3,
            "Height": 1.63,
            "Age": 26,
            "BMI": 21.6,
            "Image": "images/ella.jpg"
        },
        "Louis": {
            "Mass": 49.7,
            "Height": 1.68,
            "Age": 14,
            "BMI": 17.6,
            "Image": "images/louis.jpg"
        }
    }


def closest_bmi(human_models, BMI):
    """Return the human model with the closest BMI to the given BMI."""
    closest_model = None
    min_diff = float("inf")
    
    for model, specs in human_models.items():
        diff = abs(specs["BMI"] - BMI)
        if diff < min_diff:
            min_diff = diff
            closest_model = model
    
    return closest_model

def calculate_sar(electric_field_strengths, tissue_masses, power_densities):
    """Calculate Specific Absorption Rate (SAR)."""
    if len(electric_field_strengths) != len(tissue_masses) or len(tissue_masses) != len(power_densities):
        raise ValueError("Input data dimensions do not match!")
    
    sar_values = (np.array(power_densities) / np.array(tissue_masses)) * (np.array(electric_field_strengths) ** 2)
    return np.mean(sar_values)  # Return average SAR

