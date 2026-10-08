-- Chapter 5: SQL basics on bramblewood.db (SQLite)

-- 5.1 Look at the first five rows
SELECT * FROM sales LIMIT 5;

-- 5.2 Revenue by store in 2025
SELECT st.store_name,
       ROUND(SUM(s.units * s.unit_price * (1 - s.discount)), 0)
         AS revenue_2025
FROM sales AS s
JOIN stores AS st ON st.store_id = s.store_id
WHERE s.order_date BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY st.store_name
ORDER BY revenue_2025 DESC;

-- 5.3 Revenue and gross margin by category in 2025
SELECT p.category,
       ROUND(SUM(s.units * s.unit_price * (1 - s.discount)), 0)
         AS revenue,
       ROUND(SUM(s.units * (s.unit_price * (1 - s.discount)
                            - p.unit_cost)), 0) AS gross_profit,
       ROUND(100.0 * SUM(s.units * (s.unit_price * (1 - s.discount)
                                    - p.unit_cost))
         / SUM(s.units * s.unit_price * (1 - s.discount)), 1)
         AS margin_pct
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE s.order_date >= '2025-01-01'
GROUP BY p.category
ORDER BY revenue DESC;

-- 5.4 Orders by discount band (CASE)
SELECT CASE
         WHEN discount = 0    THEN '1. No discount'
         WHEN discount < 0.15 THEN '2. Under 15%'
         ELSE '3. 15% or more'
       END AS discount_band,
       COUNT(*) AS orders
FROM sales
GROUP BY discount_band
ORDER BY discount_band;

-- 5.5 Month-on-month change with a window function (first half of 2025)
WITH monthly AS (
  SELECT substr(order_date, 1, 7) AS month,
         SUM(units * unit_price * (1 - discount)) AS revenue
  FROM sales
  GROUP BY month
)
SELECT month,
       ROUND(revenue, 0) AS revenue,
       ROUND(LAG(revenue) OVER (ORDER BY month), 0) AS prev_month,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
             / LAG(revenue) OVER (ORDER BY month), 1) AS pct_change
FROM monthly
WHERE month BETWEEN '2024-12' AND '2025-06'
ORDER BY month;

-- 5.10 Filter groups with HAVING: products with more than 500 order lines in 2025
SELECT p.product_name, COUNT(*) AS order_lines
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE s.order_date >= '2025-01-01'
GROUP BY p.product_name
HAVING COUNT(*) > 500
ORDER BY order_lines DESC;
