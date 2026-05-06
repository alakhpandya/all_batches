-- Print all the departments in which no employees are working
use hr2;
select d.department_id, d.department_name 
from employees e
right join departments d
on e.department_id = d.department_id
where e.department_id is null;

-- Print all the employees whose department_id is missing. Do it using left/right join.
select e.* 
from employees e
left join departments d
on e.department_id = d.department_id
where e.department_id is null;

-- Print all the actors who have not played role in any movie. Use moviesdb database.
use moviesdb;
-- Print all the movies whose actors details is not available


-- Using hr2, print all the details of every employee & department that includes employees without department as well as departments without employees.
-- There is no outer join in MySQL
use hr2;
select *
from employees e
right join departments d
on e.department_id = d.department_id
union
select * 
from employees e
left join departments d
on e.department_id = d.department_id;