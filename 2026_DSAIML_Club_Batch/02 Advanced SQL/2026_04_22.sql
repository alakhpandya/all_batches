-- Print the names of the actors who did not play role in any movie (Use moviesdb database)
use moviesdb;
select a.actor_id, a.name, a.birth_year
from movie_actor ma
right join actors a on ma.actor_id = a.actor_id
-- where movie_id is null;
where ma.actor_id is null;

-- Print the names of the departments in which no employee is working (Use hr2 database)
use hr2;
-- select d.department_id, department_name
select *
from departments d
left join employees e on d.department_id = e.department_id
where employee_id is null;
-- where commission_pct is null;
-- where e.manager_id is null;

-- Write a query to find the name (first_name, last_name) of the employees who are managers (use hr)
use hr;
select distinct e2.employee_id, e2.first_name, e2.last_name
from employees e1
join employees e2 on e1.manager_id = e2.employee_id;

-- using subquery
select *
from employees
where employee_id in (select distinct manager_id from employees);

