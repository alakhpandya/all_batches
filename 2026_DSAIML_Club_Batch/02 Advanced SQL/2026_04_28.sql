/*
Return movie_id, budget_adj, revenue_adj columns from financial table of moviesdb database where budget_adj and revenue_adj are budget & revenue converted into Million INR.
*/
use moviesdb;

select movie_id,
case
	when unit="Billions" then budget_inr*1000
    when unit="Thousands" then budget_inr/1000
    else budget_inr
end as budget_adj,
case
	when unit="Billions" then revenue_inr*1000
    when unit="Thousands" then revenue_inr/1000
    else revenue_inr
end as revenue_adj
from (
	select movie_id,
	if(currency="USD", budget*80, budget) as budget_inr,
	if(currency="USD", revenue*80, revenue) as revenue_inr,
	unit
	from financials
) t;

/*
Print the movie titles, industry and profit of each movie. Sort the result in descending order of profit (profit = revenue – budget). 
Clean the revenue & budget so that it becomes easy to compare the profit each movie did 
(Hint: both of them must be in the same currency and in the same unit (thousand/million/billion etc) to compute the profit.)
*/
select m.movie_id, title, 
revenue_adj - budget_adj as profit_mn_inr, industry
from movies m
join (
	select movie_id,
	case
		when unit="Billions" then budget_inr*1000
		when unit="Thousands" then budget_inr/1000
		else budget_inr
	end as budget_adj,
	case
		when unit="Billions" then revenue_inr*1000
		when unit="Thousands" then revenue_inr/1000
		else revenue_inr
	end as revenue_adj
	from (
		select movie_id,
		if(currency="USD", budget*80, budget) as budget_inr,
		if(currency="USD", revenue*80, revenue) as revenue_inr,
		unit
		from financials
	) t1
) f
on m.movie_id = f.movie_id
order by 3 desc;

-- Write a query to display the department_id, emp_id, first_name, last_name, and salary of employees who earn the highest salary in their respective departments.
use hr;
select e.department_id, employee_id as emp_id, first_name, last_name, salary, dep_max_sal
from employees e
join (
	select department_id, max(salary) as dep_max_sal
	from employees
	group by department_id
) as d
on e.department_id = d.department_id
where e.salary = d.dep_max_sal
order by 1;

-- C.T.E. = Common Table Expression
with d as (
	select department_id, max(salary) as dep_max_sal
	from employees
	group by department_id
)
select e.department_id, employee_id as emp_id, first_name, last_name, salary, dep_max_sal
from employees e
join d on e.department_id = d.department_id
where e.salary = d.dep_max_sal
order by 1;

-- Print the employees who are earning more than the average salary of their department
use hr;
with t as (
	select department_id, avg(salary) as dep_avg_sal
    from employees
    group by department_id
)
select *
from employees e
join t on e.department_id = t.department_id
where e.salary > t.dep_avg_sal;

-- From moviesdb database print names of all the actors who are of age from 70 to 85 (including both). Use CTE method instead of subquery if needed.
use moviesdb;
select *, 2025-birth_year as age
from actors
where 2025-birth_year between 70 and 85;

/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ 
(Use ‘demo’ database)
*/
use demo;
with cte as (
	select c.city, avg(so.sales) as city_avg
	from customers c
	join sales_order so on c.customer_id = so.customer
	group by c.city
)
-- select so.*, c.city, cte.city_avg
select so.*
from sales_order so
join customers c on so.customer=c.customer_id
join cte on c.city = cte.city
where so.sales > cte.city_avg and so.deal_size <> "Small";