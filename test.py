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
    (104, "Choi", "VIP")
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
query = """ SELECT c.customer_grade, AVG(s.amount) AS average_amount
FROM sales AS s
JOIN customers AS c
ON s.customer_id = c.customer_id
GROUP BY c.customer_grade
HAVING average_amount >= 300
ORDER BY average_amount DESC
"""

cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()