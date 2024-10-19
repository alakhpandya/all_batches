use demo;

-- select "Mode of shipping" as MoS, product_line, count(*)
select product_line, count(*)
from products
where product_line not in ("Classic Cars", "Vintage Cars")
group by product_line;

select "Cars" as product_line, count(*) as cnt
from products
where product_line in ("Classic Cars", "Vintage Cars");

use paintings;
select * from paintings;

select * from artists;
-- Give me the artist name that appears more than once
use paintings;
select *, 
row_number() over(partition by id, first_name, last_name) as occurance
from artists;

-- Print the movies table with the following columns: movie_id, title, industry, imdb_rating and industry_avg_imdb_rating rounded off after 1 decimal place.

-- Introduction to window functions:
use moviesdb;
select *,
row_number() over(partition by studio)
from movies
order by studio;

-- Get me the top 2 employees with highest salaries in their department
use hr;
select * from employees;
select employee_id,first_name, last_name, department_id, salary,
row_number() over(partition by department_id order by salary desc) as toppers
from employees
order by employee_id;

with t1 as
(
	select employee_id,first_name, last_name, department_id, salary,
	row_number() over(partition by department_id order by salary desc) as toppers
	from employees
)
select * from t1
where toppers < 3;

-- Print the top 3 students from each department