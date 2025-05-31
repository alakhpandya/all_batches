use moviesdb;

select * from movies;
select count(movie_id), count(title), count(studio), count(*)
from movies;

select *
from movies
where imdb_rating is not null;

select count(imdb_rating)
from movies;

select title
from movies
where studio is null;


select *
from movies
-- order by imdb_rating asc;
order by imdb_rating desc;

select *
from movies
-- order by release_year, imdb_rating;
-- order by release_year, imdb_rating desc;
order by release_year desc, imdb_rating asc;


-- Print the top 5 movies according to their imdb_ratings:
select *
from movies
order by imdb_rating desc
limit 5;

select *
from movies
where industry = "Bollywood"
order by release_year desc, imdb_rating desc
limit 3 offset 2;