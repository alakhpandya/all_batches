-- Solution to homework questions
/*
1. Find the most profitable orders. Orders which have higher sells price than the average sales price for their city and for which the deal size is not small 
are considered as ‘Most Profitable Orders’ (Use ‘demo’ database)
*/
use demo;
select * from sales_order;
select * from customers;

with cte1 as (
	select order_number, sales, deal_size, city
	from sales_order so
	join customers c
	on so.customer = c.customer_id
),
cte2 as (
	select city, avg(sales) as city_avg
	from cte1
	group by city
)
select order_number, sales, deal_size, cte1.city
from cte1
join cte2
on cte1.city = cte2.city
where sales > city_avg and deal_size <> "Small";

-- Give me the artist names appearing more than once in paintings database
use paintings;
select first_name, last_name
from artists
group by first_name, last_name
having count(*) > 1;

-- Print movie_id, title, industry, imdb_rating, studio & average rating of that studio from the movies table of moviesdb database.
use moviesdb;
with t1 as (
	select studio, round(avg(imdb_rating), 1) as studio_avg_rating
    from movies
    group by studio
)
select movie_id, title, industry, imdb_rating, m.studio, studio_avg_rating
from movies m
join t1
on m.studio = t1.studio;

-- Window Functions
use classwork;
select * from student_score;

select *,
row_number() over(partition by dep_name) as roll_no
from student_score;

-- Give me the artist names appearing more than once in paintings database
use paintings;

with t1 as (
	select *,
	row_number() over(partition by first_name, last_name) as count
	from artists
)
select * from t1
where count > 1;

-- Give department-wise roll numbers in ascending order of their names
select *,
row_number() over(partition by dep_name order by student_name) as roll_no
from student_score;

-- Find out top-2 earners from each department in hr2 database
use hr2;
with t1 as (
	select *,
	row_number() over(partition by department_id order by salary desc) as earner_rank
	from employees
)
select employee_id, first_name, last_name, salary, department_id, earner_rank
from t1;

select employee_id, first_name, last_name, salary, department_id,
rank() over(partition by department_id order by salary desc) as earner_rank,
dense_rank() over(partition by department_id order by salary desc) as earner_dense_rank
from employees;

-- Percent_rank
use classwork;
select * from student_score;
select *,
percent_rank() over(partition by dep_name order by score) as percentile
from student_score;

-- We want to create two teams of students in each department. If the number of students in a department is odd then first team may have 1 student more than the second team.
use classwork;
select * from student_score;
select *,
ntile(2) over(partition by dep_name) as Team,
ntile(2) over(partition by dep_name order by score) as New_team
from student_score;

-- Print movie_id, title, industry, imdb_rating, studio & average rating of that studio from the movies table of moviesdb database.
use moviesdb;
select movie_id, title, industry, imdb_rating, studio,
avg(imdb_rating) over() as total_average,
avg(imdb_rating) over(partition by studio) as studio_average,
avg(imdb_rating) over(partition by studio order by imdb_rating) as studio_moving_average,
max(imdb_rating) over(partition by studio) as studio_max_rating,
max(imdb_rating) over(partition by studio order by imdb_rating) as studio_moving_max_rating,
count(*) over(partition by studio) as no_of_movies
from movies;

with t1 as (
	select m.movie_id, title, industry, imdb_rating, studio, budget, revenue, release_year
    from movies m
    left join financials f
    on m.movie_id = f.movie_id
)
select *,
-- sum(budget) over(partition by studio) as studio_total_expenditures,
-- sum(revenue) over(partition by studio) as studio_total_collection,
sum(budget) over(partition by studio order by release_year) as running_total_expenses,
sum(revenue) over(partition by studio order by release_year) as running_total_income
from t1;

-- lead, lag, first_value, last_value, nth_value
use classwork;
select *,
-- lead(score) over() as next_students_score
lead(score) over(partition by dep_name) as next_students_score,
lag(score) over(partition by dep_name order by score) as prev_students_score
from student_score;

use hr2;
select *,
-- lead(salary, 2) over(partition by department_id)
first_value(salary) over(partition by department_id) as dep_first_salary,
last_value(salary) over(partition by department_id) as dep_last_salary,
nth_value(salary, 3) over(partition by department_id) as dep_3rd_salary
from employees;


-- Frames in window functions
use hr2;
select *,
-- sum(salary) over(partition by department_id order by salary rows between 1 preceding and current row) as dep_running_total
-- sum(salary) over(partition by department_id rows between unbounded preceding and unbounded following) as dep_total
-- sum(salary) over(partition by department_id rows between 1 preceding and 2 following) as dep_total
-- avg(salary) over(partition by department_id rows between 1 preceding and 2 following) as dep_total
sum(salary) over(partition by department_id order by salary rows between unbounded preceding and unbounded following) as dep_running_total
from employees;


-- full outer join: do full outer join of employees & departments table to show the employees without department & departments without employees both

select *
from employees
where department_id is null;

select *
from employees e
left join departments d
on e.department_id = d.department_id
where e.department_id is null
union
select *
from employees e
right join departments d
on e.department_id = d.department_id
where e.department_id is null;

-- Get google_gmail, player & student datasets & load them into classwork.
/*
Find the number of emails received by each user under each built-in email label. The email labels are: ‘Promotion’, ‘Social’ and ‘Shopping’. 
Output the user along with the number of promotion, social & shopping emails they got.
*/

use farmers_market;
select vendor_id, max(original_price)
from vendor_inventory
group by vendor_id;