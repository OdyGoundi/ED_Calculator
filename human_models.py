def get_human_models():
    """Returns specifications for different human models, including image paths."""
    return {
        "Duke": {
            "Mass": 70.2,
            "Height": 1.77,
            "Age": 34,
            "BMI": 22.4,
            "Image": "images/duke.jpg"
        },
        "Eartha": {
            "Mass": 29.9,
            "Height": 1.36,
            "Age": 8,
            "BMI": 16.2,
            "Image": "images/eartha.jpg"
        },
        "Ella": {
            "Mass": 57.3,
            "Height": 1.63,
            "Age": 26,
            "BMI": 21.6,
            "Image": "images/ella.jpg"
        },
        "Louis": {
            "Mass": 49.7,
            "Height": 1.68,
            "Age": 14,
            "BMI": 17.6,
            "Image": "images/louis.jpg"
        }
    }

def find_closest_model(user_bmi):
    """Finds the human model with the closest BMI to the user."""
    models = get_human_models()
    closest_model = None
    min_diff = float("inf")

    for model, specs in models.items():
        diff = abs(specs["BMI"] - user_bmi)
        if diff < min_diff:
            min_diff = diff
            closest_model = model

    return closest_model
