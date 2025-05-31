-- Print orders which were placed in the last quarter of 2003 and have deal size small
select *
from sales_order
where qtr_id = 4 and year_id=2003 and deal_size="Small";


-- Print the first and last city (alphabetically) of customers from each country
select customer_id, city
from customers;

select country, min(city), max(city)
from customers
group by country;

select product_line, max(price)
from products
group by product_line;

/*
Print all the orders made from the country “USA”. Use  sales_order & customers tables from Demo database. 
Return order_number, order_date & deal_size columns in descending order of order_date.
*/

select s.order_number, s.order_date, s.deal_size
from sales_order s
join customers c
on s.customer = c.customer_id
where c.country = "USA"
order by s.order_date desc;

/*
Get me the customers who are not from USA and their status is "In Process"
*/

select distinct(c.customer_id), c.customer_name, s.status
from sales_order s
join customers c
on s.customer = c.customer_id
where c.country <> "USA" and s.status = "In Process";

-- Print the names of the actors who did not play role in any movie
use moviesdb;

select * from movie_actor;
select * from actors;

select a.actor_id, a.name, ma.movie_id
from actors a
left join movie_actor ma
on a.actor_id = ma.actor_id
where ma.movie_id is null;