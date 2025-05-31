use hr2;

select * from employees
order by department_id;

select department_id, avg(salary)
from employees
group by department_id;

/*
Print a table that has all the columns of all 107 employees (from hr2 database) from employees table along with average salary of their corresponding department.
*/
with t1 as
(
	select department_id, avg(salary) as dep_avg_salary
	from employees group by department_id
)
select * from employees as e
-- join t1 on e.department_id = t1.department_id;
join t1 using(department_id);

/*
In moviesdb database, print all the columns of movies table along with average rating of each studio beside them
*/
use moviesdb;
select *, (select avg(imdb_rating) from movies m1 where m1.studio = m2.studio) as studio_avg_ratings
from movies m2;


-- Print the artist names appearing more than once
use paintings;
select * from artists;

select first_name,last_name 
from artists group by first_name,last_name 
having count(*)>1;
/*
Give department-wise roll number to each student. For example, students in Biochemistry department will have roll numbers 1, 2 & 3 (as there are only 3 students in this
department) then students of Computer Science department will have roll numbers 1, 2, 3 & 4 and so on.
*/
select * from student_score
order by dep_name;