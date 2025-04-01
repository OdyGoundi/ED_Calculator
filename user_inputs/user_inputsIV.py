import ipywidgets as widgets
from IPython.display import display, clear_output

def create_usage_selection_ui():
    """Creates a UI for selecting usage options and displaying the corresponding image."""
    
     # Define options
    usage_options = ["Non User", "Light User", "Medium User", "Heavy User"]
    
    # Create dropdown widget
    usage_selector = widgets.Dropdown(
        options=usage_options,
        value="Non User",  # Default selection
        description="Usage:",
        style={"description_width": "initial"}
    )
    
    # Output area
    output = widgets.Output()
    
    # Function to handle selection change
    def on_usage_change(change):
        with output:
            clear_output(wait=True)
            print(f"Selected Usage: {change['new']}")  # Display selected option
            
    # Attach event listener
    usage_selector.observe(on_usage_change, names="value")
    
    # Display the selector is an ipynb job
    # Display UI
    display(usage_selector, output)

