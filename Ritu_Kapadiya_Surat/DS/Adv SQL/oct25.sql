use moviesdb;
select * from financials;
select * from movies;
-- Give me movies rankes as per their ratings for each studio seperately


use paintings;

update artists
SET id = 2
where first_name = "Kate";

update artists
SET id = 3
where first_name = "Natali";

SELECT *
FROM artists;

with t1 as (
	select id, first_name, last_name, row_number() over() as row_id
	from artists
)
select *
from t1;

with t1 as (
	select first_name, last_name, count(id) as nos
	from artists
	group by first_name, last_name
	having count(id) > 1
)
delete from artists
where id in (select nos from t1);


select title, studio, imdb_rating,
row_number() over(partition by studio order by imdb_rating desc) as 'rank'
from movies
order by studio;

select studio, title, imdb_rating,
rank() over(partition by studio order by imdb_rating desc) as 'rank',
dense_rank() over(partition by studio order by imdb_rating desc) as 'dense rank'
from movies
order by studio;

use classwork;
select * from student_score;

-- Print average score of each department
select *,
avg(score) over(partition by dep_name) as avg_score
from student_score
order by dep_name;

-- Print the maximum & minimum scores of each department along with the names of every student
select *,
max(score) over(partition by dep_name) as max_score,
min(score) over(partition by dep_name) as min_score,
avg(score) over(partition by dep_name) as avg_score
from student_score
order by dep_name, score;

-- Lead & Lag
select *,
-- LEAD(score) OVER(),
-- LEAD(score) OVER(PARTITION BY dep_name)
LEAD(score) OVER(PARTITION BY dep_name order by score) AS next_score
from student_score
order by dep_name;

select *,
LAG(score) OVER(PARTITION BY dep_name ORDER BY score desc) as prev_score
from student_score
order by dep_name;

