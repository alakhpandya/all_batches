-- C.T.E. : Common Table Expression

-- From moviesdb database print names of all the actors who are of age from 70 to 85 (including both). Use CTE method instead of subquery if needed.
use moviesdb;

select *
from (
	select *, year(curdate()) - birth_year as age
	from actors
) as t
where age between 70 and 85;

with t as (
	select *, year(curdate()) - birth_year as age
	from actors
)
select * 
from t
where age between 70 and 85;

-- Create a result showing movies released after 2015 and display their title and rating.
with cte as (
	select * from movies
    where release_year > 2015
)
select title, imdb_rating
from cte;

-- Create a result showing movies with IMDb rating greater than 8 and display their titles and ratings.
with t1 as (
	select * from movies
    where imdb_rating > 8
)
select title, imdb_rating
from t1;

-- Create a result showing total number of movies in each industry, and display industries having more than 5 movies.
with a as (
	select industry, count(*) as total_movies
    from movies
    group by industry
)
select * 
from a
where total_movies > 5;

-- Create a result that calculates the average IMDb rating of all movies, and display movies rated above the average.
with t as (
	select avg(imdb_rating) as avg_rating
    from movies
)
select * 
from movies
where imdb_rating > (select avg_rating from t);

-- Create a result that calculates the average movie budget, and display movie_id whose budget is greater than the average.
with t as (
	select avg(budget) from financials
)
select movie_id
from financials
where budget > (select * from t);

-- Create a result showing total movies acted by each actor, and display actor_id who have acted in more than 2 movies.
with t as (
	select actor_id, count(*) as total_movies
    from movie_actor
    group by actor_id
)
select actor_id, total_movies
from t
where total_movies > 2;

-- Create a result showing total movies acted by each actor, and display names of the actors who have acted in more than 2 movies.
with t as (
	select actor_id, count(*) as total_movies
    from movie_actor
    group by actor_id
)
select t.actor_id, a.name, total_movies
from t
join actors a on t.actor_id = a.actor_id
where total_movies > 2;

-- Convert all the budget & revenue in millions
select movie_id,
case
	when unit = "Billions" then budget * 1000
    when unit = "Thousands" then budget / 1000
    else budget
end as budget_mn,
case
	when unit = "Billions" then revenue * 1000
    when unit = "Thousands" then revenue / 1000
    else revenue
end as revenue_mn,
currency
from financials;

-- Use the above query as CTE & convert all the budget & revenue in USD. Use $ 1 = ₹ 80 conversion rate.
with t1 as (
	select movie_id,
	case
		when unit = "Billions" then budget * 1000
		when unit = "Thousands" then budget / 1000
		else budget
	end as budget_mn,
	case
		when unit = "Billions" then revenue * 1000
		when unit = "Thousands" then revenue / 1000
		else revenue
	end as revenue_mn,
	currency
	from financials
)
select movie_id,
round(if(currency = "INR", budget_mn/80, budget_mn), 2) budget_mn_USD,
round(if(currency = "INR", revenue_mn/80, revenue_mn), 2) revenue_mn_USD
from t1;

-- Create a result showing total movies released per year, and display the year with the highest number of movie releases.
with t as (
	select release_year, count(*) as total_movies
    from movies
    group by release_year
)
select *
from t
order by 2 desc
limit 1;

/*
Print the movies which produced more than 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: profit * 100 / Budget.
*/
with t1 as (
	select movie_id, (revenue - budget)*100/budget as pct_profit
	from financials
    where (revenue - budget)*100/budget > 500
)
select t1.movie_id, title, industry, release_year, imdb_rating, studio, pct_profit
from t1
left join movies m on m.movie_id = t1.movie_id
where imdb_rating < (select avg(imdb_rating) from movies);

-- Another way to do this:
with t1 as (
	select movie_id, (revenue - budget)*100/budget as pct_profit
	from financials
    where (revenue - budget)*100/budget > 500
),
t2 as (
	select *
    from movies
    where imdb_rating < (select avg(imdb_rating) from movies)
)
select *
from t1
join t2 on t1.movie_id = t2.movie_id;

-- Print the movie_id, title, industry, imdb_rating, studio and name of the language of top 5 profitable movies.
with t1 as (
	select movie_id,
	case
		when unit = "Billions" then budget * 1000
		when unit = "Thousands" then budget / 1000
		else budget
	end as budget_mn,
	case
		when unit = "Billions" then revenue * 1000
		when unit = "Thousands" then revenue / 1000
		else revenue
	end as revenue_mn,
	currency
	from financials
),
t2 as (
	select movie_id, 
	round(if(currency = "INR", revenue_mn/80, revenue_mn), 2) -
    round(if(currency = "INR", budget_mn/80, budget_mn), 2) profit_mn_USD
	from t1
)
select m.movie_id, title, industry, imdb_rating, studio, profit_mn_USD, l.name as language
from t2
right join movies m on m.movie_id = t2.movie_id
join languages l on m.language_id = l.language_id
order by profit_mn_USD desc
limit 5;