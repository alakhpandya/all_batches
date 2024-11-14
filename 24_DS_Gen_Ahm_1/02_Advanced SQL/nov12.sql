select * from moviesdb.movies;

use moviesdb;
select * from movies;
select * 
from financials;

select title, release_year, imdb_rating
from movies;

-- 2.	Print title & industry of all movies from movies table
select title, industry from movies;

-- 3.	Print all the Bollywood movies from movies table
select *
from movies
where industry = "bollywood";

-- 4.	Print all the different industry present in the movies table
select distinct(industry) from movies;
select distinct industry from movies;

/*
5.	Suppose your query is going to produce result on the IMDB website based on user’s search. 
Return all the details of movies (all columns) if a user searches “Thor” on IMDB website search. 
Feel free to actually go on IMDB to check what it returns on the same search.
*/
select *
from movies
-- where title = "Thor";
-- where title like "Thor%";
-- where title like "%Thor";
where title like "%Thor%";

-- 6.	Do the same (as in previous question) for a user who searches “Avenger”
select * from movies
where title like "%avenger%";

-- 7.	Give me movies with rating at least 8.
select *
from movies
where imdb_rating >= 8;

-- 8.	Print names, ratings, industry and production studios of the movies which have got at least 5 ratings on imdb but have not got more than 9 ratings
select title, imdb_rating, industry, studio
from movies
-- where imdb_rating >= 5 and imdb_rating <= 9;
where imdb_rating between 5 and 9;

-- 9.	Give me all the details of the movies with rating between 1 to 4 (including both)
select *
from movies
where imdb_rating between 1 and 4;

-- 10.	Give me all the Bollywood movies with rating more than 7 (titles, ratings & studio)
select title, imdb_rating, studio
from movies
where industry = "Bollywood" and imdb_rating > 7;

-- 11.	Print titles, ratings & studio of the Hollywood movies which have even movie_id & ratings above 7
select title, imdb_rating, studio
from movies
where industry="Hollywood" and imdb_rating > 7 and movie_id % 2 = 0;

-- 12.	Print titles & release_year of all the movies from Marvel Studios
select title, release_year
from movies
where studio = "Marvel Studios";

-- 13.	Print all the movies which have word “The” in them and have rating between 5 to 9 (including both)
select *
from movies
where title like "% The %" and imdb_rating between 5 and 9;