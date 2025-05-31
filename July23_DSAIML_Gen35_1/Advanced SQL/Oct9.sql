-- select * from moviesdb.actors;
-- select * from moviesdb.movies;

use moviesdb;
select * from actors;
select * from movies;

select title, industry, imdb_rating
from movies;

select title
from movies
WHERE industry = "Bollywood";

select distinct industry
from movies;

select *
from movies
-- where title like "Thor%";
-- where title like "%Thor";
where title like "%Thor%";

select title, imdb_rating
from movies 
where title like "%Avenger%";

select title, industry, imdb_rating
from movies
where imdb_rating >= 8;

select * from movies
where imdb_rating >=5 and imdb_rating <=9;

select * 
from movies 
where imdb_rating between 5 and 9;

-- 7. Print titles & release_year of all the movies from Marvel Studios

select *
from movies 
where imdb_rating >7 and industry = "bollywood";