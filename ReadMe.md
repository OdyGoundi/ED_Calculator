# 📡 Exposure Dose Calculator

A Jupyter-based tool to estimate daily absorbed electromagnetic energy dose (J/kg/day) using realistic human models, environmental EMF data, and time-based activity patterns.

---

## ✅ How to Use the Calculator

For now, run it locally in **Jupyter Notebook** using:

- Python 3.10+
- Installed packages:
  - `numpy`
  - `pandas`
  - `ipywidgets`
  - `openpyxl` (for `.xlsx` reading)

> Open `Calculator.ipynb` and run each cell sequentially. Select your BMI, environment, and activity schedule.

---

## 🌐 Colab Integration (Planned)

Target: Each stable version will include a **Google Colab link** so no local setup is required.

---

## 📜 Project Scope and Guidelines 

This calculator is part of a research thesis to model exposure from environmental EMF fields caused by distant sources (e.g., base stations), using simplified but **scientifically grounded rules**:

- Power density is calculated as:  
  $$ S = \frac{E^2}{377} \quad \text{(in W/m²)} $$
- Absorbed dose is:  
  $$ \text{Dose (J/kg)} = \text{SAR (W/kg)} \times S \times t $$

> The tool multiplies per-tissue SAR values with power density and time across multiple activity segments to yield a **daily cumulative exposure**.

Supported scenarios must consider:

- Variability in EM fields based on:
  - Outdoor/indoor location
  - Environment (urban, rural, etc.)
  - Time of day/month
- Realistic user behavior (e.g., child in schoolyard for 3 hours, then at home)
- Predefined human models from the [IT’IS Virtual Population](https://itis.swiss/virtual-population/virtual-population/vip3/)

> Accuracy depends on match between selected BMI and available models. Some estimations are symbolic where data are missing.

---

## ⚠️ Known Scientific and Practical Considerations

1. **BMI ≠ universal**:
   - Especially for infants and very young children, **body mass** may be more representative than BMI.
   - Consider alternative anthropometric markers.

2. **Human models are limited**:
   - Only a subset of standardized IT’IS models (e.g., Duke, Eartha, etc.) are supported.
   - Accuracy drops significantly when target person ≠ model assumptions.

3. **Incomplete environmental data**:
   - If EMF values are missing for specific locations/frequencies, tool may use **simplified estimations or skip** them.

4. **Error estimation not yet implemented**:
   - Future versions may quantify **method + measurement + model uncertainty**.
   - E.g., a Duke-based 24h dose with field data may have ~36% margin of uncertainty.

---

## 💡 Ideas for Future Improvements

- Scenario database with real-world location presets
- Error propagation modeling
- Colab + UI integration
- Dose visualizations per organ/frequency
- User feedback on model applicability

---

## 👨‍🔬 For Developers

Directory layout:
- `calculations/` → Core dose, SAR, EI computation
- `parameters/` → EMF field data and config
- `user_inputs/` → Interactive UI components (BMI, environment, time sliders)
- `data/` → Excel sheets with SAR per frequency
- `images/` → Reference visuals (models, environments)
- `tests/` → Test scripts for validation

---