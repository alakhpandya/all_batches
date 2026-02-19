use hr2;
/*
Display departments whose average employee salary is greater than the overall average salary.
*/
select department_id, avg(salary)
from employees
group by department_id
having avg(salary) > (
	select avg(salary) from employees
);

-- Display job titles for jobs that have employees earning more than 10000.
select distinct j.job_title
from jobs j
left join employees e on j.job_id = e.job_id
where e.salary > 10000;

-- Display employees whose salary is higher than the average salary of their own department.
select employee_id, first_name, last_name, salary
from employees e1
where salary > (
	select avg(salary)
    from employees e2
    where e1.department_id = e2.department_id
    group by department_id
);

-- Do this using subqueries: Display departments where the highest salary of any employee in that department is greater than 12000.
-- 1st way:
select distinct department_id
from employees e1
where (
	select max(salary)
    from employees e2
    where e1.department_id = e2.department_id
) > 12000;

-- 2nd way:
select department_id, department_name
from departments d
where (
	select max(salary)
    from employees e
    where d.department_id = e.department_id
) > 12000
order by department_id;

-- 3rd way:
select department_id, department_name
from departments
where department_id in (
	select department_id
	from employees
	where salary > 12000
);

-- Display employees who earn more than the average salary of employees with the same job.
select employee_id, first_name, last_name, salary
from employees e1
where salary > (
	select avg(salary)
    from employees e2
    where e1.job_id = e2.job_id
);

-- Display employees who work in the department that has the highest average salary.
select employee_id, first_name, last_name
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

-- Display employees who were hired after the most recently hired employee in their department
select employee_id, first_name, last_name, hire_date
from employees e1
where hire_date > (
	select max(hire_date)
	from employees e2
    where e1.department_id = e2.department_id
);

-- Use subqueries to solve this: Display departments that have no employees earning less than 5000.
select department_id
from employees
group by department_id
having min(salary) >= 5000;


-- not in
select distinct department_id
from employees
where department_id not in (
	select distinct department_id
	from employees
	where salary < 5000
);

-- Use subqueries to solve this: Display countries where no departments exist.
select country_name, l.location_id, d.department_name
from countries c
left join locations l on c.country_id = l.country_id
left join departments d on d.location_id = l.location_id
where d.department_id is not null;

select country_name
from countries
where country_name not in (
	select country_name
	from countries c
	left join locations l on c.country_id = l.country_id
	left join departments d on d.location_id = l.location_id
	where d.department_id is not null
);

select salary as "income"
from employees;

select *, 5000 as increment
from employees;