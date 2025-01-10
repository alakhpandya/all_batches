-- Joins
/*
use hr;
select department_id, round(avg(salary), 0) as dept_avg_salary 
from employees
group by department_id;

select first_name, last_name, salary, department_id,
case
	when salary > (select avg(salary) from employees where department_id = e.department_id) then "Above Avg"
    else "Below Avg"
end as nature
from employees e;

use moviesdb;
select * from movies;
select * from financials;
*/
/*
Get me the columns movie_id, title, revenue, budget & profit (profit = revenue - budget) sorted in the descending order of their profit.
*/

select m.movie_id, title, revenue, budget, revenue - budget as profit
from movies m
join financials f
on m.movie_id = f.movie_id
order by 5 desc;

/*
create database if not exists temp;
use temp;
select * from articles;

drop database if exists temp;
*/
-- select * from;
use moviesdb;
select title, name as language
from movies m
left join languages l
on l.language_id = m.language_id;
-- using(language_id);

