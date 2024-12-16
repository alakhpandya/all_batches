use demo;
-- Get me the customers who are not from USA and their status is "In Process"
select * from sales_order;
select * from customers;

select distinct c.customer_id, c.customer_name, c.country, s.status
from customers c
left join sales_order s
on c.customer_id = s.customer
where country <> "USA" and status = "In Process";

-- Print the names of the actors who did not play role in any movie

use moviesdb;
select * from actors;
select * from movie_actor;
select * from movies;

select a.actor_id, a.name
from actors a
left join movie_actor ma
on a.actor_id = ma.actor_id
where ma.movie_id is null;

use hr2;
select * from employees;

select *
from employees
where employee_id in (
	select manager_id from employees
);

-- Print the names of the departments in which no employee is working.
select distinct department_name, count(e.employee_id)
from departments d
left join employees e
on d.department_id = e.department_id
where e.department_id is null
group by department_name;

select distinct manager_id from employees;