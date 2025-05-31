use sql50;

select * from prices;
select * from unitssold;

select *, p.price * us.units as total_sale
from prices p
join unitssold us
on p.product_id = us.product_id
where us.purchase_date between p.start_date and p.end_date;

-- Window functions: RANK
use hr;
select department_id, first_name, last_name, salary,
RANK() OVER(partition by department_id order by salary desc) as ranking,  -- Competition Rank
DENSE_RANK() OVER(partition by department_id order by salary desc) as dense_ranking, -- Dense Rank
PERCENT_RANK() OVER(partition by department_id order by salary desc) as percentile
from employees;

-- Print top-3 earners from each department. Return columns: department_name, employee_id, first_name, last_name, salary and ranking (Use dense ranking system on hr dataset)

-- Window function: NTILE 
select * from employees;

select department_id, first_name, last_name, salary,
NTILE(4) OVER() as "group"
from employees;

with t1 as
(
	select department_id, first_name, last_name, salary,
	NTILE(3) OVER() as groop
	from employees
)
select * from t1
where groop = 1;

select department_id, first_name, last_name, salary,
NTILE(6) OVER() as groop
from employees;

select department_id, first_name, last_name, salary,
NTILE(2) OVER(partition by department_id order by salary desc) as groop
from employees;

select department_id, first_name, last_name, salary,
NTILE(2) OVER(order by salary) as groop
from employees;

/*
In the student score table, divide the students into two groups in such a way that all top-scoring students from each department fall in 2nd group and all the 
low-scoring students in the first group.
*/

-- Aggregate window functions - AVG, MAX, MIN, SUM, COUNT
use moviesdb;
select * from movies;

select round(avg(imdb_rating), 1)
from movies;

select *,
-- AVG(imdb_rating) OVER() as Avg_rating
round(AVG(imdb_rating) OVER(), 1) as Avg_rating,
max(imdb_rating) over() as top_rating,
min(imdb_rating) over() as worst_rating,
count(*) over(partition by industry) as no_of_ratings_in_industry
from movies;

/*
Print the how good or bad each movie performed in terms of imdb_ratings when compared with the average imdb rating of their corresponding industry (the difference
between the imdb_rating of the movie and avg imdb rating of the industry that movie belongs to). Return the following columns: movie_id, title, industry, 
imdb_rating, industry_avg_rating and difference
*/

/*
Print the difference between the profit of each movie and the per-movie average profit of the studio which produced that film along with the following columns:
movie_id, title, studio, studio_avg_profit, movie_profit and profit_difference.
*/

-- window function - sum
with t1 as
(
	select m.movie_id, m.title, m.studio,
	if(f.unit = "Billions", budget * 1000, if(f.unit = "Thousands", budget / 1000, budget)) as budget,
	if(f.unit = "Billions", revenue * 1000, if(f.unit = "Thousands", revenue / 1000, revenue)) as revenue,
	f.currency
	from movies m
	join financials f
	on m.movie_id = f.movie_id
)
select *,
sum(budget) over(partition by studio) as total_studio_spent
from t1;