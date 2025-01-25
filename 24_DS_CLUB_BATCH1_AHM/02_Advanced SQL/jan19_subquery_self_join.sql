use hr2;

select *
from employees
where employee_id in (
	select distinct manager_id
	from employees
);

/*
Write a query to print all the employees who are earning more than their managers
*/
-- select e.first_name,e.salary employee_salary,m.salary manager_salary 
select e.employee_id, e.first_name, e.last_name, e.salary, e.manager_id, m.first_name as manager_name, m.salary as manager_salary
from employees e 
join employees m
on e.manager_id=m.employee_id
where e.salary > m.salary;

/*
Print the employees who are earning more than the average salary of their department.
*/
-- employee_id, first_name, last_name, salary, dep_avg_salary
select e.employee_id, e.first_name, e.last_name, e.salary, t.department_id, t.dep_avg_salary
from employees e
join (
select department_id, avg(salary) as dep_avg_salary 
from employees
group by department_id
) as t
on e.department_id = t.department_id
where e.salary > t.dep_avg_salary
order by t.department_id;

use moviesdb;

select movie_id,
case
	when currency = "USD" then budget_mn*80
    else budget_mn
end as budget_mn_inr,
case
	when currency = "USD" then revenue_mn*80
    else revenue_mn
end as revenue_mn_inr
from (
	select movie_id, currency,
	case
		when unit = "Billions" then budget*1000
		when unit = "Thousands" then budget/1000
		else budget
	end as budget_mn,
	case
		when unit = "Billions" then revenue*1000
		when unit = "Thousands" then revenue/1000
		else revenue
	end as revenue_mn
	from financials
) t;