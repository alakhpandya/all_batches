use moviesdb;

select * from movies;

/*
Please print the average ratings of each industry as an extra column named "Avg Industry Rating" in this table.
*/

with t1 as
(
	select industry, round(avg(imdb_rating), 2) as "Avg Industry Rating"
	from movies
	group by industry
)
select *
from movies m
join t1 on m.industry = t1.industry;

-- Window functions
select *,
row_number() over() as row_num
from movies;

use paintings;
delete from artists
where id in
(
	select row_num
	from
	(
		select id,
		row_number() over(partition by first_name, last_name) as row_num
		from artists
	) as t1
	where row_num > 1
);
select * from artists;

use classwork;
select *,
-- row_number() over(partition by dep_name order by student_name) as row_num
row_number() over(partition by dep_name order by score desc) as row_num
from student_score
order by dep_name, student_name;

