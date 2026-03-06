use moviesdb;
select * from movies;
select * from languages;

-- Natural join
select *
from movies
join languages
using(language_id);

select m.movie_id, title, studio, m.language_id, l.name
from movies m
join languages l		-- join means inner join by default
on m.language_id = l.language_id;

-- Print movie_id, title, industry, budget, unit, currency & studio.
select m.movie_id, title, industry, budget, unit, currency, studio
from movies m
join financials f on m.movie_id = f.movie_id;

-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id.
select actor_id, title
from movies m
join movie_actor ma on m.movie_id = ma.movie_id;

-- Print number of movies played by each actor beside his/her name sorted in descending order of number of movies
select name, count(movie_id) as no_of_movies
from movie_actor ma
join actors a on ma.actor_id = a.actor_id
group by a.actor_id
order by 2 desc;

-- List all movies along with their budget and revenue (Print all the columns of movies table along with budget & revenue)
select m.*, f.budget, f.revenue
from movies m
join financials f on m.movie_id = f.movie_id;

-- Display movie titles and their language names for movies released after 2015.
select m.title, l.name
from movies m
join languages l on m.language_id = l.language_id
where m.release_year > 2015;

-- Count how many movies are available in each language (use inner join only)
select l.name, count(*) as no_of_movies
from movies m
join languages l on m.language_id = l.language_id
group by l.language_id;

-- Display movie titles, budgets, and revenues for only those movies which have made profit
select m.title, f.budget, f.revenue
from movies m
join financials f on m.movie_id = f.movie_id
where revenue > budget;

-- Print names of actors who have acted in at least in 2 movies.
select name, count(movie_id) as no_of_movies
from movie_actor ma
join actors a on ma.actor_id = a.actor_id
group by a.actor_id
having count(movie_id) >= 2;

-- Print minimum, maximum & average budget for each Bollywood studio. Return studio, minimum budet, maximum budget & avg budget columns.
select studio, min(budget) as "minimum budget", max(budget) as "maximum budget", round(avg(budget), 1) as "avg budget"
from movies m
join financials f on m.movie_id = f.movie_id
where industry = "Bollywood"
group by studio;

-- Find the average IMDb rating of movies for each industry and language combination
select industry, l.name, round(avg(imdb_rating), 1) as avg_rating
from movies m
join languages l on m.language_id = l.language_id
group by industry, l.name;

-- Display actor name along with the average IMDb rating of the movies they have acted in.
select a.name, round(avg(imdb_rating), 1) as avg_rating
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
join actors a on ma.actor_id = a.actor_id
group by a.actor_id;

select ma.movie_id, a.* 
from actors a
join movie_actor ma on a.actor_id = ma.actor_id;

select * from movie_actor order by actor_id;