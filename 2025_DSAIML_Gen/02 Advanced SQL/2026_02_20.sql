-- 1.	Print and observe all the tables of moviesdb (understand the data)
-- 2.	Print title & industry of all movies from movies table
select title, industry
from movies;

-- 3.	Print all the Bollywood movies from movies table
select *
from movies
where industry = "bollywood";

-- 4.	Print all the different industries present in the movies table
select distinct(industry)
from movies;