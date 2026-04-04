import sqlite3

DB_PATH = "practice.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 기존 테이블 삭제
cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("DROP TABLE IF EXISTS customers")

# 새 테이블 생성
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    customer_grade TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE sales (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    region TEXT NOT NULL,
    product TEXT NOT NULL,
    amount INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

# 고객 데이터
customers_data = [
    (101, "Kim", "VIP"),
    (102, "Lee", "VIP"),
    (103, "Park", "VIP"),
    (104, "Choi", "VIP"),
    (105, "Jung", "VIP"),
    (106, "Han", "VIP"),
    (107, "Kang", "Basic"),
    (108, "Cho", "Basic"),
    (109, "Yoon", "Basic"),
    (110, "Jang", "Basic"),
    (111, "Lim", "Basic"),
    (112, "Shin", "Basic"),
    (113, "Oh", "Basic"),
    (114, "Seo", "Basic"),
    (115, "Hwang", "Basic"),
    (116, "Song", "Basic"),
    (117, "Ryu", "Basic"),
    (118, "Baek", "Basic"),
]

cursor.executemany("""
INSERT INTO customers (customer_id, customer_name, customer_grade)
VALUES (?, ?, ?)
""", customers_data)

sales_data = []

def add_sale(customer_id, region, product, amount, order_date):
    order_id = len(sales_data) + 1
    sales_data.append((order_id, customer_id, region, product, amount, order_date))


# 101 Kim - VIP, 총액 큼 / 저위험
add_sale(101, "Seoul", "Laptop", 2200, "2026-03-28")
add_sale(101, "Seoul", "Monitor", 900, "2026-03-18")
add_sale(101, "Seoul", "Mouse", 150, "2026-02-20")
add_sale(101, "Seoul", "Keyboard", 180, "2026-01-20")

# 102 Lee - VIP, 고위험
add_sale(102, "Busan", "Server", 3000, "2025-12-10")
add_sale(102, "Busan", "Laptop", 1400, "2026-01-10")
add_sale(102, "Busan", "Mouse", 80, "2026-03-12")
add_sale(102, "Busan", "Monitor", 700, "2026-02-15")

# 103 Park - VIP, 혼합형 고위험
add_sale(103, "Seoul", "Printer", 600, "2026-03-22")
add_sale(103, "Seoul", "Monitor", 750, "2026-02-25")
add_sale(103, "Seoul", "Laptop", 1200, "2025-12-28")
add_sale(103, "Seoul", "SSD", 350, "2026-01-25")

# 104 Choi - VIP, 정상
add_sale(104, "Gwangju", "Laptop", 1800, "2026-03-27")
add_sale(104, "Gwangju", "Keyboard", 200, "2026-03-10")
add_sale(104, "Gwangju", "Monitor", 650, "2026-02-28")

# 105 Jung - VIP, 31~60 중심
add_sale(105, "Daegu", "Printer", 500, "2026-02-12")
add_sale(105, "Daegu", "Mouse", 60, "2026-02-20")
add_sale(105, "Daegu", "Keyboard", 140, "2026-03-01")

# 106 Han - VIP, 총액 큼 / 정상
add_sale(106, "Seoul", "Server", 3500, "2026-03-29")
add_sale(106, "Seoul", "Monitor", 1100, "2026-03-14")
add_sale(106, "Seoul", "Laptop", 1700, "2026-02-18")
add_sale(106, "Seoul", "SSD", 400, "2026-03-05")

# 107 Kang - Basic, 심한 고위험
add_sale(107, "Busan", "Mouse", 70, "2025-12-05")
add_sale(107, "Busan", "Keyboard", 120, "2025-12-22")
add_sale(107, "Busan", "Monitor", 450, "2026-01-18")
add_sale(107, "Busan", "Laptop", 900, "2026-03-25")

# 108 Cho - Basic, 정상
add_sale(108, "Seoul", "Mouse", 50, "2026-03-30")
add_sale(108, "Seoul", "Keyboard", 130, "2026-03-20")
add_sale(108, "Seoul", "Headset", 220, "2026-03-07")

# 109 Yoon - Basic, 61~90 포함
add_sale(109, "Incheon", "Monitor", 500, "2026-01-30")
add_sale(109, "Incheon", "Mouse", 60, "2026-02-25")
add_sale(109, "Incheon", "Laptop", 1000, "2026-03-26")

# 110 Jang - Basic, 소액 고위험
add_sale(110, "Daejeon", "Printer", 300, "2025-12-20")
add_sale(110, "Daejeon", "Mouse", 40, "2026-03-28")
add_sale(110, "Daejeon", "Keyboard", 90, "2026-03-15")

# 111 Lim - Basic, 혼합형 정상
add_sale(111, "Seoul", "Laptop", 1200, "2026-03-29")
add_sale(111, "Seoul", "Monitor", 600, "2026-02-22")
add_sale(111, "Seoul", "Mouse", 80, "2026-02-10")

# 112 Shin - Basic, 91+ 포함 고위험
add_sale(112, "Gwangju", "Monitor", 700, "2025-11-28")
add_sale(112, "Gwangju", "SSD", 250, "2026-01-12")
add_sale(112, "Gwangju", "Mouse", 60, "2026-03-19")

# 113 Oh - Basic, 31~60 중심
add_sale(113, "Daegu", "Printer", 450, "2026-02-05")
add_sale(113, "Daegu", "Keyboard", 120, "2026-02-27")
add_sale(113, "Daegu", "Mouse", 50, "2026-03-01")

# 114 Seo - Basic, 총액 큼 / 저위험
add_sale(114, "Busan", "Server", 2800, "2026-03-31")
add_sale(114, "Busan", "Laptop", 1600, "2026-03-11")
add_sale(114, "Busan", "Monitor", 900, "2026-02-26")
add_sale(114, "Busan", "SSD", 300, "2026-01-22")

# 115 Hwang - Basic, 정상
add_sale(115, "Seoul", "Laptop", 1300, "2026-03-17")
add_sale(115, "Seoul", "Monitor", 650, "2026-03-04")
add_sale(115, "Seoul", "Mouse", 70, "2026-03-29")

# 116 Song - Basic, 고위험
add_sale(116, "Incheon", "Printer", 550, "2026-01-08")
add_sale(116, "Incheon", "Keyboard", 150, "2025-12-30")
add_sale(116, "Incheon", "Monitor", 650, "2026-02-18")
add_sale(116, "Incheon", "Mouse", 60, "2026-03-24")

# 117 Ryu - Basic, 주문 없음
# 118 Baek - Basic, 주문 없음

cursor.executemany("""
INSERT INTO sales (order_id, customer_id, region, product, amount, order_date)
VALUES (?, ?, ?, ?, ?, ?)
""", sales_data)

conn.commit()

customer_count = cursor.execute("SELECT COUNT(*) FROM customers").fetchone()[0]
sales_count = cursor.execute("SELECT COUNT(*) FROM sales").fetchone()[0]

print(f"customers rows: {customer_count}")
print(f"sales rows: {sales_count}")
print("practice.db setup complete")

conn.close()