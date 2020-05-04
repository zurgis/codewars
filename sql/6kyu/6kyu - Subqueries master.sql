-- The objective of this Kata is to show that you are proficient at string manipulation (and perhaps that you can use extensively subqueries).

-- You will use people table but will focus solely on the name column

-- name
-- Greyson Tate Lebsack Jr.
-- Elmore Clementina O'Conner
-- you will be provided with a full name and you have to return the name in columns as follows.

-- name	first_lastname	second_lastname
-- Greyson Tate	Lebsack	Jr.
-- Elmore	Clementina	O'Conner
-- Note: Don't forget to remove spaces around names in your result. Note: Due to multicultural context, if full name has more than 3 words, consider first 2 as name

SELECT
  ARRAY_TO_STRING(list[1:len-2], ' ') AS name,
  list[len-1] AS first_lastname,
  list[len] AS second_lastname
FROM
  (SELECT 
    list,
    ARRAY_LENGTH(list, 1) AS len 
  FROM 
    (SELECT STRING_TO_ARRAY(name, ' ') AS list FROM people) AS full_list)
  AS list_and_len

-- My answer
SELECT 
  CASE
    WHEN array_length(regexp_split_to_array(name, ' '), 1) = 3 THEN split_part(name, ' ', 1)
    ELSE split_part(name, ' ', 1) || ' ' || split_part(name, ' ', 2)
  END AS name,
  CASE
    WHEN array_length(regexp_split_to_array(name, ' '), 1) = 3 THEN split_part(name, ' ', 2)
    ELSE split_part(name, ' ', 3)
  END AS first_lastname,
  CASE
    WHEN array_length(regexp_split_to_array(name, ' '), 1) = 3 THEN split_part(name, ' ', 3)
    ELSE split_part(name, ' ', 4)
  END AS second_lastname
FROM people