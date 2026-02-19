use hr2;

-- Display employees who have a salary greater than every employee in department 50.
select employee_id, first_name, last_name, salary
from employees
where salary > (
	select max(salary)
    from employees
    where department_id = 50
);

-- Display employees whose salary is among the top 3 highest salaries in the company.
select *
from employees
order by salary desc
limit 3;

select *
from employees e1
where (
	select count(distinct(salary))
    from employees e2
    where e2.salary > e1.salary
) < 3;


use moviesdb;
-- Display movies whose IMDb rating is higher than the average IMDb rating of movies in the same industry.
select *
from movies m1
where imdb_rating > (
	select avg(imdb_rating) from movies m2
    where m1.industry = m2.industry
);

-- Display actors who have acted in more movies than the average number of movies per actor.
select actor_id
from movie_actor
group by actor_id
having count(distinct movie_id) > (
	select count(distinct movie_id)/count(distinct actor_id) as avg_movies_per_actor 
    from movie_actor
);