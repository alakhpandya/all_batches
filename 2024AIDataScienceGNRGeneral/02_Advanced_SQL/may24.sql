/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ 
(Use ‘demo’ database)
*/
use demo;
select order_number, sales, deal_size, city
from sales_order so
join customers c on so.customer = c.customer_id;

with t1 as (
	select order_number, sales, deal_size, city
	from sales_order so
	join customers c on so.customer = c.customer_id
),
t2 as (
	select city, avg(sales) as city_avg
	from t1
	group by city
)
select order_number, sales, deal_size, t1.city
from t1
join t2 on t1.city = t2.city
where sales > city_avg and deal_size <> "small";

/*
2) Find the difference in average sales for each month of 2003 and 2004 (Use ‘demo’ database)
*/
with t1 as (
	select month_id, round(avg(sales), 2) as avg_sales_2003
	from sales_order
	where year_id = 2003
	group by month_id
),
t2 as (
	select month_id, round(avg(sales), 2) as avg_sales_2004
	from sales_order
	where year_id = 2004
	group by month_id
)
select t1.month_id, avg_sales_2003, avg_sales_2004, round(avg_sales_2004 - avg_sales_2003, 2) as difference
from t1
join t2 on t1.month_id = t2.month_id;

-- Union & Union All