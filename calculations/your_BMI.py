from calculations import Basic_operations
import human_models
import importlib
from IPython.display import display, Image

# Reload Calculations to ensure latest version
importlib.reload(Basic_operations)

def run_bmi_calculation(height, weight):
    """Runs the BMI calculation based on provided height and weight."""
    
    bmi = Basic_operations.calculate_bmi(height, weight)

    # Find the closest human model
    closest_model = human_models.find_closest_model(bmi)

    # Get the image path
    human_mod = human_models.get_human_models()
    image_path = human_mod[closest_model]["Image"]

    # ✅ Print message for debugging
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"✅ The closest human model to you is: {closest_model} (BMI: {human_mod[closest_model]['BMI']})")

    # ✅ Display the model image
    display(Image(filename=image_path, width=150))

    return closest_model  # ✅ Ensure it returns the closest model

