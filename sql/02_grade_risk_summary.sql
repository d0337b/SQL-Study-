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