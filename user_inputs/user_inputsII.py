import ipywidgets as widgets
from IPython.display import display

def create_bmi_ui(height_slider, height_input, weight_slider, weight_input, on_submit_callback):
    """Displays the BMI input UI (height, weight, and submit button)."""
    submit_button = widgets.Button(description="Calculate BMI")
    submit_button.on_click(on_submit_callback)  

    # Display all widgets together to prevent duplication
    display(widgets.VBox([
        widgets.HBox([height_slider, height_input]), 
        widgets.HBox([weight_slider, weight_input]), 
        submit_button
    ]))
