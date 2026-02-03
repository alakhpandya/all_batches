-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id.
use moviesdb;
select * from movie_actor;
select * from movies;
select * from actors;

select actor_id, title
from movies m
join movie_actor ma
on m.movie_id = ma.movie_id
order by actor_id;

-- Print number of movies played by each actor beside his/her name sorted in ascending order of actor_id.
select a.name, count(movie_id)
from movie_actor ma
join actors a
on ma.actor_id = a.actor_id
group by ma.actor_id;

-- List all movies along with their budget and revenue (Print all the columns of movies table along with budget & revenue)
select m.*, f.budget, f.revenue
from movies m
join financials f
on m.movie_id = f.movie_id;

-- Display movie titles and their language names for movies released after 2015.
select m.title, l.name
from movies m
join languages l
on m.language_id = l.language_id
where release_year > 2015;

-- Show all movies along with their language name where the language is 'English'.
select m.*, l.name
from movies m
join languages l
on m.language_id = l.language_id
where l.name = "English";

-- Count how many movies are available in each language (use inner join only)
select l.name, count(*)
from movies m
join languages l
on m.language_id = l.language_id
group by l.name;

-- Display the average IMDb rating for movies in each language. = Do "language-wise average of imdb_rating"
select l.name, round(avg(imdb_rating), 1)
from movies m
join languages l
on m.language_id = l.language_id
group by l.name;

-- Display movie titles, budgets, and revenues for movies where revenue is greater than budget.
select m.title, f.budget, f.revenue
from movies m
join financials f
on m.movie_id = f.movie_id
where f.revenue > f.budget;

-- Print actors who have acted in at least 3 movies.
select actor_id, count(*)
from movie_actor
group by actor_id
having count(*) >= 3;

-- Print names of actors who have acted in at least 3 movies.
select a.name, count(*)
from movie_actor ma
join actors a
on ma.actor_id = a.actor_id
group by a.name
having count(*) >= 3;

-- Why do we write "ma.actor_id = a.actor_id" or "m.movie_id = f.movie_id" inside "on" clause?
select *
from movies m
join financials f
on m.movie_id < f.movie_id;