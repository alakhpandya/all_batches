use classwork;
-- Swap the names of each two adjacent students.  Use students table from classwork database.
select *,
case
	when id % 2 = 0 then lag(student_name, 1) over()
 -- else coalesce(lead(student_name, 1) over(), student_name)
	else ifnull(lead(student_name, 1) over(), student_name)
end as new_order
from students;

select * from students;

/*
Get me the running total of points for each group_name in the `player` table from `classwork` database
*/
use classwork;
select *, 
-- sum(points) over(partition by group_name order by id) 
sum(points) over(partition by group_name rows between unbounded preceding and current row) 
from player;

-- Calculate the running totals for the number of new subscribers separately for each network from `subscribers` table of `classwork` database.

/*
From the `subscribers` table of `classwork` database, for each social_network show:
1. The number of new subscribers added on the first day and, 
2. The number of new subscribers added on the last day
*/
select *,
first_value(new_subscribers) over(partition by social_network) as first_day,
last_value(new_subscribers) over(partition by social_network) as last_day
from subscribers;
select * from subscribers;