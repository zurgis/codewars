-- Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

-- Your task is to make 'Past' function which returns time converted to milliseconds.

-- Example:
-- past(0, 1, 1) == 61000
-- Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59

select (h * 3600 + m * 60 + s) * 1000 as res from past