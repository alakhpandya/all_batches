-- Print the employees who are earning more than the average salary of their department (use hr).
use hr;

select e1.employee_id, e1.first_name, e1.last_name, e1.salary, e2.avg_sal, e1.department_id 
from employees e1
join (
	select department_id, avg(salary) as avg_sal
	from employees
	group by department_id
) as e2
on e1.department_id = e2.department_id
where e1.salary > e2.avg_sal;


/*
Return movie_id, budget_adj, revenue_adj columns from financial table of moviesdb database 
where budget_adj and revenue_adj are budget & revenue converted into Million INR.
*/

/*
Print the movies which produced more than 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: profit * 100 / Budget
*/
use moviesdb;

SELECT title, industry, imdb_rating, profit, profit_pct
from (
	SELECT title, industry, imdb_rating, revenue_adj - budget_adj as profit, (revenue_adj - budget_adj)*100/budget_adj as profit_pct
	FROM movies m
	JOIN
		(SELECT movie_id,
				budget * IF(unit = 'Billions', 1000, IF(unit = 'thousands', .001, 1)) * IF(currency = 'USD', 80, 1) budget_adj,
				revenue * IF(unit = 'Billions', 1000, IF(unit = 'thousands', .001, 1)) * IF(currency = 'USD', 80, 1) revenue_adj
		FROM financials
		) f 
	USING (movie_id)
	where imdb_rating < (SELECT avg(imdb_rating) from movies)
) as m2
where profit_pct > 500;

-- C.T.E. : Commmon Table Expression
-- Print the employees who are earning more than the average salary of their department (use hr). Use CTE method.
use hr;

with e2 as (
	select department_id, avg(salary) as avg_sal
	from employees
	group by department_id
)
select e1.employee_id, e1.first_name, e1.last_name, e1.salary, e2.avg_sal, e1.department_id 
from employees e1
join e2
on e1.department_id = e2.department_id
where e1.salary > e2.avg_sal;


use moviesdb;
select year(current_date())
from movies;