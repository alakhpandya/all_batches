select * from sales_order;
select * from products;
select * from customers;

select *
from sales_order
where sales < (quantity_ordered * price_each);

select distinct product_code from products;

-- Print the orders which were placed after august 2003 and their deal size is small
select *
from sales_order
where deal_size = "Small" and
order_date > "2003-08-31";

-- Print orders which were placed in the last quarter of 2003 and have deal size small
select *
from sales_order
where deal_size = "Small" and
qtr_id = 4 and year_id = 2003;

-- Print the first and last city (alphabetically) of customers from each country
select country, min(city) as first_city, max(city) as last_city
from customers
group by country;

-- Find the minimum & maximum sales price for each product line
select product_line, min(price_each) as min_price, max(price_each) as max_price
from products p
left join sales_order so
on p.product_code = so.product
group by product_line;

/*
Print all the orders made from the country “USA”. Use  sales_order & customers tables from Demo database. 
Return order_number, order_date & deal_size columns in descending order of order_date.
*/
select order_number, order_date, deal_size
from customers c
right join sales_order so
on so.customer = c.customer_id
where country = "USA"
order by order_date desc;

/*
Get me the customers who are not from USA and their status is "In Process"
*/
select *
from customers c
left join sales_order so
on c.customer_id = so.customer
where country != "USA" and status = "In Process";

/*
Print the names of the actors who did not play role in any movie
*/
use moviesdb;
select *
from actors a
left join movie_actor ma on a.actor_id = ma.actor_id
left join movies m on ma.movie_id = m.movie_id
where m.movie_id is null;
/*
Print the names of the departments in which no employee is working (Use hr2 database & right join)
*/
use hr2;
select * from employees;