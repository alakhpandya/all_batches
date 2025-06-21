use moviesdb;

use demo;
select * from sales_order;
select * from customers;

select country, min(city), max(city)
from customers
group by country;

/*
Print all the orders made from the country “USA”. Use  sales_order & customers tables from Demo database. 
Return order_number, order_date & deal_size columns. Show the result in descending order of order_date.
*/

select *
from sales_order so
join customers c
on so.customer = c.customer_id
where c.country = "USA";

-- Get me the customers who are not from USA and their status is "In Process"
select *
from sales_order so
join customers c
on so.customer = c.customer_id
where c.country != "USA" and status = "In Process";

-- Write a query to find the name (first_name, last_name) of the employees who are managers (use hr).
use hr;
select first_name, last_name
from employees
where employee_id in (
	select distinct manager_id from employees
);

select distinct manager_id from employees;

-- Write a query to print all the employees who are earning more than their managers (use hr2)
use hr2;
select e1.*, e2.salary as manager_salary 
from employees e1
join employees e2
on e1.manager_id = e2.employee_id
where e1.salary > e2.salary;

select e1.*
from employees e1
where e1.salary > (
	select salary
    from employees e2
    where e1.manager_id = e2.employee_id
);