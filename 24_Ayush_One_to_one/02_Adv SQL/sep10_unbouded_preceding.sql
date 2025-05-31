use classwork;

select * from player;
-- Get me the running total of points for each group

select *,
-- sum(points) over(partition by group_name order by id rows unbounded preceding) as running_total
-- sum(points) over(partition by group_name order by id rows 2 preceding) as running_total
-- count(*) over(partition by group_name order by id range between 1 preceding and 2 following) as count4
-- count(*) over(partition by group_name order by id range between unbounded preceding and unbounded following) as count4
-- count(*) over(partition by group_name order by id range between current row and unbounded following) as count4
count(*) over(partition by group_name order by id range between 5 preceding and current row) as count4
from player;

