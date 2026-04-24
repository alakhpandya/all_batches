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

-- Write a query to print all the employees who are earning more than their managers (use hr2)
use hr2;
select e1.employee_id, e1.first_name, e1.last_name, e1.salary as employee_salary, e1.manager_id, e2.first_name as manager_name, e2.salary as manager_salary
from employees e1
join employees e2 on e1.manager_id = e2.employee_id
where e1.salary > e2.salary;

-- Using Subquery???

-- Print the employees who are earning above average salary (use hr)
use hr;
select *
from employees 
where salary > (select avg(salary) from employees);

-- Print the employees who are earning more salary than the average salary of their department
use hr2;
select department_id, avg(salary) from employees group by department_id;

/*
select *
from employees 
where salary > (select avg(salary) from employees group by department_id);		-- Error
*/
select * 
from employees e
left join (
	select department_id, avg(salary) as avg_salary
    from employees 
    group by department_id
) as t on e.department_id = t.department_id
where e.salary > t.avg_salary;