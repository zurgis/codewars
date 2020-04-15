-- Your friends told you that if you keep coding on your computer, you are going to hurt your eyes. They suggested that you go with them to trivia night at the local club.

-- Once you arrive at the club, you realize the true motive behind your friends' invitation. They know that you are a computer nerd, and they want you to query the countries table and get the answers to the trivia questions.

-- Schema of the countries table:

-- country (String)
-- capital (String)
-- continent (String)
-- The first question: from the African countries that start with the character E, get the names of their capitals ordered alphabetically.

-- You should only give the names of the capitals. Any additional information is just noise
-- If you get more than 3, you will be kicked out, for being too smart
-- Also, this database is crowd-sourced, so sometimes Africa is written Africa and in other times Afrika.
-- Resources:

-- SQL LIKE Oerator
-- SQL IN Operator
-- SQL ORDER BY
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases just to validate your answer.

-- SQL for Beginners Series

-- This kata is part of a collection of SQL challenges for beginners. You can take the rest of the challenges here:

-- Adults only (SQL for Beginners #1)
-- On the Canadian Border (SQL for Beginners #2)
-- Register for the Party (SQL for Beginners #3)
-- Collect Tuition (SQL for Beginners #4)
-- Best-Selling Books (SQL for Beginners #5)
-- Countries Capitals for Trivia Night (SQL for Beginners #6)

-- Your solution here
select capital from countries 
where continent in ('Africa', 'Afrika')
and country like 'E%'
order by capital
limit 3