-- Aggregate Window Functions: avg(), min(), max(), sum(), count()
use moviesdb;
select movie_id, title, imdb_rating, studio,
avg(imdb_rating) over(partition by studio) as studio_avg_rating,
min(imdb_rating) over(partition by studio) as studio_min_rating,
max(imdb_rating) over(partition by studio) as studio_max_rating,
count(imdb_rating) over(partition by studio) as studio_count,
sum(imdb_rating) over(partition by studio) as meaning_less_sum
from movies;

-- Ranking Window Functions
use hr2;
select employee_id, first_name, last_name, salary, manager_id, department_id,
-- row_number() over()
row_number() over(partition by department_id)
from employees;

use classwork;
select *,
-- row_number() over(partition by dep_name)
row_number() over(partition by dep_name order by student_name) as roll_number
from student_score;
-- order by student_name;

-- get me the top 3 earners from each department
use hr2;
with t as (
	select employee_id, first_name, last_name, salary, manager_id, department_id,
	row_number() over(partition by department_id order by salary desc) as salary_rank
	from employees
)
select *
from t;
-- where salary_rank <= 3;

with t as (
	select employee_id, first_name, last_name, salary, manager_id, department_id,
	rank() over(partition by department_id order by salary desc) as salary_rank
	from employees
)
select *
from t
where salary_rank <= 3;

-- In painting dataset, find out the duplicated artists names and id using row_number() window function
use paintings;
select id, first_name, last_name
from (
	select *,
	row_number() over(partition by first_name, last_name order by id) as "repeat"
	from artists
) as t
where t.repeat > 1;

use hr2;
select employee_id, first_name, last_name, salary, manager_id, department_id,
rank() over(partition by department_id order by salary desc) as competition_rank,
dense_rank() over(partition by department_id order by salary desc) as "dense_rank"
from employees;

use classwork;
select *,
percent_rank() over(partition by dep_name order by score) as percentile
from student_score;

select *,
-- ntile(2) over() as "group"
-- ntile(3) over() as "group"
-- ntile(2) over(partition by dep_name) as "group"
ntile(2) over(partition by dep_name order by score) as "group"
from student_score;

-- Value Window Functions

-- Aggregate Window Function - Something new