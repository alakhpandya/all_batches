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
select *,
-- first_value(student_name) over(partition by dep_name) as first_student
-- first_value(student_name) over(partition by dep_name order by student_name) as first_student
-- first_value(student_name) over(partition by dep_name order by score desc) as first_student,
-- last_value(student_name) over(partition by dep_name) as last_student,
-- nth_value(student_name, 2) over(partition by dep_name) as "2nd_student",
-- lead(student_name) over() as "lead",		-- shift up
-- lead(student_name, 2) over() as "lead 2"
-- lead(student_name) over(partition by dep_name) as "dep_lead"
-- lag(student_name) over() as "lag"		-- shift down
-- lag(student_name, 2) over() as "lag 2"
lag(student_name) over(partition by dep_name) as "dep_lag"
from student_score;

-- Print the total salary paid to each department along with all the columns of employees table in hr database
use hr;
select *,
sum(salary) over(partition by department_id) as total_salary_paid
from employees;

-- Print 5 most profitable movies of each industry using moviesdb database
use moviesdb;
with t1 as (
	select movie_id, if(currency="INR", budget, budget*80) as budget_inr,
    if(currency="INR", revenue, revenue*80) as revenue_inr,
    unit
    from financials
), t2 as (
	select movie_id,
    case 
		when unit="Billions" then revenue_inr*1000
        when unit="Thousands" then revenue_inr/1000
        else revenue_inr
	end 
    -
    case 
		when unit="Billions" then budget_inr*1000
        when unit="Thousands" then budget_inr/1000
        else budget_inr
	end 
    as profit_mn_inr
    from t1
), t3 as (
	select m.*, t2.profit_mn_inr,
	rank() over(partition by industry order by profit_mn_inr desc) as movie_rank
	from movies m
	left join t2 on m.movie_id=t2.movie_id
)
select *
from t3
where movie_rank <= 5;

-- Fetch two employees from each department who joined first along with their job_title, department_name and region_name. Use hr2 database.
use hr2;
with t1 as (
	select *,
    rank() over(partition by department_id order by hire_date) as employee_joining_order
    from employees
), t2 as (
	select t1.*, j.job_title
    from t1
    left join jobs j on t1.job_id = j.job_id
    where employee_joining_order <= 2
)
select t2.employee_id, first_name, last_name, hire_date, job_id, job_title, t2.department_id, r.region_name
from t2
left join departments d on t2.department_id = d.department_id
left join locations l on d.location_id = l.location_id
left join countries c on l.country_id = c.country_id
left join regions r on c.region_id = r.region_id;

-- Get top earner from each department & then return only top 5 amongst them. Use hr2 database.
with t as (
	select *,
	max(salary) over(partition by department_id) as department_highest_salary
	from employees
)
select *
from t
where salary = department_highest_salary
order by salary desc
limit 5;

-- Swap the names of each two adjacent students. Use students table from classwork database.
use classwork;
select * 
from students;

-- Aggregate Window Function - Something new
