import Calculations
import importlib
from IPython.display import display, Image

# Reload utils to ensure latest version
importlib.reload(Calculations)

def run_bmi_calculation(height, weight):
    """Runs the BMI calculation based on provided height and weight."""
    
    bmi = Calculations.calculate_bmi(height, weight)

    # Find the closest human model
    human_models = Calculations.human_models_specifications()
    closest_model = Calculations.closest_bmi(human_models, bmi)

    # Get the image path
    image_path = human_models[closest_model]["Image"]

    print(f"\nYour BMI: {bmi:.2f}")
    print(f"The closest human model to you is: {closest_model}")

    # Display the model image
    display(Image(filename=image_path, width=150))

    return closest_model
