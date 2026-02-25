use moviesdb;
select * from financials;
-- 1 Billion = 1000 Millions = 1000000 Thousands
select distinct unit from financials;

-- Convert budget & revenue of all the movies (from financials table) into millions. Return movie_id, budget_mn, revenue_mn & currency columns.
select movie_id,
case
	when unit = "Billions" then budget*1000
    when unit = "Thousands" then budget/1000
    else budget
end as budget_mn,
case
	when unit = "Billions" then revenue*1000
    when unit = "Thousands" then revenue/1000
    else revenue
end as revenue_mn,
currency
from financials;

-- Display movies whose IMDb rating is higher than the average IMDb rating of movies of the same studio.
select *
from movies m1
where imdb_rating > (
	select avg(imdb_rating)
    from movies m2
    where m1.studio = m2.studio
);

-- Display movies whose revenue is greater than the average revenue of movies released in the same year.
select *
from financials f1
join movies m1 on f1.movie_id = m1.movie_id
where revenue > (
	select avg(revenue)
    from financials f2
    join movies m2 on f2.movie_id = m2.movie_id
    where m1.release_year = m2.release_year
);

-- Display movies that have a rating higher than every movie released before 2015.
select *
from movies
where imdb_rating > (
	select max(imdb_rating)
    from movies
    where release_year < 2015
);

-- Display languages that have more movies than the average number of movies per language.
select count(distinct language_id)
from languages l;

select language_id, name
from languages l
where (
	select count(movie_id)		-- no. of movies per lang
	from movies m1
    where l.language_id = m1.language_id
) >
(
	select count(movie_id) / count(distinct language_id)		-- avg no of movies per lang
	from movies m2
);

-- Display actors who have acted in movies from more industries than the average industry per actor.
select distinct name
from actors a
where 
(
	select count(distinct industry)							-- count_of_industries_for_that_actor
    from movies m1
    join movie_actor ma on m1.movie_id = ma.movie_id
    where a.actor_id = ma.actor_id
)
>
(
	select count(distinct industry) / count(distinct actor_id)		-- average_industry_per_actor
	from movies m2
    join movie_actor ma on m2.movie_id = ma.movie_id
);

-- Get me the movies sorted in descending order of their profit. Return movie_id, title, profit & studio columns
SELECT m.movie_id, m.title, 
(t1.revenue_mn_inr - t1.budget_mn_inr) AS profit, 
m.studio
FROM movies m
JOIN (
	select movie_id, 
    if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_mn_inr,
    if(currency = "USD", budget_mn*80, budget_mn) as budget_mn_inr
    from (
		select movie_id,
        case
			when unit="Billions" then revenue*1000
            when unit="Thousands" then revenue/1000
            else revenue
		end as revenue_mn,
        case
			when unit="Billions" then budget*1000
            when unit="Thousands" then budget/1000
            else budget
		end as budget_mn,
        currency
        from financials
    ) as t2
) as t1 ON m.movie_id = t1.movie_id
ORDER BY profit DESC;

