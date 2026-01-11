use moviesdb;

select * from movies;  -- inline comment

-- single line comment/inline comment
/*
Multi
Line
Comment
*/

-- printing selected columns:
select title, industry from movies;

-- where clause: Return all the bollywood movies
select * 
from movies
-- where industry = "Bollywood";
where industry = "bollywood";

-- Get me the actors who are born after 1985
select *
from actors
where birth_year > 1985;

-- Print movie_id, budget & revenue of those movies which have currency in USD. Use financials table from moviesdb.
select movie_id, budget, revenue
from financials
where currency = "USD";

-- Return title, industry & imdb_rating of movies which have at least 7 rating.
select title, industry, imdb_rating
from movies
where imdb_rating >= 7;

-- Return title, imdb_rating, release_year & studio of bollywood movies which were released after year 2000
select title, imdb_rating, release_year, studio
from movies
where industry = "Bollywood" and release_year > 2000;

-- Print all the details of the movies which have budget over 25 but revenue under 100. Use financials table from moviesdb database.
select *
from financials
where budget > 25 and revenue < 100;

-- Return movie_id, unit, revenue & currency of the movies which have unit in "millions" and currency in "INR"
use moviesdb;
select * from financials;
select movie_id, unit, revenue, currency
from financials
where unit = "Millions" and currency = "INR";

-- and = but = also = nevertheless