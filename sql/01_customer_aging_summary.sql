WITH customer_summary AS(
    SELECT c.customer_name, c.customer_grade,
    COALESCE(SUM(s.amount),0) AS total_amount,

    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 0 AND 
        julianday('2026-04-02') - julianday(s.order_date) <= 30 THEN s.amount
        ELSE 0
    END) AS current_0_30_amount,

    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 31 AND 
        julianday('2026-04-02') - julianday(s.order_date) <= 60 THEN s.amount
        ELSE 0
    END) AS over_31_60_amount,

    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 61 AND
        julianday('2026-04-02') - julianday(s.order_date) <=90 THEN s.amount
        ELSE 0
    END) AS over_61_90_amount,

    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 61 THEN s.amount
        ELSE 0
    END) AS over_61_total_amount,

    SUM(CASE
        WHEN julianday('2026-04-02') - julianday(s.order_date) >= 91 THEN s.amount
        ELSE 0
    END) AS over_91_plus_amount

    FROM customers AS c
    LEFT JOIN sales AS s
    ON c.customer_id = s.customer_id
    GROUP BY c.customer_name, c.customer_grade, c.customer_id
)
SELECT customer_name, customer_grade, total_amount,
current_0_30_amount, over_31_60_amount, over_61_90_amount, over_91_plus_amount,
over_61_total_amount,
CASE
    WHEN over_61_total_amount > 0 THEN 'Risk'
    ELSE 'Normal'
END AS risk_flag,

CASE
    WHEN total_amount = 0 THEN 0
    ELSE CAST(over_61_total_amount AS REAL) / total_amount
END AS risk_ratio

FROM customer_summary
ORDER BY 
CASE
    WHEN risk_flag = 'Risk' THEN 1
    ELSE 2
END,
risk_ratio DESC, total_amount DESC, customer_name ASC
;