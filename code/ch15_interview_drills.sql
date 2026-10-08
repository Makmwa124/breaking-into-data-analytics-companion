-- Chapter 15 / Appendix B: SQL interview drills on bramblewood.db

-- Drill 1: top three products by 2025 revenue
SELECT p.product_name,
       ROUND(SUM(s.units * s.unit_price * (1 - s.discount)), 0) AS revenue
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE s.order_date >= '2025-01-01'
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 3;

-- Drill 2: stores whose 2025 revenue beat the average store
WITH store_rev AS (
  SELECT store_id, SUM(units * unit_price * (1 - discount)) AS revenue
  FROM sales
  WHERE order_date >= '2025-01-01'
  GROUP BY store_id
)
SELECT st.store_name, ROUND(r.revenue, 0) AS revenue
FROM store_rev AS r
JOIN stores AS st ON st.store_id = r.store_id
WHERE r.revenue > (SELECT AVG(revenue) FROM store_rev)
ORDER BY revenue DESC;

-- Drill 3: each store's busiest month in 2025 by order count
WITH m AS (
  SELECT store_id, substr(order_date, 1, 7) AS month, COUNT(*) AS orders,
         RANK() OVER (PARTITION BY store_id ORDER BY COUNT(*) DESC) AS rnk
  FROM sales
  WHERE order_date >= '2025-01-01'
  GROUP BY store_id, month
)
SELECT store_id, month, orders
FROM m
WHERE rnk = 1
ORDER BY store_id;

-- Drill 4: share of 2025 revenue from discounted orders
SELECT ROUND(100.0 * SUM(CASE WHEN discount > 0
                              THEN units * unit_price * (1 - discount)
                              ELSE 0 END)
             / SUM(units * unit_price * (1 - discount)), 1)
         AS pct_revenue_discounted
FROM sales
WHERE order_date >= '2025-01-01';

-- Drill 5: running total of 2025 revenue by quarter
WITH q AS (
  SELECT substr(order_date, 1, 4) || '-Q' ||
         ((CAST(substr(order_date, 6, 2) AS INTEGER) + 2) / 3) AS quarter,
         SUM(units * unit_price * (1 - discount)) AS revenue
  FROM sales
  WHERE order_date >= '2025-01-01'
  GROUP BY quarter
)
SELECT quarter,
       ROUND(revenue, 0) AS revenue,
       ROUND(SUM(revenue) OVER (ORDER BY quarter), 0) AS running_total
FROM q
ORDER BY quarter;
