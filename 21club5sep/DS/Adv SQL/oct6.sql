use moviesdb;
/*
select * from financials;

with profitability as(
	select *, (revenue-budget)*100/budget as pct_profit
	from financials
),
below_avg as (
	select * from movies
    where imdb_rating < (select avg(imdb_rating) from movies)
)
select p.movie_id, b.title, b.imdb_rating, p.pct_profit
from profitability p
join below_avg b on p.movie_id = b.movie_id
where p.pct_profit >= 500;
*/

-- select * from movies;

-- Window function: RANK()

select *,
rank() over(partition by studio order by imdb_rating desc) as "Rank"
from movies;
-- order by title;

-- DENSE_RANK()
select *,
dense_rank() over(partition by studio order by imdb_rating desc) as "Rank"
from movies;

-- Give me the top movie of every studio based on their imdb_ratings
with cte as (
	select *,
	dense_rank() over(partition by studio order by imdb_rating desc) as "Ranking"
	from movies
)
select studio, title, imdb_rating
from cte
where Ranking = 1;

