/*
Find the popularity percentage for each user on Meta/Facebook. 
The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, 
then converted into a percentage by multiplying by 100. Output each user along with their popularity percentage. 
Order records in ascending order by user id.
*/

use classwork;

with all_users as (
	select user1, user2 from facebook_friends
	union
	select user2, user1 from facebook_friends
),
friends as (
	select user1, count(user2) as friends_count from all_users group by user1
)
select user1, friends_count*100/(select count(user1) from friends) as popularity_pct
from friends
order by user1;

use hr2;
select e.employee_id, e.first_name, e.last_name, e.department_id, d.department_id, d.department_name from employees e
left join departments d on e.department_id = d.department_id
union
select e.employee_id, e.first_name, e.last_name, e.department_id, d.department_id, d.department_name from employees e
right join departments d on e.department_id = d.department_id;


use demo;
select "cars" as product_line from products;