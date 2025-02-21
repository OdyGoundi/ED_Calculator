import ipywidgets as widgets

def get_height_input():
    """Creates height selection widgets but does not display them."""
    height_slider = widgets.FloatSlider(value=170, min=40, max=220, step=1, description="Height (cm):", continuous_update=False)
    height_input = widgets.FloatText(value=170, description="Manual Input (cm):")
    widgets.jslink((height_slider, 'value'), (height_input, 'value'))
    
    return height_slider, height_input  # Return widgets (no display)

def get_weight_input():
    """Creates weight selection widgets but does not display them."""
    weight_slider = widgets.FloatSlider(value=70, min=5, max=200, step=0.5, description="Weight (kg):", continuous_update=False)
    weight_input = widgets.FloatText(value=70, description="Manual Input (kg):")
    widgets.jslink((weight_slider, 'value'), (weight_input, 'value'))
    
    return weight_slider, weight_input  # Return widgets (no display)
