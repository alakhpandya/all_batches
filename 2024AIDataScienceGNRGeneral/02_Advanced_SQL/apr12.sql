-- joins: Inner join, left join, right join, full outer join/outer join, self join, cross join

use moviesdb;
select * from movies;
select * from languages;

select *
from movies m
join languages l				-- default join type: inner join
on m.language_id = l.language_id;

select m.movie_id, m.title, m.imdb_rating, m.language_id, l.name as language
from movies m
join languages l				-- default join type: inner join
on m.language_id = l.language_id;

select m.movie_id, m.title, m.imdb_rating, m.language_id, l.name as language
from movies m
left join languages l				
on m.language_id = l.language_id;

select * from movies;
insert into movies values(141, "Chhava", "Bollywood", 2025, 9.5, "Maddock Films", null);

select m.movie_id, m.title, m.imdb_rating, m.language_id, l.name as language
from movies m
right join languages l
on m.language_id = l.language_id;

select *
from movies m
inner join languages l
using(language_id);

-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id.

-- Print names of actors vs. movies they have played role in. Print your result in alphabetical order of actors’ names.
select * from actors;
select * from movies;
select * from movie_actor;

select a.name, m.title
from actors a
left join movie_actor ma on a.actor_id = ma.actor_id
left join movies m on ma.movie_id = m.movie_id
order by 1;

-- Print average imdb_rating of the movies played by each actor. Return avg_rating column beside name of each actor.
