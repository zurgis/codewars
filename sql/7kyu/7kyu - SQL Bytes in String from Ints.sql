-- Given a table of random numbers as follows:

-- ** numbers table schema **

-- id
-- number1
-- number2
-- number3
-- number4
-- number5
-- Your job is to return a table in the following format, where each value is the number of bytes in the string representation of the number.

-- ** output table schema **

-- octnum1
-- octnum2
-- octnum3
-- octnum4
-- octnum5
-- See expected results for more clarity if required.

/*  SQl  */
select 
  octet_length(number1::varchar) as octnum1, 
  octet_length(number2::varchar) as octnum2,
  octet_length(number3::varchar) as octnum3,
  octet_length(number4::varchar) as octnum4,
  octet_length(number5::varchar) as octnum5
from numbers