use classwork;
select * from student_score;

-- Indexing & Partitioning
select student_id, dep_name, score,
-- avg(score) over(partition by dep_name order by score rows between unbounded preceding and unbounded following) as avg_score
-- avg(score) over(partition by dep_name order by score rows between unbounded preceding and 0 following) as avg_score
avg(score) over(partition by dep_name order by score rows between 1 preceding and 1 following) as avg_score
from student_score;