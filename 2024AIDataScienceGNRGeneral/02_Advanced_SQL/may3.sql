-- Topic: Subqueries

/*
Write a query to find the name (first_name, last_name) of the employees who are managers.
*/
select *
from employees
where employee_id in (
	select distinct manager_id
	from employees
	where manager_id is not null
);

-- Using self join
select distinct e.employee_id, e.first_name, e.last_name
from employees e
join employees emp
on e.employee_id = emp.manager_id;

-- Write a query to print all the employees who are earning more than their managers
use hr2;
select emp.employee_id, emp.first_name, emp.last_name, emp.salary as employee_salary, e.first_name as manager, e.salary as manager_salary
from employees e
join employees emp
on e.employee_id = emp.manager_id
where emp.salary > e.salary;

-- using subquery
select *
from employees e
where salary > (
	select salary
    from employees
    where employee_id = e.manager_id
);

-- Print the employees who are earning more than the average salary of their department.
select *
from employees e1
where salary > (
	select avg(salary)
	from employees e2
    where e1.department_id = e2.department_id
	group by department_id
);