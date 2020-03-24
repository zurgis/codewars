-- For this challenge you need to create a SELECT statement, this SELECT statement will use an IN to check whether a department has had a sale with a price over 90.00 dollars BUT the sql MUST use the WITH statement which will be used to select all columns from sales where the price is greater than 90.00, you must call this sub-query special_sales.

-- departments table schema
-- id
-- name
-- sales table schema
-- id
-- department_id (department foreign key)
-- name
-- price
-- card_name
-- card_number
-- transaction_date
-- resultant table schema
-- id
-- name
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

-- Best Practices
-- Create your SELECT statement here
WITH special_sales AS
  ( SELECT * FROM sales WHERE price > 90.00 )
SELECT id, name FROM departments WHERE id IN (SELECT department_id FROM special_sales)

-- My answer
-- Create your SELECT statement here
WITH special_sales (id, department_id, name, price, card_name, card_number, transaction_date)
AS
  ( SELECT * FROM sales WHERE price > 90.00 )
SELECT d.id, d.name FROM departments d JOIN special_sales s ON d.id = s.department_id GROUP BY d.id ORDER BY d.id