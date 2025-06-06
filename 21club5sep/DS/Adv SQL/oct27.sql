use classwork;

select * from student_score;
/*
select distinct dep_name, 
avg(score) over(partition by dep_name order by score) as avg_score
from student_score;
*/
/*
select student_name, dep_name, score,
avg(score) over(partition by dep_name order by score rows between unbounded preceding and unbounded following) as avg_score
from student_score;
*/
select student_name, dep_name, score,
-- avg(score) over(partition by dep_name order by score rows between unbounded preceding and 0 following) as avg_score
-- avg(score) over(partition by dep_name order by score rows between 1 preceding and 1 following) as avg_score
avg(score) over(partition by dep_name order by score rows between 0 preceding and unbounded following) as avg_score
from student_score;