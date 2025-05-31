use moviesdb;
select * from financials;
-- task-1: In the financial table, create a new column of "profit" after converting all movies into the same unit & the same currency.

select m.movie_id, m.title, m.studio, m.imdb_rating, t3.profit
from movies m
join (
	select movie_id, revenue_mn_USD - budget_mn_USD as profit
	from (
		select movie_id, 
		round(if(currency="INR", budget_mn/80, budget_mn), 2) as budget_mn_USD,
		round(if(currency="INR", revenue_mn/80, revenue_mn), 2) as revenue_mn_USD
		from (
			select movie_id,
			if(unit="Billions", budget*1000, if(unit="Thousands", budget/1000, budget)) as budget_mn,
			if(unit="Billions", revenue*1000, if(unit="Thousands", revenue/1000, revenue)) as revenue_mn,
			currency
			from financials
		) t1
	) t2
) t3
on m.movie_id = t3.movie_id
order by t3.profit desc;

-- C.T.E. = Common Table Expression
/*
Print the employees who are earning more than the average salary of their department using CTE
*/
use hr2;
with cte as (
	select department_id, avg(salary) as dep_avg_salary 
	from employees
	group by department_id
)

select e.employee_id, e.first_name, e.last_name, e.salary, cte.department_id, cte.dep_avg_salary
from employees e
join cte
on e.department_id = cte.department_id
where e.salary > cte.dep_avg_salary
order by cte.department_id;

-- Creating multiple CTEs:
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

/*
Using moviesdb dataset, print the id, title, imdb_rating, studio & profit of each movie. 
Sort your result in the descending order of profit. Hint: profit of a movie is its revenue - budget.
*/
WITH t1 as
(
	select movie_id,
	if(unit="Billions", budget*1000, if(unit="Thousands", budget/1000, budget)) as budget_mn,
	if(unit="Billions", revenue*1000, if(unit="Thousands", revenue/1000, revenue)) as revenue_mn,
	currency
	from financials
)
select movie_id, 
round(if(currency="INR", budget_mn/80, budget_mn), 2) as budget_mn_USD,
round(if(currency="INR", revenue_mn/80, revenue_mn), 2) as revenue_mn_USD
from t1;

with t1 as (
	select movie_id,
	if(unit="Billions", budget*1000, if(unit="Thousands", budget/1000, budget)) as budget_mn,
	if(unit="Billions", revenue*1000, if(unit="Thousands", revenue/1000, revenue)) as revenue_mn,
	currency
	from financials
),
t2 as (
	select movie_id, 
	round(if(currency="INR", budget_mn/80, budget_mn), 2) as budget_mn_USD,
	round(if(currency="INR", revenue_mn/80, revenue_mn), 2) as revenue_mn_USD
	from t1
),
t3 as (
	select movie_id, revenue_mn_USD - budget_mn_USD as profit
    from t2
)
select  m.movie_id, m.title, m.studio, m.imdb_rating, t3.profit
from movies m
join t3
on m.movie_id = t3.movie_id
order by t3.profit desc;