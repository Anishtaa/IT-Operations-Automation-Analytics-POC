"""
load_data.py

Purpose:
- Load IT incident event log data
- Perform basic inspection
- Entry point for analytics automation (POC)
"""

import pandas as pd
from pathlib import Path


def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Loads a CSV dataset and returns a pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df


def inspect_dataset(df: pd.DataFrame) -> None:
    """
    Prints basic dataset information for quick inspection.
    """
    print("\nDataset Preview:")
    print(df.head())

    print("\nDataset Shape (rows, columns):")
    print(df.shape)

    print("\nDataset Info:")
    print(df.info())

    print("\nMissing Values (top 10):")
    print(df.isnull().sum().sort_values(ascending=False).head(10))


if __name__ == "__main__":
    data_path = Path("data/incident_event_log.csv")

    if data_path.exists():
        data = load_dataset(data_path)
        inspect_dataset(data)
    else:
        print(
            "Dataset not found.\n"
            "Please place 'incident_event_log.csv' inside the data/ folder."
        )
