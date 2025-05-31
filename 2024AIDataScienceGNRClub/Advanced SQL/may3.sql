-- subqueries
/*
Write a query to find the name (first_name, last_name) of the employees who are managers.
*/
use hr;
select distinct manager_id
from employees 
where manager_id is not null;

select *
from employees
where employee_id in (
	select distinct manager_id
	from employees 
	where manager_id is not null
);

-- Write a query to print all the employees who are earning more than their managers
use hr2;

select *
from employees e
where salary > (
	select salary
	from employees
	where employee_id = e.manager_id
);

select * from employees where employee_id in (148, 149);

-- using self-join:
select emp.employee_id, emp.first_name, emp.last_name, emp.salary as employee_salary, emp.manager_id, e.salary as manager_salary
from employees e
join employees emp
on e.employee_id = emp.manager_id
where e.salary < emp.salary;

/*
Print the employees who are earning more than the average salary of their department.
*/
use hr2;
select *
from employees e
where salary > (
	select avg(salary) as avg_salary from employees where department_id=e.department_id group by department_id
);

-- From the financials table of moviesdb dataset, convert all movies into Million USD, asuume the currency exchange rate 1 USD = 80 INR
use moviesdb;
select * from financials;
-- 1 Bn = 1000 Mn, 1/1000 Thousands = 1 Mn

select movie_id, currency, 
case
	when unit = "Billions" then budget*1000
    when unit = "Thousands" then budget/1000
    else budget
end as budget_mn,
if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as revenue_mn
from financials;

select movie_id, if(currency="INR", budget_mn/80, budget_mn) as budget_mn_usd, if(currency="INR", revenue_mn/80, revenue_mn) as revenue_mn_usd
from (
	select movie_id, currency, 
	case
		when unit = "Billions" then budget*1000
		when unit = "Thousands" then budget/1000
		else budget
	end as budget_mn,
	if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as revenue_mn
	from financials
) as t1;

/*
Print each movie (id, title, industry, studio) along with its profit. Also sort your result in the descending order of profit. hint: profit is revenue - budget but you
need to first convert all the movies budgets & revenues in the same unit & same currency
*/