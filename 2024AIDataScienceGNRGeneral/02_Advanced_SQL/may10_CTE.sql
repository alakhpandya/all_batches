use moviesdb;
select * from financials;

/*
From the financials table of moviesdb dataset, convert all movies into Million USD, 
asuume the currency exchange rate 1 USD = 80 INR
*/
-- outer query: convert into USD
-- inner subquery: convert Billions & Thousands into Millions
select movie_id,
round(if(currency="INR", budget_mn/80, budget_mn), 2) as budget_mn_usd,
round(if(currency="INR", revenue_mn/80, revenue_mn), 2) as revenue_mn_usd
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
) as t1;

/*
Using moviesdb dataset print movie_id, title, imdb_rating, studio and profit of each movie.
Print your result in the descending order of profit. Hint: profit = revenue - budget.
*/
select m.movie_id, m.title, m.imdb_rating, m.studio, revenue_mn_usd - budget_mn_usd as profit
from (
	select movie_id,
	round(if(currency="INR", budget_mn/80, budget_mn), 2) as budget_mn_usd,
	round(if(currency="INR", revenue_mn/80, revenue_mn), 2) as revenue_mn_usd
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
	) as t1
) as t2
join movies m on m.movie_id = t2.movie_id
order by profit desc;

-- C.T.E. = Common Table Expression
-- Print the employees who are earning more than the average salary of their department
use hr;

select employee_id, first_name, last_name, salary, e.department_id, avg_salary
from  employees e
join (
	select department_id, avg(salary) as avg_salary
	from employees
	group by department_id
) as t1
on t1.department_id = e.department_id
where e.salary > t1.avg_salary;

with t1 as (
	select department_id, avg(salary) as avg_salary
	from employees
	group by department_id
)
select employee_id, first_name, last_name, salary, e.department_id, avg_salary
from employees e
join t1 on e.department_id = t1.department_id
where salary > avg_salary;

