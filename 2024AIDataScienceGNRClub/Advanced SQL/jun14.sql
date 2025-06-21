
/*
Give department-wise roll number to each student. For example, students in Biochemistry department will have roll numbers 1, 2 & 3 (as there are only 3 students in this
department) then students of Computer Science department will have roll numbers 1, 2, 3 & 4 and so on.
*/
use classwork;
select * from student_score;

select *,
row_number() over(partition by dep_name order by student_name) as roll_no
from student_score;

-- Print top-3 earners from each department. Use hr2
USE HR2;
with t1 as (
	select *,
	row_number() over(partition by department_id order by salary desc) as row_num
	from employees
)
select * from t1
where row_num <= 3;

select *,
rank() over(partition by department_id order by salary desc) as earner_rank,
dense_rank() over(partition by department_id order by salary desc) as earner_dense_rank
from employees;

use classwork;
select *,
percent_rank() over(partition by dep_name order by score) as percentile 
from student_score;

select * from student_score
order by dep_name;

select *,
ntile(2) over(partition by dep_name order by score) as team_no
from student_score;

-- Print average imdb_rating for each studio in the movies table beside each movie.
use moviesdb;
select *,
round(avg(imdb_rating) over(), 1) as total_avg_rating,
round(avg(imdb_rating) over(partition by studio), 1) as studio_avg_rating
from movies;

-- Print studio-wise average budget & average revenue along with movie_id, title, industry, release_year, studio, imdb_rating, unit & currency.


-- Print minimum & maximum salaries of each department in employees table of hr database.

/*
Print all the columns of employee table of hr database and also add a column that has "above average", "average" or "below average" for the employees
whose salaries are higher, same or less than average salary of their respective departments.
*/
use  hr;

with t1 as (
	select *,
	avg(salary) over(partition by department_id) as dep_avg_sal
	from employees
)
select *,
case 
	when salary > dep_avg_sal then "above average"
    when salary = dep_avg_sal then "average"
    else "below average"
end as "type"
from t1;