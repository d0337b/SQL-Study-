import sqlite3

def run_sql_file(sql_path):
    conn = sqlite3.connect("practice.db")
    cursor = conn.cursor()
    
    with open(sql_path, "r", encoding="utf-8") as file:
        query = file.read()
    
    cursor.execute(query)

    # 컬럼명 보기
    columns = [desc[0] for desc in cursor.description]
    print("\n[columns]")
    print(columns)

    # 결과 보기
    rows = cursor.fetchall()
    print("\n[rows]")
    for row in rows:
        print(row)
    
    conn.close()

def main():
    run_sql_file("sql/02_grade_risk_summary.sql")

if __name__ == "__main__":
    main()