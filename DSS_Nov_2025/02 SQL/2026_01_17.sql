-- CRUD: Create, Read, Update, Delete

/*
Print all the movies which have word “The” in them and have rating between 5 to 9 (including both)
*/
use moviesdb;
select *
from movies
where title like "%the%" and
imdb_rating between 5 and 9;

-- Print the number of Bollywood movies present in the movies table
-- select count(movie_id) as number_of_bollywood_movies
-- select count(movie_id) number_of_bollywood_movies
-- select count(title)
-- select count(imdb_rating)
select count(*) as number_of_bollywood_movies
from movies
where industry = "bollywood";

-- Give me the total number of movies released in years 2013, 2017 & 2022
select count(*)
from movies
where release_year in (2013, 2017, 2022);

-- Print all the movies which were not released in the year 2022

-- Print all the movies which were not released in the year 2016, 2020 & 2022

-- Print the movies sorted by their year of release such that the older movies come at the top and latest at the bottom
select *
from movies
order by release_year;

-- Sort the movies in the ascending order of their imdb_rating
select *
from movies
order by imdb_rating;

-- Sort the movies in the discending order of their imdb_rating
select *
from movies
order by imdb_rating desc;

-- Sort the movies in the discending order of their imdb_rating but show only those movies for which imdb_rating is available
select *
from movies
where imdb_rating is not Null
order by imdb_rating desc;

/*
Print the movies such that the oldest movies come first & latest last but in a particular year, 
they should be arranged so that the movie with highest imdb_rating is at the top & movie with least imdb_rating is at the bottom.
*/
select *
from movies
order by release_year asc, imdb_rating desc;

-- Print the top 5 movies according to their imdb_ratings
select *
from movies
order by imdb_rating desc
limit 5;

-- Return title, release_year, imdb_rating & studio of the latest movies (released after 2014). 
-- Return only top 10 of them when sorted in descending order of imdb_rating.
select title, release_year, imdb_rating, studio
from movies
where release_year > 2014
order by imdb_rating desc
limit 10;

-- Sort movies by their titles in ascending order : Sorts as per ASCII values
select *
from movies
order by title;

/*
We have organized an award ceremony for these movies. Top 3 movies (based on their imdb_rating) are getting the bumper prizes which have been already announced. 
Now we want to give condolence prizes to the movies which stood from rank 4th till 10th (including both) according to their imdb_rating. 
You are asked to print titles and ratings of these movies.
*/

select title, imdb_rating
from movies
order by 2 desc;

select title, imdb_rating
from movies
order by 2 desc
limit 7
offset 3;

-- Print the least, highest & average values of imdb_ratings rounded off after one decimal place
select 
round(min(imdb_rating), 1) as min_rating,
round(max(imdb_rating), 1) as max_rating,
round(avg(imdb_rating), 1) as avg_rating	
from movies;

-- avg() does not count the nulls while dividing
select sum(imdb_rating) from movies;

-- Print the average imdb_rating of the “Vinod Chopra Films” studio
select avg(imdb_rating) as avg_rating
from movies
where studio = "Vinod Chopra Films";

/*
Print the table in the following format:
id		title								release_year	imdb_rating		studio
101		K.G.F: Chapter 2 | Bollywood		2022			8.4				Hombale Films
*/

select 
movie_id as id,
concat(title, " | ", industry) as title,
release_year, imdb_rating, studio
from movies;

-- Print only the first character of title of each movie
select substr(title, 1, 1)
from movies;

-- Print the third, forth & fifth characters of title of each movies in uppercase
select
upper(substr(title, 3, 3)) as new_title
from movies;

-- Print the titles of movies in a way that first character of title of every movie is capitalized and every other character in lower case.
select
concat(upper(substr(title, 1, 1)), lower(substr(title, 2))) as new_title
from movies;

-- Replace all the null values in imdb_ratings column by 0.
select title, coalesce(imdb_rating, 0) as imdb_rating
-- select title, coalesce(imdb_rating, "N/A") as imdb_rating
from movies;

select title,
ifnull(imdb_rating, 0) as new_rating
from movies;