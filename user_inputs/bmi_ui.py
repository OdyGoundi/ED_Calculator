import ipywidgets as widgets
from IPython.display import display, clear_output
import calculations.your_BMI as your_BMI

def on_submit_button_clicked(b, height_slider, weight_slider, output):
    """Handles BMI calculation and updates the closest model dynamically."""
    height_m = height_slider.value / 100  # Convert cm to meters
    weight = weight_slider.value

    # Get closest model (which already displays the image)
    closest_model = your_BMI.run_bmi_calculation(height_m, weight)

    # Display output dynamically
    with output:
        clear_output(wait=True)  # Clear previous output
        print(f"✅ The closest human model to you is: {closest_model}")

def create_bmi_ui():
    """Creates and displays the BMI UI."""
    height_slider = widgets.FloatSlider(value=170, min=100, max=220, step=1, description="Height (cm):")
    weight_slider = widgets.FloatSlider(value=70, min=30, max=200, step=0.5, description="Weight (kg):")
    submit_button = widgets.Button(description="Calculate BMI")
    output = widgets.Output()

    submit_button.on_click(lambda b: on_submit_button_clicked(b, height_slider, weight_slider, output))

    display(widgets.VBox([height_slider, weight_slider, submit_button, output]))
