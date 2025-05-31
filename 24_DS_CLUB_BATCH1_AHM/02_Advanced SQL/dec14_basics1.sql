use moviesdb;
-- select * from moviesdb.movies;
select * from movies;

-- 1. Print all the tables & understand the data

-- 2.	Print title & industry of all movies from movies table

-- 3.	Print all the Bollywood movies from movies table
select *
from movies
where industry = "bollywood";

-- 4.	Print all the different industry present in the movies table
-- select distinct(industry)
select distinct industry
from movies;

/*
5.	Suppose your query is going to produce result on the IMDB website based on user’s search. 
Return all the details of movies (all columns) if a user searches “Thor” on IMDB website search. 
Feel free to actually go on IMDB to check what it returns on the same search.
*/

select *
from movies
-- where title like "Thor%";	begins with "Thor"
-- where title like "%Thor";	ends with "Thor"
where title like '%thor%';		-- contains "Thor"

-- 6.	Do the same (as in previous question) for a user who searches “Avenger”
select *
from movies
where title like "%Avenger%";

-- 7.	Give me movies with rating at least 8.


-- 8.	Print names, ratings, industry and production studios of the movies which have got at least 5 ratings on imdb but have not got more than 9 ratings
select *
from movies
where imdb_rating between 5 and 9;

-- 9.	Give me all the details of the movies with rating between 1 to 4 (including both)

-- 10.	Give me all the Bollywood movies with rating more than 7 (titles, ratings & studio)

-- 11.	Print titles, ratings & studio of the Hollywood movies which have even movie_id & ratings above 7

-- 12.	Print titles & release_year of all the movies from Marvel Studios

-- 13.	Print all the movies which have word “The” in them and have rating between 5 to 9 (including both)

-- 14.	Print the year in which the movie Godfather was released

-- 15.	Print all the movie studios of Bollywood.

-- 16.	Give me all the movies released in the years 2015, 2016, 2017 or 2018.

-- 17.	How many Bollywood movies are there in the movies table?
select count(*) "no of movies"
from movies
where industry = "Bollywood";


-- 