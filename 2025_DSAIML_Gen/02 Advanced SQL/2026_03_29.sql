-- Use farmers_market database to answer these questions:
use farmers_market;
-- 1. Compare (show the difference) current quantity with average of previous 3 transactions
with t as (
	select customer_id, market_date, transaction_time, quantity,
	avg(quantity) over(partition by customer_id order by market_date, transaction_time rows between 3 preceding and 1 preceding) as avg_3
	from customer_purchases
)
select *,
avg_3 - quantity as diff
from t;

-- 2. Find the top 3 customers (by total spend) for each year.
with t1 as (
	select customer_id, year(market_date) as yr,
	sum(quantity*cost_to_customer_per_qty) as total_spent
	from customer_purchases
    group by customer_id, year(market_date)
),
t2 as (
	select *,
    rank() over(partition by yr order by total_spent desc) as customer_rank
    from t1
)
select yr, customer_id, total_spent, customer_rank
from t2
where customer_rank <= 3;

-- 3. For each customer, find their most expensive single transaction and return full details.
with t1 as (
	select *,
    quantity*cost_to_customer_per_qty as txn_value
	from customer_purchases
), t2 as (
	select *,
	rank() over(partition by customer_id order by txn_value desc) as txn_rank
	from t1
)
select *
from t2
where txn_rank = 1;

-- 4. Find customers whose latest purchase quantity is higher than their average historical quantity.
with t as (
	select *,
	avg(quantity) over(partition by customer_id) as avg_qty,
	rank() over(partition by customer_id order by market_date desc, transaction_time desc) as rn
    from customer_purchases
)
select customer_id, market_date, transaction_time, quantity, avg_qty
from t
where rn = 1 and quantity > avg_qty;

-- 5. Find the second highest spending customer for each product.
with t1 as (
    select product_id, customer_id,
	sum(quantity * cost_to_customer_per_qty) as total_spend
    from customer_purchases
    group by product_id, customer_id
), 
t2 as (
	select *,
	dense_rank() over(partition by product_id order by  total_spend desc) as rnk
    FROM t1
)
select *
from t2
where rnk = 2;


-- More practice questions (on the same dataset):
/*
6. Identify “loyal customers” who purchased on at least 3 consecutive market dates.
7. For each customer, calculate the % contribution of each transaction to their total spend.
8. Find customers whose spending trend is consistently increasing (each transaction ≥ previous one).
9. Find the day where each product had its highest total sales (revenue).
10. Find customers who are in the top 10% of spenders overall.
11. For each customer, find the longest gap (in days) between two consecutive purchases.
*/