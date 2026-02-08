use moviesdb;

-- Print names of actors beside title of each movie. Return movie_id, title, actor_id and name of the actor.
select m.movie_id, m.title, a.actor_id, a.name
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
join actors a on ma.actor_id = a.actor_id;

use hr;
-- Print location of each eamployee. Return employee_id, first_name, last_name, department_name and city columns.
select e.employee_id, e.first_name, e.last_name, d.department_name, l.city
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id;

-- Print name of each country along with number of departments working in that country.
select c.country_name, count(d.department_id)
from countries c
join locations l on c.country_id = l.country_id
join departments d on d.location_id = l.location_id
group by c.country_name;

-- Return department name of each job title. Show job_id, job_title, department_id and department_name columns.
select distinct j.job_id, j.job_title, d.department_id, d.department_name
from jobs j
join employees e on j.job_id = e.job_id
join departments d on e.department_id = d.department_id
order by j.job_id, d.department_id;



-- Print names of actors along with the titles of movies they have played role in.
use moviesdb;
select a.actor_id, a.name, m.movie_id, m.title
from actors a
left join movie_actor ma on a.actor_id = ma.actor_id
left join movies m on ma.movie_id = m.movie_id
order by a.actor_id;

-- Print name of each country along with number of departments working in that country. Also show the countries in which no department is working.
-- OR
-- Print name of each country along with number of departments working in that country. If there is no department working in a country then print 0 beside its name
use hr;
select c.country_name, count(d.department_id) as no_of_dep
from countries c
join locations l on c.country_id = l.country_id
left join departments d on l.location_id = d.location_id
group by c.country_name
order by 2 desc;

-- Use hr2 for the following questions:
-- 1. Display employee first name, last name, job title, and department name for all employees.
use hr2;
select e.first_name, e.last_name, j.job_title, d.department_name
from employees e
left join jobs j on e.job_id = j.job_id
left join departments d on e.department_id = d.department_id;

-- Display each department name and the total number of employees currently working in that department, including departments with no employees.
select d.department_name, count(e.employee_id) as no_of_employees
from departments d
left join employees e 
on d.department_id = e.department_id
group by d.department_name;

-- Display country name and the number of different cities present in each country including the countries which do not have any city




/*
Display job titles and the average salary of employees working in each job, and classify each job as high paying if the avg_salary is above 15000, low paying 
if the avg_salary is below 1000 otherwise medium_salary.
*/
select * from jobs;
select j.job_title, avg(e.salary) as avg_salary
from jobs j
left join employees e on e.job_id = j.job_id
group by j.job_title;



-- Display all departments along with the city where they are located, including departments that do not have any employees.

-- Display employee name, job title, and indicate whether the employee’s salary falls within the minimum and maximum salary defined for that job.

/*
Display department name and city, along with the total number of employees in each department, and classify departments as small, medium, or large based on 
employee count.
*/

-- Display region name and the total number of employees working in that region, including regions where no employees are currently working.

/*
Display department name and the total number of employees who have ever worked in that department (either currently or as recorded in job history), 
and classify departments as active or less active based on that total.
*/