from calculations.sar_matrix_loader import load_sar_matrix
from parameters.environment_params import ENVIRONMENT_EMF

# Map UI location names to EMF indoor/outdoor categories
location_map = {
    "On the Road": "outdoor",
    "At Work": "indoor",
    "At Home": "indoor",
    "Other Indoor": "indoor",
    "Other Outdoor": "outdoor"
}

def calculate_dose(model, env, time_alloc):
    """Calculate daily dose using SAR data and environment field values."""
    sar_matrix = load_sar_matrix(model=model)
    total_dose = 0

    if env in ENVIRONMENT_EMF:
        for loc, t_hours in time_alloc.items():
            env_type = location_map.get(loc)
            if not env_type:
                print(f"⚠️ Skipping unknown location: {loc}")
                continue

            try:
                freq_field_dict = ENVIRONMENT_EMF[env][env_type]
            except KeyError:
                print(f"⚠️ Environment type '{env_type}' not defined for environment '{env}'")
                continue

            for freq, E in freq_field_dict.items():
                S = E**2 / 377  # Convert E field (V/m) to power density (W/m²)
                for tissue, freq_data in sar_matrix.items():
                    if freq in freq_data:
                        sar = freq_data[freq] * 1e-3  # mW/kg → W/kg
                        dose = sar * S * t_hours * 3600  # J/kg = W/kg × seconds
                        total_dose += dose
                        print(f"{tissue} @ {freq} ({loc}): {dose:.3e} J/kg")
    else:
        print(f"⚠️ Environment '{env}' not found in ENVIRONMENT_EMF.")

    return total_dose

