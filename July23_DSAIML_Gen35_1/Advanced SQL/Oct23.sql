use moviesdb;

-- Get me the titles, industry, ratings and budget of all the movies
select * from movies;
select * from financials;

select movies.title, movies.industry, movies.imdb_rating, financials.budget
from movies
JOIN financials
ON movies.movie_id = financials.movie_id;

select m.title, m.industry, m.imdb_rating, f.budget
from movies m
JOIN financials f
ON m.movie_id = f.movie_id;

-- JOIN means INNER JOIN

-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id
select ma.actor_id, m.title
from movies m
join movie_actor ma
on m.movie_id = ma.movie_id
order by actor_id asc;

-- Print number of movies played by each actor_id sorted in ascending order of actor_id.
select ma.actor_id, count(m.title)
from movies m
join movie_actor ma
on ma.movie_id = m.movie_id
group by ma.actor_id
order by actor_id;

-- Print number of movies played by each actor. That is, write name of the actor and number of movies played by them in against their names.
select a.name, count(title)
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
join actors a on ma.actor_id = a.actor_id
group by a.name
order by a.name;

/* 
Print the movie titles, industry and revenue. Sort the result in descending order of revenue. Clean the revenue so that it becomes easy to compare the business each movie did. 
(Hint: If all of them are in the same currency and in the same unit (thousand/million/billion etc) then it is possible to compare the business of movies with each other)
*/

select * from financials;

select movie_id, revenue, unit, currency, USD,
CASE 
	WHEN unit = "Billions" THEN USD*1000
    WHEN unit = "Millions" THEN USD
    WHEN unit = "Thousands" THEN USD/1000
END new_revenue
from (
	select movie_id, unit, revenue, currency, IF(currency = "INR", revenue/80, revenue) as USD
	from financials
) t1
order by new_revenue desc;