-- Given the following table 'decimals':

-- ** decimals table schema **

-- id
-- number1
-- number2
-- Return a table with two columns (number1, number2) where the values in number1 have been rounded down and the values in number2 have been rounded up.

/*  SQL  */
select floor(number1) as number1, ceil(number2) as number2 from decimals