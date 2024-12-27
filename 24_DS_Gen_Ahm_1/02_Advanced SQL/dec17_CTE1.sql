use moviesdb;
-- 1. Find movies with an IMDb rating above the average rating
select title, imdb_rating from movies
where imdb_rating > (select avg(imdb_rating) as avg_rating from movies);

-- 2. List movies released in the same year as the movie titled 'Inception'
select title from movies
where release_year = (select release_year from movies where title = 'Inception');

-- 3. Find the highest-rated movies for each studio
SELECT studio, title, imdb_rating
FROM movies m
WHERE imdb_rating = (
    SELECT MAX(imdb_rating)
    FROM movies as m2
    WHERE m2.studio = m.studio
) 
order by 1;


-- CTE: Common Table Expression
-- Task-1: converting all budget & revenue into millions
-- Task-2: converting all budget & revenue into INR

with t1 as
(
	select movie_id, currency,
	case
		when unit="Billions" then budget*1000
		when unit="Thousands" then budget/1000
		else budget
	end budget_mn,
	case
		when unit="Billions" then revenue*1000
		when unit="Thousands" then revenue/1000
		else revenue
	end revenue_mn
	from financials
),
t2 as
(
	select movie_id,
			if(currency="USD", budget_mn*80, budget_mn) as budget_mn_inr,
			if(currency="USD", revenue_mn*80, revenue_mn) as revenue_mn_inr
	from t1
),
t3 as
(
select movie_id, revenue_mn_inr - budget_mn_inr as profit from t2
)
select m.movie_id, m.title, m.imdb_rating, t3.profit
from movies m
left join t3 on m.movie_id = t3.movie_id
order by profit desc;

/*
1. Find the Average Rating of Movies by Studio
Write a query using a CTE to calculate the average rating of movies grouped by Studio.
*/
with cte as
(
	select studio, avg(imdb_rating) as avg_rating
    from movies
    group by studio
)
select * 
from cte;














