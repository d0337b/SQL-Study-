WITH customer_summary AS(
    SELECT c.customer_name, c.customer_grade, c.customer_id,
    COALESCE(SUM(s.amount),0) AS total_amount,

    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 61 AND
        julianday('2026-04-02') - julianday(s.order_date) <=90 THEN s.amount
        ELSE 0
    END) AS over_61_90_amount,

    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 91 THEN s.amount
        ELSE 0
    END) AS over_91_plus_amount,
    
    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 61 THEN s.amount
        ELSE 0
    END) AS over_61_total_amount
    
    FROM customers AS c
    LEFT JOIN sales AS s
    ON c.customer_id = s.customer_id
    GROUP BY c.customer_name, c.customer_grade, c.customer_id
)
SELECT customer_name, customer_grade, total_amount, over_61_90_amount, over_91_plus_amount,
over_61_total_amount,
CASE
    WHEN total_amount = 0 then 0
    ELSE CAST(over_61_total_amount AS REAL) / total_amount
END AS risk_ratio
FROM customer_summary
WHERE over_61_total_amount > 0
ORDER BY risk_ratio DESC, total_amount DESC, customer_name ASC
;