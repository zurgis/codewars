-- This kata is inspired by SQL Basics: Simple PIVOTING data by matt c.

-- You need to build a pivot table WITHOUT using CROSSTAB function. Having two tables products and details you need to select a pivot table of products with counts of details occurrences (possible details values are ['good', 'ok', 'bad'].

-- Results should be ordered by product's name.

-- Model schema for the kata is:

-- schema

-- your query should return table with next columns

-- name
-- good
-- ok
-- bad
-- Compare your table to the expected table to view the expected results.

-- Best Practices
-- add your query here!
SELECT p.name,
  count(case when d.detail = 'good' then 1 end) as good,
  count(case when d.detail = 'ok'  then 1 end) as ok, 
  count(case when d.detail = 'bad' then 1 end) as bad
FROM products p
INNER JOIN details d ON p.id = d.product_id
GROUP BY p.name
ORDER BY p.name

-- My answer
-- add your query here!
SELECT
  name,
  (SELECT count(detail) FROM details AS d WHERE detail = 'good' AND d.product_id = p.id) AS good,
  (SELECT count(detail) FROM details AS d WHERE detail = 'ok' AND d.product_id = p.id) AS ok,
  (SELECT count(detail) FROM details AS d WHERE detail = 'bad' AND d.product_id = p.id) AS bad
FROM 
  products as p
ORDER BY name