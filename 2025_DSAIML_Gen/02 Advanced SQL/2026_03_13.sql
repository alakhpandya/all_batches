-- Print the orders which were placed after august 2003 and their deal size is small. Use demo dataset.
use demo;
select *
from sales_order
where order_date > "2003-08-31" and deal_size = "Small";
-- where month_id > 8 and year_id > 2003 and deal_size = "Small";  Not correct answer

-- Print orders which were placed in the last quarter of 2003 and have deal size small
select *
from sales_order
where qtr_id = 4 and year_id = 2003 and deal_size = "Small";

-- Print the first and last city (alphabetically) of customers from each country
select country, min(city) as first_city, max(city) as last_city 
from customers
group by country;
select * from customers;

-- Find the minimum & maximum price for each product line
select product_line,  min(price) as minimum_price, max(price) as max_price
from products
group by product_line;

/*
Print all the orders made from the country “USA”. 
Return order_number, order_date & deal_size columns. Show the result in descending order of order_date.
*/
select order_number, order_date, deal_size
from sales_order so
join customers c on so.customer=c.customer_id
where c.country="USA";

-- Get me the customers who are not from USA and their status is "In Process"
select c.customer_id, so.order_number, so.order_date, so.deal_size, c.country, so.status
from sales_order so
join customers c on so.customer=c.customer_id
where c.country <> "USA" and so.status = "In Process";

-- Write a query to find the name (first_name, last_name) of the employees who are managers (use hr).
use hr;
select first_name, last_name 
from employees
where employee_id in (
	select manager_id from employees
);

-- Find movies with an IMDb rating above the average rating
use moviesdb;
select * 
from movies
where imdb_rating > (select avg(imdb_rating) from movies);
-- balance > (20, 100)

-- List movies released in the same year as the movie titled 'Inception'
select *
from movies
where release_year = (
	select release_year from movies
    where title = "Inception"
) and
title <> "Inception";

-- Find the highest-rated movies for each studio (Solve this WITHOUT using group by)
select distinct studio, imdb_rating
from movies m1
where imdb_rating in (
	select max(imdb_rating)
    from movies m2
    where m1.studio = m2.studio
);

-- Write a query to print all the employees who are earning more than their managers (use hr2)
-- Using connected subquery
use hr2;
select employee_id, first_name, last_name, salary, manager_id
from employees e1
where salary > (
	select salary
    from employees e2
    where e1.manager_id = e2.employee_id
);

-- Using self join
select e1.employee_id, e1.first_name, e1.last_name, e1.salary, e1.manager_id, e2.first_name, e2.last_name, e2.salary
from employees e1
left join employees e2 on e1.manager_id = e2.employee_id
where e1.salary > e2.salary;