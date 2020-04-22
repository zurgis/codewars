-- Given a demographics table in the following format:

-- ** demographics table schema **

-- id
-- name
-- birthday
-- race
-- return a single column named 'calculation' where the value is the bit length of name, added to the number of characters in race.

/*  SQL  */
select bit_length(name) + length(race) as calculation from demographics