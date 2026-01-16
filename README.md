# IT Operations Automation & Analytics POC

## Overview
This project is a **proof-of-concept (POC)** designed to demonstrate how operational IT incident data can be **automatically cleaned, analyzed, and transformed into actionable metrics** to support data-driven decision-making.

The project simulates a real-world IT operations analytics workflow using Python, SQL, and Power BI-ready outputs.

---

## Objectives
- Analyze IT incident event logs to identify **recurring issues and trends**
- Automate **data cleaning, preprocessing, and metric generation**
- Generate **operational performance summaries** using both Python and SQL
- Prepare structured outputs suitable for **dashboarding and reporting**

---

## Tech Stack
- **Programming Language:** Python  
- **Data Analysis:** Pandas  
- **Database:** SQLite (via Python `sqlite3`)  
- **Query Language:** SQL  
- **Visualization:** Power BI  
- **Version Control:** Git & GitHub  
- **IDE:** VS Code  

---

## Project Structure
IT-Operations-Automation-Analytics-POC/
│
├── data/
│ ├── incident_event_log.csv
│ ├── incident_event_log_cleaned.csv
│ ├── it_operations.db
│ ├── metrics/
│ └── sql_metrics/
│
├── scripts/
│ ├── load_data.py
│ ├── clean_data.py
│ ├── generate_metrics.py
│ ├── load_to_db.py
│ └── run_sql_metrics.py
│
├── sql/
│ ├── incidents_by_category.sql
│ ├── incidents_by_priority.sql
│ └── incidents_by_status.sql
│
├── dashboards/
├── reports/
├── requirements.txt
├── .gitignore
└── README.md

markdown
Copy code

---

## Dataset
- **Type:** IT Incident / Event Log Dataset  
- **Format:** CSV  
- **Description:** ServiceNow-style incident management records containing incident categories, priorities, states, and lifecycle information.  
- **Usage:** Used to simulate real-world IT operations analytics scenarios.

---

## Workflow
1. **Data Loading & Inspection**
   - Load raw incident data
   - Inspect schema, size, and missing values

2. **Data Cleaning & Preprocessing**
   - Standardize column names
   - Handle missing values
   - Remove duplicates
   - Export cleaned dataset

3. **Metric Generation (Python)**
   - Incident counts by category
   - Incident counts by priority
   - Incident status distribution

4. **SQL-Based Analytics**
   - Load cleaned data into SQLite
   - Execute SQL queries for operational metrics
   - Export SQL-derived summaries

5. **Dashboard Preparation**
   - Generate CSV outputs ready for Power BI dashboards

---

## How to Run the Project

### 1. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run data pipeline
bash
Copy code
python scripts/load_data.py
python scripts/clean_data.py
python scripts/generate_metrics.py
python scripts/load_to_db.py
python scripts/run_sql_metrics.py
Key Outcomes
Automated IT incident data preprocessing pipeline

Python and SQL-based operational metrics generation

Clean, structured outputs for dashboarding

Modular, reproducible analytics workflow

Future Enhancements
Resolution time and SLA analysis

Trend analysis over time

Advanced Power BI dashboards

Integration with live databases or APIs