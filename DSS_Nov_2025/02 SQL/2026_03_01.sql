use demo;
-- Print the orders which were placed after august 2003 and their deal size is small
select * from customers;
select * from products;
select * from sales_order;

select *
from sales_order
where order_date > "2003-08-31" and deal_size = "Small";

-- Print orders which were placed in the last quarter of 2003 and have deal size small
select *
from sales_order
where order_date between "2003-10-01" and "2003-12-31" and deal_size = "Small";

select *
from sales_order
where qtr_id = 4 and year_id = 2003 and deal_size="Small";

-- Print the first and last city (alphabetically) of customers from each country
select country, min(city) first_city, max(city) last_city
from customers
group by country;

-- Find the minimum & maximum price_each for each product line
select p.product_line, min(s.price_each), max(s.price_each)
from products p
join sales_order s on p.product_code = s.Product
group by p.product_line;

/*
Print all the orders made from the country “USA”. 
Use  sales_order & customers tables from Demo database. Return order_number, order_date & deal_size columns. Show the result in descending order of order_date.
*/
select order_number, order_date, deal_size, country
from sales_order s
left join customers c on s.customer = c.customer_id
where c.country = "USA"
order by order_date desc;

-- Get me the customers who are not from USA and their status is "In Process"
select distinct c.customer_id, c.customer_name, c.phone, c.address, c.city, c.state, c.postal_code, c.country, s.status
from sales_order s
left join customers c on s.customer = c.customer_id
where c.country <> "USA" and s.status = "In Process";

-- Print all the unique product lines
select distinct product_line from products;

/*
Find the most profitable orders. 
Orders which have higher sales price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ 
(Use ‘demo’ database)
*/
with t1 as (
	select city, avg(sales) as city_avg
    from sales_order s
	join customers c on s.customer = c.customer_id
    group by city
),
t2 as (
	select *
	from sales_order s
	join customers c on s.customer = c.customer_id
    where deal_size != "Small"
)
select t2.*, round(city_avg, 0) city_avg
from t2
join t1 on t1.city = t2.city
where sales > city_avg;

-- Find the difference in average sales for each month of 2003 and 2004 (Use ‘demo’ database)
with t1 as (
	select month_id, avg(sales) as avg_sales_2003
	from sales_order
	where year_id = 2003
	group by month_id
),
t2 as (
	select month_id, avg(sales) as avg_sales_2004
	from sales_order
	where year_id = 2004
	group by month_id
)
select t1.month_id, round(t2.avg_sales_2004 - t1.avg_sales_2003, 2) as diff
from t1
join t2 on t1.month_id = t2.month_id
order by t1.month_id;

-- OR
SELECT 
    month_id,
    AVG(CASE WHEN year_id = 2003 THEN sales END) AS avg_sales_2003,
    AVG(CASE WHEN year_id = 2004 THEN sales END) AS avg_sales_2004,
    AVG(CASE WHEN year_id = 2004 THEN sales END) 
      - AVG(CASE WHEN year_id = 2003 THEN sales END) AS difference
FROM sales_order
WHERE year_id IN (2003, 2004)
GROUP BY month_id
ORDER BY month_id;

-- OR
with t as (
    select 
        month_id,
        year_id,
        avg(sales) as avg_sales
    from Sales_order
    where year_id in (2003, 2004)
    group by month_id, year_id
)
select
    a.month_id,
    a.avg_sales as "2004_avg_sales",
    b.avg_sales as "2003_avg_sales",
    a.avg_sales - b.avg_sales as diff
from t a
join t b
    on a.month_id = b.month_id
where a.year_id = 2004
  and b.year_id = 2003
order by a.month_id, a.year_id, b.month_id, b.year_id;

/*
Find the popularity percentage for each user on Meta/Facebook. 
The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, 
then converted into a percentage by multiplying by 100. Output each user along with their popularity percentage. Order records in ascending order by user id.
*/
use classwork;
select * from facebook_friends;