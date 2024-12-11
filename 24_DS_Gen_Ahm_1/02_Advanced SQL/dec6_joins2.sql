/*
Print average imdb_rating of the movies played by each actor. Return avg_rating column beside name of each actor.
*/
use moviesdb;
select * from movies;
select * from actors;
select * from movie_actor;

select a.name, avg(imdb_rating) as avg_rating
from actors a
join movie_actor ma
on a.actor_id = ma.actor_id
join movies m
on m.movie_id = ma.movie_id
group by a.name
order by a.name;

-- Get me the movies sorted by their budget so that the movie with highest budget is on the top and lowest at the bottom.
select * from financials;
select m.movie_id, m.title, f.budget
from movies m
left join financials f
on m.movie_id = f.movie_id
order by f.budget desc;