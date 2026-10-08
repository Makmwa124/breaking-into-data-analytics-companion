-- Chapter 5: three common SQL mistakes, and the fixes

-- 5.6 Mistake: counting rows when you meant to count stores
SELECT COUNT(*) AS rows_counted,
       COUNT(DISTINCT s.store_id) AS stores
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE p.product_name = 'Outdoor setting 5-pc'
  AND s.order_date >= '2025-01-01';

-- 5.7 Mistake: mixing AND and OR without brackets
SELECT COUNT(*) AS orders
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE p.category = 'Outdoor' OR p.category = 'Garden'
  AND s.order_date >= '2025-01-01';

-- 5.8 The fix: brackets (or IN)
SELECT COUNT(*) AS orders
FROM sales AS s
JOIN products AS p ON p.product_id = s.product_id
WHERE p.category IN ('Outdoor', 'Garden')
  AND s.order_date >= '2025-01-01';

-- 5.9 Mistake: whole-number division
SELECT 7 / 2 AS whole_number_division,
       7 * 1.0 / 2 AS decimal_division;
