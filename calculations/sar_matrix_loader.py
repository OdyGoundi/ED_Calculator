import pandas as pd

def load_sar_matrix(*, file_path="data/FF-DL.xlsx", model="Eartha"):
    try:
        # Row 1 = metadata, Row 2 = "Frequency (MHz)", Row 3 = real header
        df = pd.read_excel(file_path, sheet_name=model, skiprows=2, header=0)

        # Rename columns to readable names
        df.rename(columns={
            df.columns[0]: "Organ",
            df.columns[1]: "900 MHz",
            df.columns[2]: "1800 MHz",
            df.columns[3]: "2600 MHz",
            df.columns[4]: "3500 MHz",
            df.columns[5]: "5500 MHz",
        }, inplace=True)

    except FileNotFoundError:
        raise FileNotFoundError(f"Excel file not found at: {file_path}")
    except ValueError:
        raise ValueError(f"Model '{model}' not found as a sheet in '{file_path}'")

    print("✅ Loaded columns:", df.columns.tolist())  # Just to verify

    sar_data = {}
    for _, row in df.iterrows():
        tissue = row["Organ"]
        sar_data[tissue] = {
            "900 MHz": row["900 MHz"],
            "1800 MHz": row["1800 MHz"],
            "2600 MHz": row["2600 MHz"],
            "3500 MHz": row["3500 MHz"],
            "5500 MHz": row["5500 MHz"]
        }

    return sar_data
