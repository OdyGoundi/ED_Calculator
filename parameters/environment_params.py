# distance from the ground
# population density
# urban, suburban, rural

# based on page. 6 of https://www.anfr.fr/fileadmin/medias/exposition-ondes/2025/2024_Analyse_mesures_2023.pdf

ENVIRONMENT_EMF = {
    "Urban": {
        "outdoor": {
            "900 MHz": 1.2,  # V/m (example GSM)
            "2600 MHz": 0.8, # V/m (example 4G)
            "3500 MHz": 0.5  # V/m (example 5G)
        },
        "indoor": {
            "900 MHz": 0.6,
            "2600 MHz": 0.4,
            "3500 MHz": 0.3
        }
    },
    "SubUrban": { ... },
    "Rural": { ... }
}