-- Display the average IMDb rating for movies in each language.
use moviesdb;

select * from movies;
select * from languages;

select l.name, avg(imdb_rating)
from movies m
join languages l
on m.language_id = l.language_id
group by l.name;

-- Display each currency and the total number of movies recorded under that currency.
select f.currency, count(m.movie_id)
from movies m
join financials f
on m.movie_id = f.movie_id
group by f.currency;

-- Calculate the average movie budget for each currency.
select currency, round(avg(budget), 2)
from financials
group by currency;

-- Print minimum, maximum & average budget of each Bollywood studio
select m.studio, min(f.budget) as min_budget, max(f.budget) as max_budget, round(avg(f.budget), 2) as avg_budget
from movies m
join financials f
on m.movie_id = f.movie_id
where industry = "Bollywood" and m.studio != ""
group by m.studio;

-- Display actor id along with the average IMDb rating of the movies they have acted in.
select ma.actor_id, round(avg(m.imdb_rating), 1) as avg_rating
from movies m
join movie_actor ma
on m.movie_id = ma.movie_id
group by ma.actor_id;

-- Find the average IMDb rating of movies for each industry and language combination



-- Display actor name along with the average IMDb rating of the movies they have acted in.



-- More about group by
use hr;
select * from employees order by department_id;
select distinct department_id 
from employees;

-- Query-1:
select department_id, sum(salary) total_salary
from employees
group by department_id
order by department_id;

-- Query-2:
select manager_id, sum(salary) total_salary
from employees
group by manager_id
order by manager_id;

-- Query-3:
select department_id, manager_id, sum(salary) total_salary
from employees
-- where department_id = 3 and manager_id = 114
-- where manager_id in (100, 114, 120)
where employee_id % 2 = 0
group by department_id, manager_id
-- having total_salary >= 10000
order by department_id;
