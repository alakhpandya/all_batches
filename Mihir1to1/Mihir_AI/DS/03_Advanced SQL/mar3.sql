-- use as7;
/*
Create table If Not Exists Employees (employee_id int, name varchar(30)); 
Create table If Not Exists Salaries (employee_id int, salary int); 
Truncate table Employees; 
insert into Employees (employee_id, name) values ('2', 'Crew'); 
insert into Employees (employee_id, name) values ('4', 'Haven'); 
insert into Employees (employee_id, name) values ('5', 'Kristian'); 
Truncate table Salaries; 
insert into Salaries (employee_id, salary) values ('5', '76071'); 
insert into Salaries (employee_id, salary) values ('1', '22517'); 
insert into Salaries (employee_id, salary) values ('4', '63539');
*/
/*
select * from salaries;

select e.employee_id
from Employees e
Left Join Salaries s
on e.employee_id = s.employee_id
where s.salary is null
union
select s.employee_id
from Employees e
Right Join Salaries s
on e.employee_id = s.employee_id
where e.name is null
order by employee_id;
*/

USE HR;

-- WINDOW FUNCTIONS
-- ROW_NUMBER
-- Get me the highest salary from each department with the first_name & the last_name of the employee with highest salary

with t1 as (
	SELECT e.*, d.department_name
	FROM employees e
	left join departments d on e.department_id = d.department_id
),
t2 as (
	select department_name, first_name, last_name, salary,
	row_number() over(partition by department_name order by salary desc) as Salary_order
	from t1
	order by department_name
)
select * from t2 where Salary_order < 2;

-- SUM
-- Print the total salary paid in each department
with t1 as (
	SELECT e.*, d.department_name
	FROM employees e
	left join departments d on e.department_id = d.department_id
)
select distinct department_name,
sum(salary) over(partition by department_name) as Total_salary_paid
from t1
order by department_name;

-- Print the percentage share of each employee's salary in the total salary paid to that department for each department.
with t1 as (
	SELECT e.*, d.department_name
	FROM employees e
	left join departments d on e.department_id = d.department_id
),
t2 as (
	select department_name, first_name, last_name, salary,
	sum(salary) over(partition by department_name) as Department_total_salary
	from t1
	order by department_name
)
select *, round(salary*100/Department_total_salary, 2) as Pct_share
from t2;

-- MAX & MIN

with t1 as (
	SELECT e.*, d.department_name
	FROM employees e
	left join departments d on e.department_id = d.department_id
),
t2 as (
	select department_name, first_name, last_name, salary,
    MIN(salary) over(partition by department_name) as Department_lowest_salary,
	MAX(salary) over(partition by department_name) as Department_highest_salary
	from t1
	order by department_name, salary
)
select *, 
salary - Department_lowest_salary as Diff_from_lowest_salary, 
Department_highest_salary - salary as Diff_from_highest_salary
from t2;

-- AVG