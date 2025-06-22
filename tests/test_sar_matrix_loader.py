from calculations.sar_matrix_loader import load_sar_matrix

def test_model_sar_structure():
    model = "Eartha"
    sar = load_sar_matrix(model=model)

    assert isinstance(sar, dict), "SAR matrix should be a dictionary"
    assert "Brain" in sar, "Expected tissue 'Brain' in SAR matrix"
    assert "900 MHz" in sar["Brain"], "Expected frequency key in tissue SAR data"
    assert isinstance(sar["Brain"]["900 MHz"], (float, int)), "SAR value should be a number"

    print(f"✅ {model}/Brain/900 MHz = {sar['Brain']['900 MHz']} mW/kg per W/m²")

def test_all_model_names():
    for model in ["Eartha", "Ella", "Duke", "Louis"]:
        sar = load_sar_matrix(model=model)
        assert "Brain" in sar, f"{model} missing 'Brain' tissue"
        assert "1800 MHz" in sar["Brain"], f"{model}/Brain missing frequency 1800 MHz"
    print("✅ All models loaded successfully and structured correctly.")

if __name__ == "__main__":
    test_model_sar_structure()
    test_all_model_names()