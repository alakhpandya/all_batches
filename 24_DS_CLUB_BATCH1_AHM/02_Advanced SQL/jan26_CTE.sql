-- CTE: Common Table Expression
/*
Print the employees who are earning more than the average salary of their department using CTE
*/
with t as (
	select department_id, avg(salary) as dep_avg_salary 
	from employees
	group by department_id
)

select e.employee_id, e.first_name, e.last_name, e.salary, t.department_id, t.dep_avg_salary
from employees e
join t
on e.department_id = t.department_id
where e.salary > t.dep_avg_salary
order by t.department_id;

-- Print the movie titles, industry and revenue. Sort the result in descending order of profit (profit = revenue – budget) using CTE
use moviesdb;
WITH t1 as (
	select movie_id, currency,
	if(unit = "Billions", budget*1000, if(unit = "Thousands", budget/1000, budget)) as budget_mn,
	if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as revenue_mn
	from financials
),
t2 as (
	select movie_id,
	if(currency = "USD", budget_mn*80, budget_mn) as budget_mn_inr,
	if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_mn_inr
	from t1
)
select m.movie_id, m.title, m.industry, 
t2.revenue_mn_inr - t2.budget_mn_inr as profit
from movies m
join t2
on m.movie_id = t2.movie_id
order by 4 desc;


-- We cannot use CTE inside 'where' clause:
use hr2;

with cte as (
	select distinct manager_id
	from employees
)
select *
from employees
where employee_id in cte;

/*
Print the movies which produced 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: (Revenue – Budget) * 100 / Budget
*/
use moviesdb;
WITH t1 as (
	select movie_id, currency,
	if(unit = "Billions", budget*1000, if(unit = "Thousands", budget/1000, budget)) as budget_mn,
	if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as revenue_mn
	from financials
),
t2 as (
	select movie_id,
	if(currency = "USD", budget_mn*80, budget_mn) as budget_mn_inr,
	if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_mn_inr
	from t1
),
t3 as (
	select m.movie_id, m.title, m.industry, 
	(t2.revenue_mn_inr - t2.budget_mn_inr)*100/t2.budget_mn_inr as profitability,
    m.imdb_rating
	from movies m
	join t2
	on m.movie_id = t2.movie_id
	where m.imdb_rating < ( select avg(imdb_rating) from movies)
	order by 4 desc
)
select * from t3
where profitability > 500;

/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ 
(Use ‘demo’ database)
*/
use demo;
with t1 as (
	select order_number, sales, so.customer, deal_size, city 
	from sales_order so
	join customers c
	on so.customer = c.customer_id
),
t2 as (
	select city, avg(sales) as city_avg
	from t1
	group by city
)
select order_number, sales, customer, deal_size, t1.city, city_avg
from t1
join t2 
on t1.city = t2.city
where deal_size <> "Small" and sales > city_avg;

-- HW- Find the difference in average sales for each month of 2003 and 2004 (Use ’demo’ database)