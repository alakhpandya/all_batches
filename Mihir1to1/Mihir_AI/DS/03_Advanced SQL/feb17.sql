-- Window functions

use paintings;
select * from artists;
-- Print the artists who are occurring more than once

with t1 as (
	select *,
	row_number() over() as row_num
	from artists
)
select *, min(row_num)
from t1
group by id, first_name, last_name;

use hr;

-- Print the top 3 earners from each department.
with t1 as (
	select *,
	row_number() over(partition by department_id order by salary desc) as row_id
	from employees
)
select employee_id, first_name, last_name, t1.department_id, d.department_name, salary
from t1
join departments d on t1.department_id = d.department_id
where row_id <= 3;

select *
from employees
order by department_id, salary desc;

/*
Print the following details of top 3 earners from each department: 
Return employee_id, first_name, last_name, t1.department_id, d.department_name, salary and average salary of each department columns.
*/

with t1 as (
	select *,
	row_number() over(partition by department_id order by salary desc) as row_id
	from employees
)
select *,
avg(salary) over(partition by department_id) as Dep_avg_salary
from t1
where row_id  <= 3;