import ipywidgets as widgets
from IPython.display import display, clear_output

# Dictionary mapping environment choices to image paths
environment_images = {
    "Urban": "images/urban.jpg",
    "SubUrban": "images/suburban.jpg",
    "Rural": "images/rural.jpg"
}

# Output widget for displaying the selected environment
output = widgets.Output()

def on_image_click(env):
    """Handles user selection and updates the output."""
    global selected_environment
    selected_environment = env
    
    with output:
        clear_output()  # Clear previous output
        print(f"✅ You selected: {env}")

def create_environment_selector():
    """Creates and displays the environment selection UI."""
    buttons = []

    for env, img_path in environment_images.items():
        btn = widgets.Button(
            description=env,
            tooltip=f"Select {env}",
            layout=widgets.Layout(width="150px", height="150px")
        )

        def on_click(b, env=env):  # Preserve the loop variable
            on_image_click(env)

        btn.on_click(on_click)

        # Read the image file and create an image widget
        img_widget = widgets.Image(value=open(img_path, "rb").read(), format='jpg', width=150, height=150)
        
        buttons.append(widgets.VBox([img_widget, btn]))

    # Display UI
    display(widgets.VBox([
        widgets.Label("📍 Select Your Environment:"),
        widgets.HBox(buttons),
        output
    ]))
