-- Chapter 10: Project 1, Bramblewood sales performance (run with run_sql.py)

-- 10.1 Store revenue, 2024 versus 2025
SELECT st.store_name,
       ROUND(SUM(CASE WHEN s.order_date < '2025-01-01'
                      THEN s.units * s.unit_price * (1 - s.discount)
                 END), 0) AS rev_2024,
       ROUND(SUM(CASE WHEN s.order_date >= '2025-01-01'
                      THEN s.units * s.unit_price * (1 - s.discount)
                 END), 0) AS rev_2025
FROM sales AS s
JOIN stores AS st ON st.store_id = s.store_id
GROUP BY st.store_name
ORDER BY rev_2025 DESC;

-- 10.2 Outdoor category: units and average discount by year
SELECT substr(s.order_date, 1, 4) AS year,
       SUM(s.units) AS units,
       ROUND(AVG(s.discount) * 100, 1) AS avg_discount_pct,
       ROUND(SUM(s.units * s.unit_price * (1 - s.discount)), 0) AS revenue
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE p.category = 'Outdoor'
GROUP BY year;

-- 10.3 Outdoor units by product and year
SELECT p.product_name,
       SUM(CASE WHEN s.order_date < '2025-01-01'
                THEN s.units ELSE 0 END) AS units_2024,
       SUM(CASE WHEN s.order_date >= '2025-01-01'
                THEN s.units ELSE 0 END) AS units_2025
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE p.category = 'Outdoor'
GROUP BY p.product_name
ORDER BY units_2024 DESC;

-- 10.4 Margin by discount band, all categories, 2025
SELECT CASE WHEN s.discount = 0 THEN '0%'
            WHEN s.discount < 0.15 THEN '10%'
            ELSE '15-20%' END AS discount_band,
       COUNT(*) AS orders,
       ROUND(SUM(s.units * s.unit_price * (1 - s.discount)), 0)
         AS revenue,
       ROUND(100.0 * SUM(s.units * (s.unit_price * (1 - s.discount)
                                    - p.unit_cost))
         / SUM(s.units * s.unit_price * (1 - s.discount)), 1)
         AS margin_pct
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE s.order_date >= '2025-01-01'
GROUP BY discount_band
ORDER BY discount_band;
