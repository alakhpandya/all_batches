-- Opening Question: Get me the top 2 earners from each department

-- Introduction to window functions
-- Print average salary beside every row of employees table
use hr;
with t1 as (
	select avg(salary) as company_avg_salary from employees
)
select employee_id, first_name, last_name, salary as emp_salary, t1.company_avg_salary
from employees
cross join t1;

select employee_id, first_name, last_name, salary as emp_salary,
-- avg(salary) over() as company_avg_salary
round(avg(salary) over(), 0) as company_avg_salary
from employees;

-- Print avg salary of each department beside every row of employees table
select employee_id, first_name, last_name, salary as emp_salary, department_id,
avg(salary) over(partition by department_id) as dep_avg_salary
from employees;

-- Print avg_price of each product line beside every row of products table from demo database.
use demo;
select *,
avg(price) over(partition by product_line) as avg_price
from products;

-- Print the total salary paid to each department beside all the rows of employees table
use hr;
select employee_id, first_name, last_name, salary as emp_salary, department_id,
-- sum(salary) over()
sum(salary) over(partition by department_id) as dep_total_salary
from employees;

-- Print the highest imdb_rating beside each row of movies table.
use moviesdb;
select *, 
max(imdb_rating) over()
from movies;

-- Print the minimum, maximum & average imdb_rating of each industry beside every row of movies table.
select *,
min(imdb_rating) over(partition by industry) as industry_min_rating,
max(imdb_rating) over(partition by industry) as industry_max_rating,
round(avg(imdb_rating) over(partition by industry), 1) as industry_avg_rating
from movies;

-- Print number of movies produced by each studio beside all the rows of movies table.
select *,
count(*) over(partition by studio) as no_of_movies
from movies;

use classwork;
select * from student_score;
-- Suppose I want to give department wise roll numbers to the students
select *,
-- row_number() over() as sr_no,
row_number() over(partition by dep_name order by student_name) as roll_no
from student_score;
-- order by dep_name, student_name;

-- What if I want to rank students based on their marks?
select *,
row_number() over(partition by dep_name order by score desc) as student_rank
from student_score;

-- Get me the top 3 earners from each department. Return columns: employee_id, first_name, last_name, salary and department_id. Use hr dataset.
use hr;
select employee_id, first_name, last_name, salary, department_id,
row_number() over(partition by department_id order by salary desc) as earner_rank
from employees;

select *
from (
	select employee_id, first_name, last_name, salary, department_id,
	row_number() over(partition by department_id order by salary desc) as earner_rank
	from employees
) t
where earner_rank <= 3;

with t as (
	select employee_id, first_name, last_name, salary, department_id,
	row_number() over(partition by department_id order by salary desc) as earner_rank
	from employees
)
select * from t
where earner_rank <= 3;

-- We should better use rank() window function
with t as (
	select employee_id, first_name, last_name, salary, department_id,
	rank() over(partition by department_id order by salary desc) as earner_rank
	from employees
)
select * from t
where earner_rank <= 3;

select employee_id, first_name, last_name, salary, department_id,
rank() over(partition by department_id order by salary desc) as competetion_rank,  -- competition rank
dense_rank() over(partition by department_id order by salary desc) as "dense_rank" 	-- Dense Rank
from employees;

use classwork;
select *,
percent_rank() over(partition by dep_name order by score) as "percent_rank" 
from student_score;

-- There are 200 seats & 10,000 students are competing for the entrance exam. What should be your minimum percentile to secure the seat?

select *,
ntile(2) over(partition by dep_name order by score) as team_no
from student_score
order by dep_name;

use moviesdb;
select *,
ntile(4) over(order by imdb_rating, release_year) as team
from movies;

-- Get top earner from each department & then return only top 5 amongst them
use hr;
with t1 as (
	select employee_id, first_name, last_name, salary, department_id,
	rank() over(partition by department_id order by salary desc) as earner_rank
	from employees
)
select * from t1
where earner_rank = 1
order by salary desc
limit 5;

-- Print the top 3 earners from each department. Return columns: employee_id, first_name, last_name, salary, department_name. Use hr dataset.

-- Fetch two employees from each department who joined first along with their job_title, department_name and region_name. Use hr2 database.
