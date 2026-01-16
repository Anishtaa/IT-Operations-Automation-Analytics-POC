"""
generate_metrics.py

Purpose:
- Generate core operational metrics from cleaned incident data
- Identify recurring issues and efficiency indicators
- Produce summary tables for dashboards
"""

import pandas as pd
from pathlib import Path


def generate_metrics(df: pd.DataFrame) -> dict:
    """
    Generates key operational metrics.
    Returns a dictionary of summary DataFrames.
    """
    metrics = {}

    # Incident count by category
    if "category" in df.columns:
        metrics["incidents_by_category"] = (
            df.groupby("category")
            .size()
            .reset_index(name="incident_count")
            .sort_values(by="incident_count", ascending=False)
        )

    # Incident count by priority
    if "priority" in df.columns:
        metrics["incidents_by_priority"] = (
            df.groupby("priority")
            .size()
            .reset_index(name="incident_count")
            .sort_values(by="incident_count", ascending=False)
        )

    # Incident status distribution
    if "incident_state" in df.columns:
        metrics["incidents_by_status"] = (
            df.groupby("incident_state")
            .size()
            .reset_index(name="incident_count")
            .sort_values(by="incident_count", ascending=False)
        )

    return metrics


if __name__ == "__main__":
    input_path = Path("data/incident_event_log_cleaned.csv")
    output_dir = Path("data/metrics")

    if not input_path.exists():
        raise FileNotFoundError("Cleaned dataset not found. Run clean_data.py first.")

    output_dir.mkdir(exist_ok=True)

    df = pd.read_csv(input_path)
    metrics = generate_metrics(df)

    for name, metric_df in metrics.items():
        output_file = output_dir / f"{name}.csv"
        metric_df.to_csv(output_file, index=False)
        print(f"Saved metric: {output_file}")

    print("Metric generation completed.")
