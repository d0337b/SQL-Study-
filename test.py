import sqlite3

conn = sqlite3.connect("practice.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    customer TEXT,
    region TEXT,
    product TEXT,
    amount INTEGER,
    order_date TEXT
)
""")

cursor.execute("DELETE FROM sales")

sales_data = [
    (1, "Kim", "Seoul", "Laptop", 1200, "2026-03-01"),
    (2, "Lee", "Busan", "Mouse", 50, "2026-03-02"),
    (3, "Park", "Seoul", "Keyboard", 80, "2026-03-03"),
    (4, "Choi", "Gwangju", "Monitor", 300, "2026-03-03"),
    (5, "Kim", "Seoul", "Mouse", 50, "2026-03-05"),
    (6, "Lee", "Busan", "Laptop", 1300, "2026-03-07")
]

cursor.executemany("""
INSERT INTO sales (order_id, customer, region, product, amount, order_date)
VALUES (?, ?, ?, ?, ?, ?)
""", sales_data)

conn.commit()

cursor.execute("SELECT region, COUNT(*) FROM sales GROUP BY region")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()