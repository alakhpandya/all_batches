/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ 
(Use ‘demo’ database)
*/
use demo;
with cte as
(
	select order_number, sales, deal_size, city
	from sales_order so
	left join customers c
	on so.customer = c.customer_id
),
cte2 as
(
	select city, avg(sales) as city_avg
	from cte
	group by city
)
select order_number, sales, deal_size, cte.city
from cte
join cte2 on cte.city = cte2.city
where sales > city_avg and deal_size <> "small";

/*
2)Find the difference in average sales for each month of 2003 and 2004 (Use ‘demo’ database)
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
join t2 on t1.month_id = t2.month_id
order by month_id;

-- Union & Union All
/*
Find the popularity percentage for each user on Meta/Facebook. 
The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, 
then converted into a percentage by multiplying by 100. 
Output each user along with their popularity percentage. Order records in ascending order by user id.
*/
select user1, user2
from facebook_friends
union
select user2, user1
from facebook_friends;

use moviesdb;
select distinct movie_id from movies;
select distinct actor_id from movie_actor;
select distinct actor_id from actors;

select * from movie_actor;
select * from actors;

select *
from movie_actor ma
left join actors a on ma.actor_id = a.actor_id
union
select *
from movie_actor ma
right join actors a on ma.actor_id = a.actor_id;

/*
Identify how many cars, motorcycles, trains and ships are available in the inventory. 
Treat all types of cars just as “Cars”. DO NOT USE ‘LIKE’ IN THIS EXAMPLE. (Use ‘demo’ database)
*/
use demo;
select * from products;
select product_line, count(*) as inventory
from products
where product_line in ("motorcycles", "trains", "ships")
group by product_line
union
select "Cars" as product_line, count(*)
from products
where product_line in ("classic cars", "vintage cars")
group by "Cars";