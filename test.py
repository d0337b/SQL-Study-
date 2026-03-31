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

cursor.execute(
"""
--sql
WITH customers_summary AS (
    SELECT strftime('%Y-%m', s.order_date) AS order_month,
    c.customer_grade,
    COUNT(s.order_id) AS total_order_count,
    COALESCE(SUM(s.amount),0) AS total_amount,
    SUM(CASE
        WHEN s.amount >= 1000 THEN 1
        ELSE 0
    END) AS high_order_count,

    SUM(CASE
        WHEN s.region = 'Seoul' THEN 1
        ELSE 0
    END) AS seoul_order_count

    FROM customers AS c
    LEFT JOIN sales AS s
    ON c.customer_id = s.customer_id
    GROUP BY order_month, c.customer_grade
)
SELECT order_month, customer_grade, total_order_count, total_amount,
high_order_count, seoul_order_count,

CASE
    WHEN total_amount >= 2000 THEN 'A'
    WHEN total_amount >= 1000 THEN 'B'
    WHEN total_amount >= 1 THEN 'C'
    ELSE 'No Order'
END AS amount_band

FROM customers_summary
WHERE customer_grade IN ('VIP', 'Basic')
GROUP BY order_month, customer_grade
HAVING total_amount >= 100
ORDER BY order_month ASC, customer_grade ASC, total_amount ASC
;
""")
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()