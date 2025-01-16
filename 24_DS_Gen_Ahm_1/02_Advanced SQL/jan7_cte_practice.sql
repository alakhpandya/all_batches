use moviesdb;
/*
2. Print the movies which produced 500% profit despite of having lower ratings than the average.
Formula to find percentage profit is: (Revenue – Budget) * 100 / Budget
*/

select title, profit_pct
from (
	select m.title, (f.revenue - f.budget)*100/f.budget as profit_pct
	from movies m
	join financials f
	on m.movie_id = f.movie_id
) as t
where profit_pct >= 1500;

with t1 as (
	select m.title, m.imdb_rating, (f.revenue - f.budget)*100/f.budget as profit_pct
	from movies m
	join financials f
	on m.movie_id = f.movie_id
),
t2 as (
	select title, imdb_rating, profit_pct
    from t1
    where imdb_rating < (select avg(imdb_rating) from movies)
)
select title, profit_pct
from t2
where profit_pct >= 500;

-- Window functions
-- Display average rating of each studio.
-- Print "below avg"/"above avg" beside each movie depending on if their rating were below or above the average rating of their studio.
select * from movies;

use classwork;
select * 
from student_score
order by dep_name, score desc;

select *,
row_number() over()
from student_score;

use moviesdb;
select *,
round(avg(imdb_rating) over(partition by studio), 1) as studio_avg
from movies
order by movie_id;

use classwork;
select *,
row_number() over(partition by dep_name) as row_num
from student_score;

select *,
-- row_number() over(partition by dep_name order by score desc) as row_num
-- rank() over(partition by dep_name order by score desc) as ranking
dense_rank() over(partition by dep_name order by score desc) as ranking
from student_score;

use paintings;
select * from artists;
-- print the names of the artists who are duplicated.

with cte as
(
	select *,
	row_number() over(partition by first_name, last_name) as row_num
	from artists
)
select id, first_name, last_name
from cte
where row_num > 1;