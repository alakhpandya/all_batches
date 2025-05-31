use moviesdb;
-- Get me the minimum ratings given to any movie
select min(imdb_rating) as Minimum_ratings
from movies;

select max(imdb_rating) as Max_ratings
from movies;

-- Get me the average imdb_rating for this data
select round(avg(imdb_rating), 1) as Avg_rating
from movies
where industry = "Bollywood";

select round(avg(imdb_rating), 1) as Avg_rating
from movies
where industry = "Hollywood";

select industry, round(avg(imdb_rating), 1) as Avg_rating
from movies
group by industry;

select title, imdb_rating/2 as new_ratings
from movies;

select concat(title, " | ", industry) as title
from movies;

select *,
substr(title, 1, 3) as short_title
from movies;

select upper(title) from movies;
select lower(title) from movies;

select concat(upper(substr(title, 1, 1)), lower(substr(title, 2))) as new_title
from movies;

select title, industry, coalesce(imdb_rating, 0) as rating from movies order by imdb_rating;
select title, industry, coalesce(imdb_rating, "N/A") as rating from movies order by imdb_rating;

select count(title) from movies;
select count(imdb_rating) from movies;
select count(studio) from movies;

select studio, count(*)
from movies
where studio != ""
group by studio
order by count(*) desc;

select title, imdb_rating
from movies
where imdb_rating is null;

select title, imdb_rating
from movies
where imdb_rating is not null;

select studio, count(*) as no_of_movies
from movies
where studio != ""
group by studio
having count(*) > 2;