-- Print names of actors beside title of each movie. Return movie_id, title, actor_id and name of the actor.
use moviesdb;
select title, name
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
join actors a on ma.actor_id = a.actor_id;

-- Print name of each country along with number of employees working in that country. Use hr dataset.
use hr;
select country_name, count(employee_id) as no_of_employees
from countries c
left join locations l on c.country_id = l.country_id
left join departments d on l.location_id = d.location_id
left join employees e on d.department_id = e.department_id
group by country_name
order by 2 desc;

select country_name, count(employee_id) as no_of_employees
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id
right join countries c on l.country_id = c.country_id
group by country_name
order by 2 desc;

-- Print average imdb_rating of each actor beside their names. If an actor has not played role in any movie, then put 0 as their average imdb_rating.
use moviesdb;
select a.name, ifnull(round(avg(imdb_rating), 1), 0) as avg_rating
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
right join actors a on a.actor_id = ma.actor_id
group by a.name
order by 1;

/*
Display department name and the total number of employees who have ever worked in that department (either currently or as recorded in job history), 
and classify departments as active or less active based on that total. Use hr2.
*/
use hr2;

select distinct e.employee_id, e.department_id as current_dep, jh.department_id as prev_dep
from employees e
left join job_history jh on e.employee_id = jh.employee_id
left join departments d on e.department_id = d.department_id
order by 1;

select d.department_name, count(employee_id) as total_employees,
if(count(employee_id) >= 5, "Active", "Less Active") as "status"
from (
	select employee_id, department_id from employees
	union
	select employee_id, department_id from job_history
) as t
right join departments d on t.department_id = d.department_id
group by d.department_id;

