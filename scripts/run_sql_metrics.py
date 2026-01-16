"""
run_sql_metrics.py

Purpose:
- Execute SQL metric queries
- Export results for dashboards
"""

import sqlite3
import pandas as pd
from pathlib import Path


SQL_FILES = {
    "incidents_by_category": "sql/incidents_by_category.sql",
    "incidents_by_priority": "sql/incidents_by_priority.sql",
    "incidents_by_status": "sql/incidents_by_status.sql",
}


if __name__ == "__main__":
    db_path = Path("data/it_operations.db")
    output_dir = Path("data/sql_metrics")

    if not db_path.exists():
        raise FileNotFoundError("Database not found. Run load_to_db.py first.")

    output_dir.mkdir(exist_ok=True)
    conn = sqlite3.connect(db_path)

    for metric_name, sql_file in SQL_FILES.items():
        query = Path(sql_file).read_text()
        df = pd.read_sql_query(query, conn)
        output_file = output_dir / f"{metric_name}.csv"
        df.to_csv(output_file, index=False)
        print(f"Saved SQL metric: {output_file}")

    conn.close()
    print("SQL metrics generation completed.")
