import Calculations
import human_models
import importlib
from IPython.display import display, Image

# Reload utils to ensure latest version
importlib.reload(Calculations)

def run_bmi_calculation(height, weight):
    """Runs the BMI calculation based on provided height and weight."""
    
    bmi = Calculations.calculate_bmi(height, weight)

    # Find the closest human model
    human_mod = human_models.get_human_models()
    closest_model = human_models.find_closest_model(bmi)

    # Get the image path
    image_path = human_mod[closest_model]["Image"]

    print(f"\nYour BMI: {bmi:.2f}")
    print(f"The closest human model to you is: {closest_model}")

    # Display the model image
    display(Image(filename=image_path, width=150))

    return closest_model
