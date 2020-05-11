-- Write a SELECT query which will return all prime numbers smaller than 100 in ascending order.

-- Your query should return one column named prime.

-- your code here
SELECT prime FROM generate_series(2, 100) as prime
WHERE NOT EXISTS(SELECT i FROM generate_series(2, prime-1) as i WHERE prime % i = 0)