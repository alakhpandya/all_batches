/*
Q2.List the Top 3 Highest RATED Movies in Each Studio
   Using a CTE, find the top 3 highest-rated movies for each Studio.
*/
use moviesdb;

with cte as (
	select m1.studio, m1.title,  m1.imdb_rating
    from movies m1
    where (
		select count(*)
        from movies m2
        where m2.studio = m1.studio and m2.imdb_rating > m1.imdb_rating
    ) < 3
)

select *
from cte
order by studio, imdb_rating desc;