-- Write a query to find the name (first_name, last_name) of the employees who are managers.
use hr;
select * from employees;

select first_name, last_name
from employees
where employee_id in (select distinct manager_id from employees);

-- Write a query to print all the employees who are earning more than their managers
use hr2;
select e1.employee_id, e1.first_name, e1.last_name, e1.manager_id, e2.first_name, e2.last_name, e1.salary as employee_salary, e2.salary as manager_salary
from employees e1
join employees e2
on e1.manager_id = e2.employee_id
where e1.salary > e2.salary;

select e1.employee_id, e1.first_name, e1.last_name
from employees e1
where e1.salary > (
	select salary
    from employees e2
    where e1.manager_id = e2.employee_id
);

/*
Print the employees who are earning more than the average salary of their department.
*/
use hr;
select department_id, avg(salary) as dep_avg_sal
from employees
group by department_id;

select e.employee_id, e.first_name, e.last_name, e.salary, e.department_id, t.dep_avg_sal
from employees e
join (
	select department_id, avg(salary) as dep_avg_sal
	from employees
	group by department_id
) as t
on e.department_id = t.department_id
where e.salary > t.dep_avg_sal;

/*
Return movie_id, budget_adj, revenue_adj columns from financial table of moviesdb database where budget_adj and revenue_adj are budget & revenue 
converted into Million INR.
*/
select movie_id, 
	if(currency = "USD", budget_mn*80, budget_mn) as budget_adj,
	if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_adj
from (
	select movie_id,
		case
			when unit = "Billions" then budget*1000
			when unit = "Thousands" then budget/1000
			else budget
		end as budget_mn,
		case
			when unit = "Billions" then revenue*1000
			when unit = "Thousands" then revenue/1000
			else revenue
		end as revenue_mn,
		currency
	from financials
) as t1;

/*
Print movie_id, budget_adj, revenue_adj & profit of each movie using financials table of moviesdb database. Show your result in the descending order of profit.
*/
select movie_id, budget_adj, revenue_adj, revenue_adj - budget_adj as profit
from (
	select movie_id, 
	if(currency = "USD", budget_mn*80, budget_mn) as budget_adj,
	if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_adj
	from (
		select movie_id,
			case
				when unit = "Billions" then budget*1000
				when unit = "Thousands" then budget/1000
				else budget
			end as budget_mn,
			case
				when unit = "Billions" then revenue*1000
				when unit = "Thousands" then revenue/1000
				else revenue
			end as revenue_mn,
			currency
		from financials
	) as t1
) as t2
order by profit desc;
/*
Print the movie titles, industry and profit. Sort the result in descending order of profit (profit = revenue – budget). 
Clean the revenue & budget so that it becomes easy to compare the profit each movie did (Hint: both of them must be in the same currency and in the same unit 
(thousand/million/billion etc) to compute the profit.)
*/
select m.movie_id, m.title, m.industry, t3.profit
from movies m
join (
	select movie_id, budget_adj, revenue_adj, revenue_adj - budget_adj as profit
	from (
		select movie_id, 
		if(currency = "USD", budget_mn*80, budget_mn) as budget_adj,
		if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_adj
		from (
			select movie_id,
				case
					when unit = "Billions" then budget*1000
					when unit = "Thousands" then budget/1000
					else budget
				end as budget_mn,
				case
					when unit = "Billions" then revenue*1000
					when unit = "Thousands" then revenue/1000
					else revenue
				end as revenue_mn,
				currency
			from financials
		) as t1
	) as t2
) as t3
on m.movie_id = t3.movie_id
order by profit desc;

-- C.T.E. : Common Table Expression

/*
Print the employees who are earning more than the average salary of their department.
*/
use hr;

select e.employee_id, e.first_name, e.last_name, e.salary, e.department_id, t.dep_avg_sal
from employees e
join (
	select department_id, avg(salary) as dep_avg_sal
	from employees
	group by department_id
) as t
on e.department_id = t.department_id
where e.salary > t.dep_avg_sal;

with t as (
	select department_id, avg(salary) as dep_avg_sal
	from employees
	group by department_id
)
select e.employee_id, e.first_name, e.last_name, e.salary, e.department_id, t.dep_avg_sal
from employees e
join t
on e.department_id = t.department_id
where e.salary > t.dep_avg_sal;

-- Write a query to find the emp_id, first_name, last_name, and salary of employees whose salary is greater than the average salary in the company.
select *
from employees e1
cross join (
	select avg(salary) as company_avg_sal from employees
) e
where salary > company_avg_sal;

with e as (
	select avg(salary) as company_avg_sal from employees
)
select *
from employees e1
cross join e
where salary > company_avg_sal;

/*
Find Highest Salary in Each Department – 
Question: Write a query to display the department_id, emp_id, first_name, last_name, and salary of employees who earn the highest salary in their respective departments.
*/
select *
from employees e
join (
	select department_id, max(salary) as dep_max_sal
    from employees
    group by department_id
) as t
on e.department_id = t.department_id
where salary = dep_max_sal;

with t as (
	select department_id, max(salary) as dep_max_sal
    from employees
    group by department_id
)
select * from employees e
join t on e.department_id = t.department_id
where salary = dep_max_sal;

/*
Return movie_id, budget_adj, revenue_adj columns from financial table of moviesdb database where budget_adj and revenue_adj are budget & revenue 
converted into Million INR.
*/
use moviesdb;
with t1 as (
	select movie_id,
		case
			when unit = "Billions" then budget*1000
			when unit = "Thousands" then budget/1000
			else budget
		end as budget_mn,
		case
			when unit = "Billions" then revenue*1000
			when unit = "Thousands" then revenue/1000
			else revenue
		end as revenue_mn,
		currency
	from financials
)
select movie_id, 
	if(currency = "USD", budget_mn*80, budget_mn) as budget_adj,
	if(currency = "USD", revenue_mn*80, revenue_mn) as revenue_adj
from t1;

/*
List Departments with No Employees – 
Question: Write a query to find the department_id and department_name of departments that have no employees assigned to them using hr2 database.
*/
use hr2;
select d.department_id, d.department_name
from departments d
left join employees e
on d.department_id = e.department_id
where e.department_id is null;