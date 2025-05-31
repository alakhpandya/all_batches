-- Window Functions - contd

use classwork;

select * from student_score;

/*
Find the average marks of each department & create a new column that has +, - or 0 beside each student depending on if he/she has scored 
above avg, below avg or avg of their respective department.
*/
select *,
avg(score) over()
as avg_marks
from student_score;

select *,
avg(score) over(partition by dep_name)
as dep_avg_marks
from student_score;

with cte as
(
	select *,
	avg(score) over(partition by dep_name)
	as dep_avg_marks
	from student_score
)
select *,
if(score > dep_avg_marks, "+", if(score = dep_avg_marks, "0", "-")) as result
from cte;

-- Other Aggregate window functions
select *,
max(score) over(partition by dep_name) as dep_max,
min(score) over(partition by dep_name) as dep_min,
avg(score) over(partition by dep_name) as dep_avg,
sum(score) over(partition by dep_name) as dep_total,
count(score) over(partition by dep_name) as dep_count
from student_score;

-- Recap of NTILE
select *,
-- ntile(3) over()
-- ntile(5) over() as grp_no
-- ntile(2) over(partition by dep_name) as grp_no
ntile(2) over(partition by dep_name order by score) as grp_no
from student_score
order by student_id;

-- Value window functions: lead, lag, first_value, last_value, nth_value
select *,
first_value(score) over() as fst_val,
last_value(score) over() as last_val
from student_score;

select *,
first_value(score) over(partition by dep_name) as dep_fst_val,
last_value(score) over(partition by dep_name) as dep_last_val
from student_score;

select *,
first_value(score) over(partition by dep_name order by student_name) as dep_fst_val
from student_score;

select *,
lead(score) over(),
lag(score) over()
from student_score;

select *,
lead(score) over(partition by dep_name order by score),
lag(score) over(partition by dep_name order by score)
from student_score;

select *,
nth_value(score, 2) over()
from student_score;

select *,
nth_value(score, 2) over(partition by dep_name)
from student_score;

-- Addressing & Partitioning
select *,
round(avg(temperature) over(partition by city), 2) as city_avg_temp
from weather;

select *,
-- avg(precipitation) over(partition by city) as city_avg_rain
-- avg(precipitation) over(partition by city rows between unbounded preceding and unbounded following) as city_avg_rain
-- avg(precipitation) over(partition by city rows between 1 preceding and 1 following) as 3_day_moving_avg_rain
-- avg(precipitation) over(partition by city rows between 1 preceding and 2 following)
avg(temperature) over(partition by city rows between unbounded preceding and current row) as running_avg_temp,
sum(precipitation) over(partition by city rows between unbounded preceding and current row) as running_total_rain
from weather;

select *,
first_value(score) over(partition by dep_name order by score) as dep_fst_val,
-- last_value(score) over(partition by dep_name order by score rows between unbounded preceding and current row) as dep_last_val
last_value(score) over(partition by dep_name order by score rows between unbounded preceding and unbounded following) as dep_last_val
from student_score;

select *,
sum(precipitation) over(partition by city rows between current row and unbounded following) as running_total_rain
from weather;