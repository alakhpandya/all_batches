use moviesdb;
select * from languages;
-- Print number of movies created in each language
-- select *
select l.name, count(title)
from languages l
LEFT join movies m
on l.language_id = m.language_id
group by l.name;

/*
Print number of movies played by each actor beside his/her id sorted in ascending order of actor_id. 
If some actor has not played role in any movie then show "0" beside their id.
*/
select a.actor_id, count(birth_year)
from movie_actor ma
right join actors a
on ma.actor_id = a.actor_id
group by a.actor_id;

-- Print names of actors who haven't played role in any movie.
select a.name, count(movie_id)
from movie_actor ma
right join actors a
on ma.actor_id = a.actor_id
group by a.name
having count(movie_id) = 0;

use hr2;

/*
Display all departments along with employee names working in them.
Include departments even if no employees are assigned. Use hr2 database.
*/
select d.department_name, e.first_name, e.last_name
from departments d
left join employees e
on d.department_id = e.department_id;

/*
Display all employees along with their dependent names.
Show "0" beside employees who do not have any dependents. Use hr database.
*/
select e.employee_id, ifnull(d.dependent_id, 0) as dependent_id, coalesce(d.first_name, 0) as first_name,
case
	when d.last_name is null then 0
    else d.last_name
end as last_name
from employees e
left join dependents d
on e.employee_id = d.employee_id
order by e.employee_id;

/*
Display all jobs along with employee names assigned to those jobs.
Also print job roles that currently have no employees. Use hr database.
*/
select j.job_id, j.job_title, e.employee_id, e.first_name
from jobs j
left join employees e
on j.job_id = e.job_id;

/*
Display all locations along with department names.
Include locations that do not have any departments.
*/
