-- Given a table of random numbers as follows:

-- ** numbers table schema **

-- id
-- number1
-- number2
-- Your job is to return table with similar structure and headings, where if the sum of a column is odd, the column shows the minimum value for that column, and when the sum is even, it shows the max value. You must use a case statement.

-- ** output table schema **

-- number1
-- number2

/*  SQL  */
select
  case
    when sum(number1) % 2 = 1 then min(number1)
    else max(number1)
  end as number1,
  case
    when sum(number2) % 2 = 1 then min(number2)
    else max(number2)
  end as number2
from numbers