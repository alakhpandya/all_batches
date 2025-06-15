/*
Find Top 3 Highest-Paid Employees 
Question: Write a query to find the emp_id, first_name, last_name, and salary of the top 3 highest-paid employees in the company.
*/
USE hr;
select *
from employees
order by salary desc
limit 3;

/*
Find Department-wise Top Earners 
Question: Write a query to find the emp_id, first_name, last_name, and salary of the top 3 highest-paid employees in each department.
*/
select e1.first_name, e1.last_name, e1.salary, e1.department_id, count(e2.salary)
from employees e1
join employees e2
on e1.department_id = e2.department_id and e1.salary <= e2.salary
group by e1.first_name, e1.last_name, e1.salary, e1.department_id
having count(e2.salary) <= 3
order by e1.department_id, count(e2.salary);

/*
Employees with the Same Job as a Specific Employee
Question: Write a query to find the emp_id, first_name, and last_name of employees who have the same job_id as the employee with emp_id = 101.
*/
select employee_id, first_name, last_name 
from employees
where job_id = (
	select job_id from employees where employee_id = 101
)
and employee_id != 101;

/*
From moviesdb database print names of all the actors who are of age from 70 to 85 (including both). Use CTE method instead of subquery if needed.
*/
use moviesdb;
with t as (
	select *
	from actors
	where year(current_date()) - birth_year between 70 and 85
)
select t.actor_id, t.name, t.birth_year, count(ma.movie_id)
from t
left join movie_actor ma
on t.actor_id = ma.actor_id
group by t.actor_id, t.name, t.birth_year;

/*
Print the movies which produced more than 500% profit despite of having lower ratings than the average.
Formula to find percentage profit is: (Revenue – Budget) * 100 / Budget.
Use subquery if needed.
*/
with t1 as (
	select *, round((revenue - budget) * 100 / Budget, 2) as profit_pct
	from financials
),
t2 as (
	select *
	from t1
	where profit_pct >= 500
)
select *
from movies m
join t2
on m.movie_id = t2.movie_id
where imdb_rating < (select avg(imdb_rating) from movies);

/*
Return movie_id, title, studio, industry & profit columns from moviesdb database in descending order of profit. 
Hint: You will need to convert budget and revenue columns into Million INR so that you can compute profit by formula profit = revenue - budget.
*/
with t1 as (
	select movie_id,
		case
			when unit = "Billions" then budget*1000
			when unit = "Thousands" then budget/1000
			else budget
		end as budget_mn,
		case
			when unit = "Billions" then revenue*1000
			when unit = "Thousands" then revenue/1000
			else revenue
		end as revenue_mn,
		currency
	from financials
),
t2 as (
	select movie_id, 
		if(currency = "USD", budget_mn*80, budget_mn) as budget_adj,
		if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_adj
	from t1
),
t3 as (
	select movie_id, round(revenue_adj - budget_adj, 2) as profit_mn_inr
    from t2
)
select m.movie_id, m.title, m.studio, m.industry, t3.profit_mn_inr
from movies m
join t3
on m.movie_id = t3.movie_id
order by profit_mn_inr desc;

/*
Home work questions:
1. Find the most profitable orders. Orders which have higher sells price than the average sales price for their city and for which the deal size is not small 
are considered as ‘Most Profitable Orders’ (Use ‘demo’ database)
2. Find the difference in average sales for each month of 2003 and 2004 (Use ‘demo’ database)
*/

-- union & union all
/*
Find the popularity percentage for each user on Meta/Facebook. 
The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, then converted into a percentage by multiplying by 100. Output each user along with their popularity percentage. 
Order records in ascending order by user id.
*/
select * from facebook_friends
union all
select * from facebook_friends;

use moviesdb;
select actor_id, movie_id from movie_actor
union
select actor_id, name from actors;

use classwork;
select * from facebook_friends;

with t1 as (
	select user1, user2 from facebook_friends
	union
	select user2, user1 from facebook_friends
),
t2 as (
	select user1, count(user2) as friends 
	from t1
	group by user1
	order by user1
)
select distinct user1, round(friends*100/(select count(distinct(user1)) from t1), 2) as popularity_pct
from t2
order by user1;

-- select count(distinct(user1)) from t1;
use demo;
select * from products;

/*
Identify how many cars, motorcycles, trains and ships are available in the inventory. 
Treat all types of cars just as “Cars”. DO NOT USE ‘LIKE’ IN THIS EXAMPLE. (Use ‘demo’ database)
*/
select 
	case
		when product_line in ("Classic Cars", "Vintage Cars") then "Cars"
		else product_line
	end as new_product_line,
    count(*) as count 
from products
group by new_product_line;

-- using union/union all
select product_line, count(*) as count
from products
where product_line not in ("Classic Cars", "Vintage Cars")
group by product_line
union
select "cars" as new_product_line, count(*) as count
from products
where product_line in ("Classic Cars", "Vintage Cars")
group by new_product_line;


use paintings;
select * from artists;
select * from sales;
select * from paintings;
/*
Display all the available paintings and their artists. 
If a painting was sold then mark them as "Sold" and if more than 1 painting of an artist are sold then display a "**" beside their name.
*/