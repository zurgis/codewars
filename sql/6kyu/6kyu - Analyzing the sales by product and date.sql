-- Task
-- Given the information about sales in a store, calculate the total revenue for each day, month, year, and product.

-- Notes
-- Order the result by the product_name, year, month, day columns
-- We're interested only in the product-specific data, so you shouldn't return the total revenue from all sales
-- Input tables
-- ----------------------------------------
-- |    Table      |   Column   |  Type   |
-- |---------------+------------+---------|
-- | products      | id         | int     |
-- |               | name       | text    |
-- |               | price      | numeric |
-- |---------------+------------+---------|
-- | sales         | id         | int     |
-- |               | date       | date    |
-- |---------------+------------+---------|
-- | sales_details | id         | int     |
-- |               | sale_id    | int     |
-- |               | product_id | int     |
-- |               | count      | int     |
-- -----------------------------------------
-- Output table
-- --------------------------
-- |    Column    |  Type   |
-- |--------------+---------|
-- | product_name | text    |
-- | year         | int     |
-- | month        | int     |
-- | day          | int     |
-- | total        | numeric |
-- --------------------------
-- Example output
-- product_name | year | month | day | total
-- -------------+------+-------+-----+------
--  milk        | 2019 | 01    | 01  | 200
--  milk        | 2019 | 01    | 02  | 190
--  milk        | 2019 | 01    |     | 390
--  milk        | 2019 | 02    | 01  | 240
--  milk        | 2019 | 02    |     | 240
--  milk        | 2019 |       |     | 630
--  milk        |      |       |     | 630

SELECT p.name AS product_name,
  EXTRACT(year FROM s.date)::integer AS year,
  EXTRACT(month FROM s.date)::integer AS month,
  EXTRACT(day FROM s.date)::integer AS day,
  SUM(p.price * sd.count) AS total
FROM sales_details AS sd
INNER JOIN products AS p
  ON p.id = sd.product_id
INNER JOIN sales AS s
  ON s.id = sd.sale_id
GROUP BY product_name, ROLLUP (year, month, day)
ORDER BY p.name, year, month, day;