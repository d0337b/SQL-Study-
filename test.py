import sqlite3

conn = sqlite3.connect("practice.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("DROP TABLE IF EXISTS customers")

cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    customer_grade TEXT
)
""")

cursor.execute("""
CREATE TABLE sales (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    region TEXT,
    product TEXT,
    amount INTEGER,
    order_date TEXT
)
""")

customers_data = [
    (101, "Kim", "VIP"),
    (102, "Lee", "Basic"),
    (103, "Park", "Basic"),
    (104, "Choi", "VIP"),
    (105, "Jung", "Basic")
]

sales_data = [
    (1, 101, "Seoul", "Laptop", 1200, "2026-03-01"),
    (2, 102, "Busan", "Mouse", 50, "2026-03-02"),
    (3, 103, "Seoul", "Keyboard", 80, "2026-03-03"),
    (4, 104, "Gwangju", "Monitor", 300, "2026-03-03"),
    (5, 101, "Seoul", "Mouse", 50, "2026-03-05"),
    (6, 102, "Busan", "Laptop", 1300, "2026-03-07"),
    (7, 103, "Seoul", "Monitor", 500, "2026-01-15"),
    (8, 104, "Busan", "Mouse", 70, "2026-02-12")
]

cursor.executemany("""
INSERT INTO customers (customer_id, customer_name, customer_grade)
VALUES (?, ?, ?)
""", customers_data)

cursor.executemany("""
INSERT INTO sales (order_id, customer_id, region, product, amount, order_date)
VALUES (?, ?, ?, ?, ?, ?)
""", sales_data)

conn.commit()

#쿼리 연습때리기

cursor.execute(
"""
--sql
WITH aging_summary AS(
    SELECT c.customer_name, c.customer_grade, c.customer_id,
    COALESCE(SUM(s.amount),0) AS total_amount,
    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 61 THEN s.amount
        ELSE 0
    END) AS total_over_61_plus_amount
    FROM customers AS c
    LEFT JOIN sales AS s
    ON c.customer_id = s.customer_id
    GROUP BY c.customer_name, c.customer_id, c.customer_grade
),
flag_summary AS(
    SELECT customer_grade, total_amount, total_over_61_plus_amount,
    CASE
        WHEN total_over_61_plus_amount > 0 THEN 'Risk'
        ELSE 'Normal'
    END AS risk_flag
    FROM aging_summary
)
SELECT customer_grade, COUNT(*) AS customer_count, SUM(total_amount) AS grade_total_amount,
SUM(total_over_61_plus_amount) AS grade_total_over_61_plus_amount,
SUM(CASE
    WHEN risk_flag = 'Risk' THEN 1
    ELSE 0
END) AS risky_customer_count
FROM flag_summary
GROUP BY customer_grade
;
""")
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()