import sqlite3 

def run_sql_file(file_path):
    print(f"\n ---{file_path} 실행 결과 ---")
    conn = sqlite3.connect("practice.db")
    cursor = conn.cursor()
    with open(file_path, "r", encoding="utf-8") as file:
        query = file.read()

    cursor.execute(query)
    rows = cursor.fetchall() #fetchall()이 다 꺼내오는거임

    for row in rows:
        print(row)

    conn.close()

run_sql_file("sql/01_customer_aging_summary.sql")
run_sql_file("sql/02_grade_risk_summary.sql")