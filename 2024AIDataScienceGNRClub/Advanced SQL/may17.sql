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
with t1 as (
	select department_id, max(salary) as salary
	from employees
	group by department_id
)
select e.department_id, e.employee_id, e.first_name, e.last_name, e.salary
from employees e
join t1 on e.department_id = t1.department_id and t1.salary = e.salary;

/*
Find Employees Earning More Than Their Department Average –
Write a query to find the emp_id, first_name, last_name, salary, and department_id of employees whose salary is greater than the average salary of their department.
*/
select first_name, last_name, salary, department_id
from employees e1
where salary > (
	select avg(salary) 
    from employees e2
    where e1.department_id = e2.department_id
);

/*
List Departments with No Employees – 
Write a query to find the department_id and department_name of departments that have no employees assigned to them 
*/
use hr2;

select d.department_id
from departments d
left join employees e on d.department_id = e.department_id
where e.department_id is null;

-- Find Top 3 Highest-Paid Employees – Question: Write a query to find the emp_id, first_name, last_name, and salary of the top 3 highest-paid employees in the company.
select employee_id, first_name, last_name, salary
from employees
order by salary desc
limit 3;

-- From moviesdb database print names of all the actors who are of age from 70 to 85 (including both). Use CTE method instead of subquery if needed.
use moviesdb;

select * 
from actors
where (year(current_date()) - birth_year) between 70 and 85;

/*
Print the movies which produced 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: (Revenue – Budget) * 100 / Budget
Use CTE method instead of subquery if needed.
*/
with profitability as (
	select movie_id, (revenue-budget) * 100 / budget as pct_profit
    from financials
)
select * 
from movies m
join profitability p
on m.movie_id = p.movie_id
where p.pct_profit >= 500 and m.imdb_rating < (
	select avg(imdb_rating) from movies
);