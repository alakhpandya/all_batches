-- Connected Subquery
-- Write a query to print all the employees who are earning more than their managers (use hr2)
use hr2;

select *
from employees e1
where e1.salary > (
	select salary
    from employees e2
    where e1.manager_id = e2.employee_id
);

-- Print the employees who are earning more salary than the average salary of their department
select *
from employees e1
where salary > (
	select avg(salary)
    from employees e2
    where e1.department_id = e2.department_id
);

-- Display departments whose average employee salary is greater than the overall average salary. Return department_id, avg_salary columns. Use hr2.
select department_id, avg(salary)
from employees
group by department_id
having avg(salary) > (
	select avg(salary) from employees
);

-- Do this using subqueries: Display departments where the highest salary of any employee in that department is greater than 12000.
select distinct department_id
from employees e1
where (
	select max(salary)
    from employees e2
    where e1.department_id = e2.department_id
) > 12000;

-- In above question also print department_name but do not use join.
-- 1st way:
select department_id, department_name
from departments d
where (
	select max(salary)
    from employees e
    where d.department_id = e.department_id
) > 12000;

-- 2nd way:
select department_id, department_name
from departments
where department_id in (
	select department_id
	from employees
	where salary > 12000
);

-- 3rd way:
select department_id , max(salary), (select department_name from departments d where e.department_id = d.department_id) dep
from employees e
group by department_id
having max(salary) > 12000;

-- Display employees who earn more than the average salary of employees with the same job.
select * 
from employees e1
where salary > (
	select avg(salary)
    from employees e2
    where e1.job_id = e2.job_id
);

-- Display employees who work in the department that has the highest average salary.
select *
from employees
where department_id = (
	select department_id
    from employees
    group by department_id
    order by avg(salary) desc
    limit 1
);

-- Display job titles where the average salary of employees in that job is greater than the overall company average salary.
select job_title 
from employees e
join jobs j on e.job_id = j.job_id
group by e.job_id
having avg(salary) > (
	select avg(salary) from employees
);

-- Display employees who were hired after the most recently left employee in their department
select *
from employees e
where hire_date > (
	select end_date
	from job_history jh
	where e.department_id = jh.department_id
	order by end_date desc
    limit 1
);