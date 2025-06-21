use classwork;

with t1 as (
	select user1, user2
	from facebook_friends
	union
	select user2, user1
	from facebook_friends
),
t2 as (
	select user1, count(user2) as friends
	from t1
	group by user1
)
select user1, friends*100/(select count(distinct(user1)) from t1) as popularity_pct
from t2
order by user1;

-- 1. In moviesdb database, print all the columns of movies table along with average rating of each studio beside them

-- 2. Print the artist names appearing more than once. Use 'artists' table from 'paintings' database

/*
3. Using 'student_score' database, allot department-wise roll number to each student. 
For example, students in Biochemistry department will have roll numbers 1, 2 & 3 (as there are only 3 students in this
department) then students of Computer Science department will have roll numbers 1, 2, 3 & 4 and so on.
*/
use classwork;
select *,
row_number() over(partition by dep_name order by student_name) as roll_no
from student_score;

select *,
row_number() over(partition by dep_name order by score desc) as roll_no
from student_score;

-- Print top-3 earners from each department. Use hr2 database.
use hr2;
with t1 as (
	select *,
    rank() over(partition by department_id order by salary desc) as salary_rank,
    dense_rank() over(partition by department_id order by salary desc) as salary_dense_rank
    from employees
)
select department_id, salary
from t1
where salary_rank <= 3;

use classwork;
select *,
-- percent_rank() over(partition by dep_name)
-- percent_rank() over(order by score) * 100 as percentile, 
round(percent_rank() over(partition by dep_name order by score) * 100, 2) as percentile
from student_score;

-- Divide students of each department into two groups - team-1 & team-2
select *,
ntile(2) over(partition by dep_name) as team,
ntile(2) over(partition by dep_name order by score) as new_team
from student_score;

-- 1. In moviesdb database, print all the columns of movies table along with average rating of each studio beside them
use moviesdb;
select *,
round(avg(imdb_rating) over(), 1) as total_avg_rating,
round(avg(imdb_rating) over(partition by studio), 1) as studio_avg_rating
from movies;


select *,
count(*) over(partition by studio) as no_of_movies,
min(release_year) over(partition by studio) as first_movie_year,
max(release_year) over(partition by studio) as latest_movie_year
from movies;

-- sum() window function
use hr;
select *,
-- sum(salary) over() total_salary
sum(salary) over(partition by department_id) dep_total_salary
from employees;