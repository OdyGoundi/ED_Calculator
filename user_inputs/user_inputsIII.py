import ipywidgets as widgets
from IPython.display import display, clear_output

def create_time_sliders():
    """Creates simple sliders for time allocation across different locations, ensuring total = 24 hours."""

    # Locations and initial values
    locations = ["On the Road", "At Work", "At Home", "Other Indoor", "Other Outdoor"]
    initial_values = [2, 8, 10, 2, 2]
    total_time = 24

    # Create sliders
    sliders = {
        loc: widgets.FloatSlider(value=initial_values[i], min=0, max=24, step=0.5, description=loc, continuous_update=False)
        for i, loc in enumerate(locations)
    }

    output = widgets.Output()

    def adjust_sliders(changed_slider_index):
        """Adjusts only the sliders below the changed one while maintaining a total of 24 hours."""
        remaining_time = total_time
        for i in range(changed_slider_index + 1):
            remaining_time -= sliders[locations[i]].value  # Keep earlier sliders fixed

        remaining_sliders = locations[changed_slider_index + 1:]  # Only adjust later sliders
        remaining_sum = sum(sliders[loc].value for loc in remaining_sliders)

        if remaining_sum > 0:
            for loc in remaining_sliders:
                sliders[loc].unobserve_all()  # Prevent loop
                sliders[loc].value = (sliders[loc].value / remaining_sum) * remaining_time
                sliders[loc].observe(lambda change, idx=locations.index(loc): adjust_sliders(idx), names='value')  # Re-enable

        update_output()

    def update_output():
        """Updates the displayed time allocation summary."""
        with output:
            clear_output(wait=True)
            print(f"Total Hours Assigned: {sum(sliders[loc].value for loc in locations):.1f} / 24")
            for loc in locations:
                print(f"{loc}: {sliders[loc].value:.1f} hours")

    # Attach event listeners
    for i, loc in enumerate(locations):
        sliders[loc].observe(lambda change, idx=i: adjust_sliders(idx), names='value')

    # Display sliders and output
    display(widgets.VBox(list(sliders.values()) + [output]))

    update_output()  # Show initial values

