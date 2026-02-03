use moviesdb;

-- Print number of movies that belong to Bollywood industry
select count(*)
from movies
where industry = "bollywood";

-- Print number of movies that belong to Hollywood industry
select count(*)
from movies
where industry = "hollywood";

-- Print count of movies for each industry beside their names
/*
industry	count
Bollywood	18
Hollywood	21
*/
select industry, count(*)
from movies
group by industry;

select title, industry, count(*)
from movies
group by industry;

select industry, max(title), count(*)
from movies
group by industry;

-- What does it mean by max(title) & min(title)
select title
from movies
where industry = "Hollywood"
order by title;

select industry, title
from movies
group by industry;

select studio, count(*) as no_of_movies
from movies
group by studio;

-- Print average imdb_rating for each industry, also round off ratings after 1 decimal place
select industry,
round(avg(imdb_rating), 1) as avg_rating
from movies
group by industry;

-- Print minimum ratings, maximum ratings & avg ratings for each studio
select studio,
min(imdb_rating) as min_rating,
max(imdb_rating) as max_rating,
round(avg(imdb_rating), 1) as avg_rating
from movies
group by studio;

-- Print maximum, minimum and average rating of each studio. 
-- Return your answer in such a way that the studio with highest average ratings appears first and the one with least average ratings goes at the end. 
select studio,
min(imdb_rating) as min_rating,
max(imdb_rating) as max_rating,
round(avg(imdb_rating), 1) as avg_rating
from movies
group by studio
-- order by avg_rating desc;
-- order by round(avg(imdb_rating), 1) desc;
order by 4 desc;

select industry, studio, count(*)
from movies
group by industry, studio;

use hr2;
select * from employees;
select department_id, manager_id, count(*) 
from employees
group by department_id, manager_id;

use hr;
select * from employees;
-- Print number of employee working in each department
select department_id, count(*)
from employees
group by department_id
order by 2 desc;

-- Print number of employee working in each department only for department_id 3, 4, 6 & 9
select department_id, count(*)
from employees
where department_id in (3,4,6,9)
group by department_id;

-- Print number of employee working in each department only for even department_id
select department_id, count(*)
from employees
where department_id % 2 = 0
group by department_id;

-- Print total salary paid in each department for odd department_ids
select department_id, sum(salary)
from employees
where department_id % 2 != 0
group by department_id;

-- Print number of employees working in each department for only those department which have more than 3 employees working
select department_id, count(*)
from employees
-- where count(*) > 3
group by department_id
having count(*) > 3;

-- For odd department_ids, print number of employee working in each department which have more than 3 employees
select department_id, count(*) as no_of_employees
from employees
where department_id % 2 != 0
group by department_id
having no_of_employees > 3;

-- Print the number of movies produced by all those studio which have produced more than 2 movies
use moviesdb;
select studio, count(*) as no_of_movies
from movies
group by studio
having no_of_movies > 2;

select studio, count(*)
from movies
group by studio
order by studio;

-- Print all the Bollywood movie studios with the release year of their last movie
select studio, max(release_year)
from movies
where industry = "Bollywood"
group by studio;