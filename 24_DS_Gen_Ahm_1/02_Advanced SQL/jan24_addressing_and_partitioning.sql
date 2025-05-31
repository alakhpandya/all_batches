-- Get me the running total of points for each group_name in the `player` table from `classwork` database

use classwork;

select * from player;
select *,
sum(points) over(partition by group_name order by full_name) as total
from player;

-- We can also get the same output by this query
select *,
sum(points) over(partition by group_name order by full_name rows unbounded preceding) as total
from player;

select * from student_score;
select *,
sum(score) over(partition by dep_name order by student_name rows between 1 preceding and 1 following) as total
from student_score;

select *,
sum(score) over(partition by dep_name rows between unbounded preceding and unbounded following) as total
from student_score;

select *,
-- sum(score) over(partition by dep_name rows between unbounded preceding and current row) as total
sum(score) over(partition by dep_name rows unbounded preceding) as total
from student_score;

select * from player
order by group_name, id;

select *, 
-- sum(points) over(partition by group_name order by id rows 2 preceding) 
sum(points) over(partition by group_name order by id rows between 2 preceding and current row) 
from player;

/*
155.85
155.85+188.58
155.85+188.58+81.09
188.58+81.09+188.59
*/

select *, 
count(*) over(partition by group_name order by id rows between current row and 1 following) 
from player;

select * from weather;