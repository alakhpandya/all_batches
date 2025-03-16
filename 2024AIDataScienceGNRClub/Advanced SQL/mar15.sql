-- SELECT * FROM moviesdb.movies;

use moviesdb;
select * from actors;
-- 1. Print and observe all the tables of moviesdb (understand the data)
-- 2. Print title & industry of all movies from movies table
select title, industry from movies;

-- 3. Print all the Bollywood movies from movies table
Select *
from movies 
where industry = "bollywood";

-- 4.	Print all the different industries present in the movies table
-- select distinct industry
select distinct(industry)
from movies;
-- unique doesn't work with mySQL

/*
5. Suppose your query is going to produce result on the IMDB website based on user’s search. 
Return all the details of movies (all columns) if a user searches “Thor” on IMDB website search. 
Feel free to actually go on IMDB to check what it returns on the same search.
*/

select *
from movies
-- where title like "Thor%";	titles starting with "Thor"
-- where title like "%Thor";	titles ending with "Thor"
where title like "%Thor%";	 -- titles containing "Thor"

-- 6. Do the same (as in previous question) for a user who searches “Avenger“
select *
from movies
where title like "%Avenger%";

-- 7. Give me movies with rating at least 8.
select *
from movies
where imdb_rating >= 8;

-- 8. Print names, ratings, industry and production studios of the movies which have got at least 5 ratings on imdb but have not got more than 9 ratings
select *
from movies
-- where imdb_rating >=5 and imdb_rating <= 9;
where imdb_rating between 5 and 9;		-- between includes both 5 & 9

-- 9. Give me all the details of the movies with rating between 1 to 4 (including both)
select *
from movies
where imdb_rating between 1 and 4;

-- 10.	Give me all the Bollywood movies with rating more than 7 (titles, ratings & studio)
select *
from movies
where industry = "Bollywood" and imdb_rating > 7;

-- 11.	Print titles, ratings & studio of the Hollywood movies which have even movie_id & ratings above 7
select *
from movies
where industry = "Hollywood" and imdb_rating > 7 and movie_id % 2 = 0;

-- 12.	Print titles & release_year of all the movies from Marvel Studios
select title, release_year
from movies
where studio = "Marvel Studios";

-- 13.	Print all the movies which have word “The” in them and have rating between 5 to 9 (including both)
select * 
from movies
where title like "%The%" and imdb_rating between 5 and 9;

-- 14.	Print the year in which Godfather movie was released
select title, release_year
from movies
where title like "%Godfather%";

-- 15.	Print all the movie studios of Bollywood.
select distinct studio
from movies
where industry = "Bollywood";

-- 16.	Give me all the movies released in the years 2015, 2016, 2017 or 2018.
select *
from movies
where release_year between 2015 and 2018;

-- 17.      Print the number of Bollywood movies present in the movies table
-- select count(title)
-- select count(release_year)
-- select count(imdb_rating)
select count(*)
from movies
where industry = "Bollywood";

-- 18.  Give me the total number of movies released in years 2013, 2017 & 2022
select count(*)
from movies
-- where release_year = 2013 or release_year = 2017 or release_year = 2022;
where release_year in (2013, 2017, 2022);

-- 19.	Give me the movies for which imdb_rating is not available.
select *
from movies
where imdb_rating is null;	-- while dealing with NULL, we need to use "is" operator

-- 20.	Give me only those movies for which imdb_ratings are available
select *
from movies
where imdb_rating is not null;

-- 21.	Print all the movies which were not released in the year 2022
select *
from movies
-- where release_year != 2022;
where release_year <> 2022;

-- 22.	Print the movies sorted by their year of release such that the older movies come at the top and latest at the bottom.
select *
from movies
order by release_year;

-- 23.	Print the movies sorted by their imdb_ratings in a way that the highest rated movie comes first and lowest rated last.
select *
from movies
order by imdb_rating desc;

-- 24.	Print the movies such that the oldest movies come first & latest last but in a particular year, 
-- they should be arranged so that the movie with highest imdb_rating is at the top & movie with least imdb_rating is at the bottom.
select *
from movies
order by release_year asc, imdb_rating desc;