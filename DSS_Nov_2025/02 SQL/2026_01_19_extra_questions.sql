SELECT *
FROM MOVIES;

-- 3.	Print all the Bollywood movies from movies table
select *
from movies
where industry = "bollywood";
-- 4. Print all the columns of financials table where currency is in USD

-- 5.	Print all the different industries present in the movies table
-- 6. Print all the unique unit present in financial table
-- 7. Return all the columns of financials table where currecy in in INR & unit is Billions
-- 8. From movies table, get me the rows that have studio name ending with "Films"
select *
from movies
where studio like "%Films";
-- 9. From movies table, return all the rows which have movie title starting with "D"

-- 10. Print all the columns of the movies table in which the movie title has "the" word in it.

-- 11. Return movie_id, title, release_year & imdb_rating of all the versions of "Avenger" sequel.

-- 12. Print all the movie_id, revenue, unit & currency which have revenue more than 1000. Use financials table.

-- 13.Print all the movie_id, revenue, unit & currency which have revenue more than 10 Million Dollars. Use financials table & only consider rows that have USD in currency.
select movie_id, revenue, unit, currency
from financials
where revenue > 10 and currency = "USD" and (unit = "Millions" or unit = "Billions");

-- 14. Get me the movie_id, budget, unit & currency of the movies which have budget between 100 Million INR to 1000 Million INR including both.
-- Consider only INR rows.