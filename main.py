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
    (6, 102, "Busan", "Laptop", 1300, "2026-03-07")
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
query = """
--sql
SELECT c.customer_grade,
    SUM(CASE
        WHEN s.amount >= 1000 THEN 1
        ELSE 0
    END) AS high_order_count,

    SUM(CASE
        WHEN s.amount < 1000 THEN 1
        ELSE 0
    END) AS non_high_order_count,

COALESCE(SUM(s.amount),0) AS total_amount
FROM sales AS s
JOIN customers AS c
ON c.customer_id = s.customer_id
GROUP BY c.customer_grade
ORDER BY total_amount DESC
;
"""

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()