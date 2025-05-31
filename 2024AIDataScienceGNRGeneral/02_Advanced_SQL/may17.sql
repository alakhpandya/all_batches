-- Recap of CTE:
use hr;
select employee_id, first_name, last_name, salary
from employees
where salary > (select avg(salary) from employees);

with t as (
select avg(salary) avg_sal from employees
)
select employee_id, first_name, last_name, salary
from employees
where salary > t.avg_sal;

/*
Employees Earning Above Average Salary: 
Write a query to find the emp_id, first_name, last_name, and salary of employees whose salary is greater than the average salary in the company.
*/
use hr;
select employee_id, first_name, last_name, salary
from employees
where salary > (select avg(salary) from employees);

/*
Find Department Heads:
Write a query to find the emp_id, first_name, last_name, and department_id of employees who are managers (their emp_id is referenced as manager_id in the table).
*/
select employee_id, first_name, last_name, department_id
from employees
where employee_id in (select manager_id from employees);

/*
Find Highest Salary in Each Department
Write a query to display the department_id, emp_id, first_name, last_name, and salary of employees who earn the highest salary in their respective departments. 
Use CTE in place of subquery if applicable.
*/
select e.department_id, employee_id, first_name, last_name, salary, dep_max_sal
from employees e
join (
	select department_id, max(salary) as dep_max_sal
	from employees
	group by department_id
) as t
on e.department_id = t.department_id and e.salary = t.dep_max_sal;

with t as (
	select department_id, max(salary) as dep_max_sal
	from employees
	group by department_id
)
select e.department_id, employee_id, first_name, last_name, salary, dep_max_sal
from employees e
join t
on e.department_id = t.department_id and e.salary = t.dep_max_sal;

/*
Find Employees Earning More Than Their Department Average –
Write a query to find the emp_id, first_name, last_name, salary, and department_id of employees whose salary is greater than the average salary of their department.
*/
with m as (
	select department_id, avg(salary) as avg_sal
    from employees
    group by department_id
)
select employee_id, first_name, last_name, salary, e.department_id
from employees e
join m
on e.department_id = m.department_id
where e.salary > m.avg_sal;

/*
List Departments with No Employees – 
Write a query to find the department_id and department_name of departments that have no employees assigned to them 
*/
use hr2;

select * from departments;

select d.department_id, department_name, location_id
from departments d
left join employees e
on d.department_id = e.department_id
where e.department_id is null;

/*
Find Top 3 Highest-Paid Employees – Question: Write a query to find the emp_id, first_name, last_name, and salary of the top 3 highest-paid employees in the company.
*/
use hr;
select *
from employees
order by salary desc
limit 3;

-- From moviesdb database print names of all the actors who are of age from 70 to 85 (including both). Use CTE method instead of subquery if needed.


/*
Print the movies which produced 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: (Revenue – Budget) * 100 / Budget
Use CTE method instead of subquery if needed.
*/