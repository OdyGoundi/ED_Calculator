import ipywidgets as widgets
from IPython.display import display, clear_output
import calculations.your_BMI as your_BMI

def on_submit_button_clicked(b, height_slider, weight_slider, output):
    """Handles BMI calculation and updates the closest model dynamically."""
    height_m = height_slider.value / 100
    weight = weight_slider.value

    # Calculate closest model from BMI
    closest_model = your_BMI.run_bmi_calculation(height_m, weight)

    import sys
    sys.modules['user_inputs'].selected_model = closest_model

    # Display result
    with output:
        clear_output(wait=True)
        print(f"✅ The closest human model to you is: {closest_model}")

def create_bmi_ui():
    """Creates and displays the BMI UI."""
    height_slider = widgets.FloatSlider(value=170, min=100, max=220, step=1, description="Height (cm):")
    weight_slider = widgets.FloatSlider(value=70, min=30, max=200, step=0.5, description="Weight (kg):")
    submit_button = widgets.Button(description="Calculate BMI")
    output = widgets.Output()

    # Define button action
    submit_button.on_click(lambda b: on_submit_button_clicked(b, height_slider, weight_slider, output))

    # Display everything
    display(widgets.VBox([height_slider, weight_slider, submit_button, output]))
