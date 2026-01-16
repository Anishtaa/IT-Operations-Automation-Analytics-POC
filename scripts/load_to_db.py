"""
load_to_db.py

Purpose:
- Load cleaned incident data into SQLite database
- Enable SQL-based analytics
"""

import sqlite3
import pandas as pd
from pathlib import Path


if __name__ == "__main__":
    data_path = Path("data/incident_event_log_cleaned.csv")
    db_path = Path("data/it_operations.db")

    if not data_path.exists():
        raise FileNotFoundError("Cleaned dataset not found. Run clean_data.py first.")

    df = pd.read_csv(data_path)

    # Create SQLite connection
    conn = sqlite3.connect(db_path)

    # Load data into SQL table
    df.to_sql("incident_events", conn, if_exists="replace", index=False)

    conn.close()

    print("Cleaned data successfully loaded into SQLite database.")
