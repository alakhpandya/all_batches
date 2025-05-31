-- Print the orders which were placed after august 2003 and their deal size is small
use demo;
select * 
from sales_order
where deal_size = "Small" and
order_date > "2003-08-31";

-- Print orders which were placed in the last quarter of 2003 and have deal size small
select * 
from sales_order
where deal_size = "Small" and
qtr_id = 4 and
year_id = 2003;

-- Print the first and last city (alphabetically) of customers from each country
select * from customers;
select country, min(city) as first_city, max(city) as last_city
from customers
group by country;

-- Find the minimum & maximum sales price for each product line
select * from products;

select * from sales_order;
select order_number, quantity_ordered, price_each, sales, product, product_line
from products p
left join sales_order so
on p.product_code = so.product
order by order_number;

select p.product_line, min(sales) as minimum_price, max(sales) as maximum_price
from products p
left join sales_order so
on p.product_code = so.product
group by p.product_line;

-- H.W.
-- Print all the orders made from the country “USA”. Use sales_order & customers tables from Demo database. 
-- Return order_number, order_date & deal_size columns in descending order of order_date.

-- Get me the customers who are not from USA and their status is "In Process"