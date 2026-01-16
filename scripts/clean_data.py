"""
clean_data.py

Purpose:
- Clean and standardize IT incident event log data
- Prepare dataset for analytics and dashboards
"""

import pandas as pd
from pathlib import Path


def clean_incident_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the incident event log dataset.
    """
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Drop completely empty rows
    df = df.dropna(how="all")

    # Handle missing values (basic strategy)
    if "incident_state" in df.columns:
        df["incident_state"] = df["incident_state"].fillna("Unknown")

    # Remove duplicates if any
    df = df.drop_duplicates()

    return df


if __name__ == "__main__":
    input_path = Path("data/incident_event_log.csv")
    output_path = Path("data/incident_event_log_cleaned.csv")

    if not input_path.exists():
        raise FileNotFoundError("Input dataset not found in data/ folder")

    df_raw = pd.read_csv(input_path)
    df_cleaned = clean_incident_data(df_raw)

    df_cleaned.to_csv(output_path, index=False)

    print("Data cleaning completed.")
    print(f"Cleaned dataset saved to: {output_path}")
