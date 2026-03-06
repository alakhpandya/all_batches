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
