def calculate_environmental_dose(sar_table, E_field_dict, time_allocation_dict):
    """
    Args:
        sar_table: dict[tissue][frequency] = SAR per W/m²
        E_field_dict: dict[location][frequency] = E [V/m]
        time_allocation_dict: dict[location] = time in hours

    Returns:
        dict[tissue] = dose in J/kg/day
    """
    results = {}
    for tissue in sar_table:
        total_dose = 0
        for location in time_allocation_dict:
            time_h = time_allocation_dict[location]
            time_sec = time_h * 3600

            for freq, E in E_field_dict[location].items():
                S = (E ** 2) / 377  # W/m²
                SAR = sar_table[tissue][freq] / 1000  # convert mW to W
                dose = SAR * S * time_sec  # J/kg
                total_dose += dose

        results[tissue] = total_dose
    return results
