-- Print the employees who are earning more than the average salary of their department (use hr).
use hr;
select * 
from employees e1
join (
	select department_id, avg(salary) as dep_avg_sal
	from employees 
	group by department_id
) e2 on e1.department_id=e2.department_id
where e1.salary > e2.dep_avg_sal;

select *
from employees e1
where e1.salary > (
	select avg(salary)
    from employees e2
    where e1.department_id=e2.department_id
);

/*
Return movie_id, budget_adj, revenue_adj columns from financial table of moviesdb database
where budget_adj and revenue_adj are budget & revenue converted into Million INR. Assume conversion rate of $1 = ₹80.
*/
use moviesdb;

select movie_id, 
round(if(currency="USD", budget_mn*80, budget_mn), 2) as budget_adj, 
round(if(currency="USD", revenue_mn*80, revenue_mn), 2) as revenue_adj
from (
	select movie_id, 
	case
		when unit="Billions" then budget*1000
		when unit="Thousands" then budget/1000
		else budget
	end as budget_mn, 
	case
		when unit="Billions" then revenue*1000
		when unit="Thousands" then revenue/1000
		else revenue
	end as revenue_mn, currency
	from financials
) as t;

-- Display the department_id, emp_id, first_name, last_name and salary of employees who earn the highest salary in their respective departments. Use hr dataset.
use hr;
select e1.department_id, employee_id, first_name, last_name, salary
from employees e1
join (
	select department_id, max(salary) as dep_highest_sal
	from employees 
	group by department_id
) e2 on e1.department_id=e2.department_id
where e1.salary = e2.dep_highest_sal;


-- Write a query to find the emp_id, first_name, last_name, and salary of the top 3 highest-paid employees in the company.
select employee_id, first_name, last_name, salary
from employees
order by salary desc
limit 3;

/*
Print the movie titles, industry and profit of each movie. Sort the result in descending order of profit (profit = revenue – budget).
*/
use moviesdb;

select title, industry, revenue_mn_inr, budget_mn_inr, 
revenue_mn_inr - budget_mn_inr as profit_mn_inr
from movies m
join (
	select movie_id, 
	round(if(currency="USD", revenue_mn*80, revenue_mn), 2) as revenue_mn_inr,
	round(if(currency="USD", budget_mn*80, budget_mn), 2) as budget_mn_inr
	from (
		select movie_id, 
		case
			when unit="Billions" then budget*1000
			when unit="Thousands" then budget/1000
			else budget
		end as budget_mn, 
		case
			when unit="Billions" then revenue*1000
			when unit="Thousands" then revenue/1000
			else revenue
		end as revenue_mn, currency
		from financials
	) as t1
) as t2 on m.movie_id = t2.movie_id
order by 5 desc;

-- C.T.E. : Common Table Expression
-- Display the department_id, emp_id, first_name, last_name and salary of employees who earn the highest salary in their respective departments. Use hr dataset.
use hr;

select e1.department_id, employee_id, first_name, last_name, salary
from employees e1
join (
	select department_id, max(salary) as dep_highest_sal
	from employees 
	group by department_id
) e2 on e1.department_id=e2.department_id
where e1.salary = e2.dep_highest_sal;


with e2 as (
	select department_id, max(salary) as dep_highest_sal
	from employees 
	group by department_id
)
select e1.department_id, employee_id, first_name, last_name, salary
from employees e1
join e2 on e1.department_id=e2.department_id
where e1.salary = e2.dep_highest_sal;

-- Practice questions for CTE:
-- From moviesdb database print names of all the actors who are of age from 70 to 85 (including both). Use CTE method instead of subquery if needed.
use moviesdb;
with t as (
	select *,
	2026 - birth_year as age 
	from actors
)
select *
from t
where age between 70 and 85;

/*
Print the movies which produced more than 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: profit * 100 / Budget.
Use CTE method instead of subquery if needed.
*/
with t1 as (
	select movie_id, (revenue - budget)*100/budget as profit_pct
    from financials
)
select *
from movies m
join t1 on m.movie_id=t1.movie_id
where profit_pct > 500 and 
imdb_rating < (select avg(imdb_rating) from movies);

/*
Print the movie titles, industry and profit of each movie. Sort the result in descending order of profit (profit = revenue – budget). Use CTE in place of subqueries.
*/
with t1 as (
	select movie_id, 
	case
		when unit="Billions" then budget*1000
		when unit="Thousands" then budget/1000
		else budget
	end as budget_mn, 
	case
		when unit="Billions" then revenue*1000
		when unit="Thousands" then revenue/1000
		else revenue
	end as revenue_mn, currency
	from financials
),
t2 as (
	select movie_id, 
    if(currency="USD", budget_mn*80, budget_mn) as budget_mn_inr,
    if(currency="USD", revenue_mn*80, revenue_mn) as revenue_mn_inr
    from t1
)
select m.movie_id, title, revenue_mn_inr - budget_mn_inr as profit_mn_inr 
from movies m
join t2 on m.movie_id = t2.movie_id
order by 3 desc;

/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ 
(Use ‘demo’ database)
*/
use demo;