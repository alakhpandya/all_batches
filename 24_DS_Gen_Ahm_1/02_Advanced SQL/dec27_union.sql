-- Union & Union All
/*
Find the popularity percentage for each user on Meta/Facebook. 
The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, 
then converted into a percentage by multiplying by 100. Output each user along with their popularity percentage. 
Order records in ascending order by user id.

Create table If Not Exists facebook_friends (user1 int, user2 int);
Truncate table facebook_friends;
insert into facebook_friends values
(2, 1),
(1, 3),
(4, 1),
(1, 5),
(1, 6),
(2, 6),
(7, 2),
(8, 3),
(3, 9);
*/
use classwork;

-- Unique users
-- all

with unique_users as (
	select user1 from facebook_friends
	union
	select user2 from facebook_friends
),
all_users as (
	select user1 as usr from facebook_friends
	union all
	select user2 as usr from facebook_friends
),
no_of_friends as (
	select usr, count(*) as friends
    from all_users
    group by usr
),
total_users as (
	select count(*) as total
    from unique_users
)
select usr as users, round(friends * 100/total, 2) as popularity_pct
from no_of_friends
cross join total_users
order by usr;

/*
select user1 as usr from facebook_friends
union all
select user2 as usr from facebook_friends;

select * from facebook_friends;
*/