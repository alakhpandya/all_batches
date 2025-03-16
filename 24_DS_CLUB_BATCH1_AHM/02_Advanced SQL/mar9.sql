use moviesdb;

select * from movies;

/*
Print movie_id, title, industry, imdb_rating, studio & average rating of that studio from the movies table of moviesdb database.
*/

select movie_id, title, industry, imdb_rating, studio,
(select avg(imdb_rating) from movies m where movies.studio=m.studio) studio_rating_avg 
from movies;

with t1 as (
	select studio, avg(imdb_rating) as average_rating 
	from movies
	group by studio
)
select m.movie_id, m.title, m.industry, m.imdb_rating, m.studio, rm.average_rating
from movies m
join t1 rm on m.studio = rm.studio;

-- Window functions
use paintings;
select * from artists;
-- Row Number window function
select id, first_name, last_name,
row_number() over()
from artists;

select id, first_name, last_name,
row_number() over(partition by first_name, last_name)
from artists;

-- Show artists whose names are duplicating
with t1 as (
	select id, first_name, last_name,
	row_number() over(partition by first_name, last_name) as r
	from artists
)
select id, first_name, last_name
from t1
where r > 1;

use classwork;
select * from student_score;

use hr;
select * from employees
where department_id = 6
order by salary desc;
select count(distinct(department_id)) from employees;

-- Get me the names, salary & department_id of top 3 employees from each department
with cte as
(
select employee_id, first_name, last_name, department_id, salary,
row_number() over(partition by department_id) as row_num
from employees
)
select * from cte
where row_num <= 3;

select employee_id, first_name, last_name, department_id, salary,
row_number() over(partition by department_id order by salary desc) as row_num
from employees;
-- order by department_id asc, salary desc;

with cte as
(
select employee_id, first_name, last_name, department_id, salary,
row_number() over(partition by department_id order by salary desc) as row_num
from employees
)
select * from cte
where row_num <= 3;

-- Window function: Rank
with cte as
(
select employee_id, first_name, last_name, department_id, salary,
rank() over(partition by department_id order by salary desc) as ranking
from employees
)
select * from cte
where ranking <= 3;

with cte as
(
select employee_id, first_name, last_name, department_id, salary,
rank() over(partition by department_id order by salary desc) as ranking
from employees
)
select * from cte
where ranking <= 4;

-- Dense Rank
with cte as
(
select employee_id, first_name, last_name, department_id, salary,
dense_rank() over(partition by department_id order by salary desc) as ranking
from employees
)
select * from cte;

-- Window Function - Percent Rank
use classwork;
select * from student_score;

select *, percent_rank() over(partition by dep_name order by score) as percentile
from student_score;

-- Window Function - NTILE
select *,
-- ntile(2) over() as group_no
-- ntile(2) over(partition by dep_name) as group_no
-- ntile(2) over(partition by dep_name order by score desc) as group_no
ntile(2) over(order by score) as group_no
from student_score;