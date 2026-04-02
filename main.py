import sqlite3 
import pandas as pd
import os

os.makedirs("output", exist_ok=True)

def save_sql_to_csv(sql_path, csv_path):
    conn = sqlite3.connect("practice.db")
    with open(sql_path, "r", encoding="utf-8") as file:
        query = file.read()

    df = pd.read_sql_query(query, conn)
    df.to_csv(csv_path, index=False)
    print(f"Saved: {csv_path}")
    conn.close()

save_sql_to_csv("sql/01_customer_aging_summary.sql", "output/customer_aging_summary.csv")
save_sql_to_csv("sql/02_grade_risk_summary.sql", "output/grade_risk_summary.csv")
save_sql_to_csv("sql/03_high_risk_customers.sql", "output/high_risk_customers.csv")