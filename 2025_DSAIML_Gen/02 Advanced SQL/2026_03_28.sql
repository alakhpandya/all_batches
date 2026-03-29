/*
Calculate the running total of salary in the ascending order of seniority of the employees separately for each department from 'hr2' database. Give your answer rounded off after two decimal place. 
Show employee_id, first_name, last_name, department_name, salary & running_total_salary columns.
*/
use hr2;
select  employee_id, first_name, last_name, hire_date, department_name, salary, 
sum(salary) over(partition by e.department_id order by hire_date)
as running_total_salary
from employees e
join departments d on e.department_id = d.department_id;

/*
From the `subscribers` table of `classwork` database, for each social_network show:
- The number of new subscribers added on the first day and, 
- The number of new subscribers added on the last day
*/
use classwork;
select *,
first_value(new_subscribers) over(partition by social_network order by date) as first_day,
last_value(new_subscribers) over(partition by social_network order by date rows between unbounded preceding and unbounded following) as last_day
from subscribers;

-- Use farmers_market database to solve the following questions:
use farmers_market;
-- 1. Rank customers by total quantity purchased (highest first). Return customer_id, total quantity, and rank columns.
select customer_id, sum(quantity) as total_quantity,
rank() over(order by sum(quantity) desc) as "rank"
from customer_purchases
group by customer_id;

-- 2. Show each transaction with date-wise running total of quantity per customer. Use customer_purchases table.
select *,
sum(quantity) over(partition by customer_id order by market_date, transaction_time) as quantity_running_total 
from customer_purchases;

-- 3. Find the first purchase date of each customer
select *,
min(market_date) over(partition by customer_id) as customer_aquisition_date
from customer_purchases;

-- 4. Compare each transaction’s quantity with previous transaction for each customer
with cte as (
	select customer_id, market_date, transaction_time, quantity,
	lag(quantity, 1) over(partition by customer_id order by market_date, transaction_time) as previous_quantity
	from customer_purchases
)
select *, quantity - previous_quantity as difference
from cte;

-- 5. Get me the moving average of last 3 transactions per each customer
with t as (
	select *, round(cost_to_customer_per_qty * quantity, 2) as amount from customer_purchases
)
select *,
round(avg(amount) over(partition by customer_id order by market_date, transaction_time rows between 2 preceding and current row), 2) as moving_avg
from t;

-- 6. Calculate cumulative revenue per customer (revenue = quantity * price)
with t as (
	select *, round(cost_to_customer_per_qty * quantity, 2) as revenue from customer_purchases
)
select *,
sum(revenue) over(partition by customer_id order by market_date, transaction_time) as cumulative_revenue
from t;