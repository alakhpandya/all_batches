use moviesdb;
select * from moviesdb.financials;
select * from aspirants;
select * from movies;

select title, industry from movies;

-- Print titles of all Bollywood movies

select title
from movies
WHERE industry = "bollywood";

-- Print number of different "industries" in the data

select count(distinct(industry))
from movies;

-- A user on imdb website searches "Thor" in the search bar. Show the result accordingly.

select title
from movies
where title like "%Thor%";

-- Print the movie titles which contain "Avenger" in them.

-- Print the movie titles and imdb rating of the movies having rating atleast 7
select title, imdb_rating
from movies
where imdb_rating >= 7;

-- Print the above result such a way that the movie with highest rating comes at the top and lowest last.
select title, imdb_rating
from movies
where imdb_rating >= 7
order by imdb_rating desc;

-- Print movie titles, their rating and year of release of the movies with rating atleast 5 but not exceeding 8.
select title, imdb_rating, release_year
from movies
-- where imdb_rating >= 5 and imdb_rating <= 8;
where imdb_rating between 5 and 8;

-- Print ids, titles and ratings of Hollwood movies with even id and ratings above 7

select movie_id, title, imdb_rating
from movies
where industry = "Hollywood" and imdb_rating > 7 and movie_id % 2 = 0;

-- Print titles and ratings of all the movies from Marvel Studios

-- Print all the movies which have “The” in them and have rating between 5 to 9 (including both)

-- Print the year in which the movie Godfather was released

-- Print all the movie studios of Bollywood.

-- Give me all the movies released in the years 2015, 2016 or 2018.

select *
from movies
where release_year in (2015, 2016, 2018);

-- Print the movie title for which imdb_rating is not available
select title
from movies
where imdb_rating is null;

-- Print the details of the movies for which imdb_ratings are available
select title
from movies
-- where imdb_rating != null;
-- where imdb_rating <> null;
where imdb_rating is not null;