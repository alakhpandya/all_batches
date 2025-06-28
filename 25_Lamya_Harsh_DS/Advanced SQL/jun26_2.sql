-- Write a query to find the emp_id, first_name, last_name, and department_id of employees who are managers (their emp_id is referenced as manager_id in the table)
use hr;
with cte as (
	select distinct manager_id from employees
)
select *
from employees
where employee_id in (select * from cte);

/*
Print the movies which produced more than 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: profit * 100 / Budget
*/
use moviesdb;

SELECT title, industry, imdb_rating, profit, profit_pct
from (
	SELECT title, industry, imdb_rating, revenue_adj - budget_adj as profit, (revenue_adj - budget_adj)*100/budget_adj as profit_pct
	FROM movies m
	JOIN
		(SELECT movie_id,
				budget * IF(unit = 'Billions', 1000, IF(unit = 'thousands', .001, 1)) * IF(currency = 'USD', 80, 1) budget_adj,
				revenue * IF(unit = 'Billions', 1000, IF(unit = 'thousands', .001, 1)) * IF(currency = 'USD', 80, 1) revenue_adj
		FROM financials
		) f 
	USING (movie_id)
	where imdb_rating < (SELECT avg(imdb_rating) from movies)
) as m2
where profit_pct > 500;

-- Using multiple CTEs
with f as (
	SELECT movie_id,
	budget * IF(unit = 'Billions', 1000, IF(unit = 'thousands', .001, 1)) * IF(currency = 'USD', 80, 1) budget_adj,
	revenue * IF(unit = 'Billions', 1000, IF(unit = 'thousands', .001, 1)) * IF(currency = 'USD', 80, 1) revenue_adj
	FROM financials
),
m2 as (
	SELECT title, industry, imdb_rating, revenue_adj - budget_adj as profit, (revenue_adj - budget_adj)*100/budget_adj as profit_pct
	FROM movies m
	JOIN f 
	USING (movie_id)
	where imdb_rating < (SELECT avg(imdb_rating) from movies)
)
SELECT title, industry, imdb_rating, profit, profit_pct
from m2
where profit_pct > 500;

/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as 
‘Most Profitable Orders’ (Use ‘demo’ database)
*/
use demo;
with t1 as (
	select city, avg(sales) city_avg
	from sales_order so
	join customers c
	on so.customer = c.customer_id
	group by city
), 
t2 as (
	select order_number, sales, city, deal_size
	from sales_order so
	join customers c
	on so.customer = c.customer_id
)
select order_number, sales, t2.city, deal_size 
from t2
join t1
on t1.city = t2.city
where sales > city_avg and deal_size != "Small";