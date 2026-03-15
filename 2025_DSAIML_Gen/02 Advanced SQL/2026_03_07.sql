use moviesdb;

select a.actor_id, a.name
from actors a
left join movie_actor ma on a.actor_id = ma.actor_id
group by a.actor_id
having count(movie_id) = 0;

/*
Display all employees along with their dependent names.
Show "0" beside employees who do not have any dependents. Use hr database.
*/
use hr;
select * from dependents;
select e.employee_id, concat(e.first_name, " ", e.last_name) as employee_name, 
case
	when d.dependent_id is null then 0
    else concat(d.first_name, " ", d.last_name)
end as dependent_name
from employees e
left join dependents d on e.employee_id = d.employee_id
order by e.employee_id;

/*
Display all jobs along with employee names assigned to those jobs.
Also print job roles that currently have no employees. Use hr database.
*/
select j.job_title, e.*
from jobs j
left join employees e on j.job_id = e.job_id
order by employee_id;

/*
Display all locations along with department names.
Include locations that do not have any departments.
*/
