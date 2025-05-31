-- Union & Union All
-- facebook friends
select * from facebook_friends;

/*
Find the popularity percentage for each user on Meta/Facebook. 
The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, 
then converted into a percentage by multiplying by 100. 
Output each user along with their popularity percentage. Order records in ascending order by user id.
*/


-- Part-1: Print all users & their friends count
use classwork;
with all_friends as (
	select user1, user2 from facebook_friends
	union
	select user2, user1 from facebook_friends
)
select user1, count(*) as friends, count(user2)*100/(select count(distinct user1) from all_friends) as popularity_pct
from all_friends
group by user1
order by user1;

/*
Identify how many cars, motorcycles, trains and ships are available in the inventory. 
Treat all types of cars just as “Cars”. DO NOT USE ‘LIKE’ IN THIS EXAMPLE. (Use 'products' table from ‘demo’ database)
*/
use demo;
select product_line, count(*) 
from products
group by product_line;

SELECT 
    CASE 
        WHEN product_line in ('Classic Cars', 'Vintage Cars') THEN 'Cars'
        ELSE product_line
	END AS new_product_line,
    count(*) as inventory
from products
where product_line in ('Classic Cars', 'Vintage Cars', 'Motorcycles', 'Ships')
group by new_product_line;

select product_line, count(*)
from products
where product_line in ('Motorcycles', 'Ships')
group by product_line
union
select "Cars" as product_line, count(*)
from products
where product_line in ('Vintage Cars', 'Classic Cars')
group by "Cars";

/*
Print a table that has all the columns of all 107 employees (from hr2 database) from employees table along with average salary of their corresponding department.
*/
use hr2;
select * from employees
order by department_id;

-- Homework Questions:
/*
1. In moviesdb database, print all the columns of movies table along with average rating of each studio beside them
2. Print the artist names appearing more than once. Use 'artists' table from 'paintings' database
3. Using 'student_score' database, allot department-wise roll number to each student. For example, students in Biochemistry department will have roll numbers 1, 2 & 3 (as there are only 3 students in this
department) then students of Computer Science department will have roll numbers 1, 2, 3 & 4 and so on.
*/
