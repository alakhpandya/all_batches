-- Get me the title, industry, release_year, studio & imdb_rating of the movies which have ratings above 5 but not released in the year 2000
select title, industry, release_year, studio, imdb_rating
from movies
where imdb_rating > 5 and release_year != 2000;

-- Print the title, industry, imdb_rating & release_year of the movies which were either released after the year 2000 or have minimum 6 imdb_rating. Use movies table from moviesdb database.
select title, industry, imdb_rating, release_year
from movies
where release_year > 2000 or imdb_rating >= 6;

-- Print all the industries present in the movies table from moviesdb database
-- select distinct industry
select distinct(industry)
from movies;

/*
Suppose your query is going to produce result on the IMDB website based on user’s search. 
Return all the details of movies (all columns) if a user searches “Thor” on IMDB website search. 
Feel free to actually go on IMDB to check what it returns on the same search.
*/
select *
from movies
-- where title = "Thor";	Doesn't work!
where title like "%Thor%";

-- Return all the coumns for the movies starting with "Avenger"
select *
from movies
where title like "Avenger%";

-- Return all the coumns for the movies ending with "Avenger"
select *
from movies
where title like "%Avenger";

-- Return all the coumns for the movies containing "Avenger"
select *
from movies
where title like "%Avenger%";

-- Give me movies with rating at least 8
select *
from movies
where imdb_rating >= 8;

-- Print names, ratings, industry and production studios of the movies which have got at least 5 ratings on imdb but have not got more than 9 ratings
-- rating >= 5 and  rating <= 9
select title, imdb_rating, industry, studio
from movies
where imdb_rating >= 5 and  imdb_rating <= 9;

-- between: includes both end points
select title, imdb_rating, industry, studio
from movies
where imdb_rating between 5 and 9;

-- Give me all the details of the movies with rating between 1 to 4 (including both)
select *
from movies
where imdb_rating between 1 and 4;

-- Give me all the Bollywood movies with rating more than 7 (titles, ratings & studio)
select title, imdb_rating, studio
from movies
where industry = "Bollywood" and imdb_rating > 7;

-- Return titles, release_year & imdb_ratings of the movies of Marvel Studios which were released between 2017 to 2023 including both the years
select title, release_year, imdb_rating
from movies
where studio = "Marvel Studios" and release_year between 2017 and 2023;

-- Print titles, ratings & studio of the Hollywood movies which have even movie_id & ratings above 7
select title, imdb_rating, studio
from movies
where industry = "Hollywood" and movie_id % 2 = 0 and imdb_rating > 7;

-- Print the year in which Godfather movie was released
select release_year
from movies
where title like "%Godfather%";

-- Print all the movie studios of Bollywood.
select distinct studio
from movies
where industry = "Bollywood";

-- Print all the columns of the movies for which imdb_rating is not available
select *
from movies
where imdb_rating is null;

-- Print all the columns of all the movies for which imdb_rating are available
select *
from movies
where imdb_rating is not null;

-- Print all the movie studios of Bollywood excluding missing studio names.
select distinct studio
from movies
where industry = "Bollywood" and studio != "";

-- Imagine I want to clean studio column for Bollywood industry in a way that I get rid of all the studio names which are missing.
-- Keep in mind that some missing name might be "" (Empty string) and some might be NULL
select distinct studio
from movies
where industry = "Bollywood" 
and 
studio is not null
and
studio != "";

-- Give me all the movies released in the years 2015, 2016, 2017 or 2018.
select *
from movies
where release_year between 2015 and 2018;

-- Print all the columns of the movies which were released in years 2015, 2018, 2021 and 2022
select *
from movies
where release_year in (2015, 2018, 2021, 2022);

-- Print all the movies of Hombale Films, DVV Entertainment & Arka Media Works
select *
from movies
where studio in ("Hombale Films", "DVV Entertainment", "Arka Media Works");