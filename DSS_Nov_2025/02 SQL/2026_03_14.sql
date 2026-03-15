-- Value Window Function
use classwork;

-- Lead & Lag
select *,
-- lead(student_name, 1) over() as new_col
-- lead(dep_name, 2) over() as new_col
-- lead(student_name, 1) over(partition by dep_name) as new_col
lead(student_name, 1) over(partition by dep_name order by score) as lead_col,
lag(student_name, 1) over(partition by dep_name order by score) as lag_col
from student_score;

-- first_value, last_value & nth_value
select *,
-- first_value(student_name) over() as first_stu
-- first_value(student_name) over(partition by dep_name) as first_stu
first_value(student_name) over(partition by dep_name order by score) as poor_stu,
last_value(student_name) over(partition by dep_name order by score) as test,
last_value(student_name) over(partition by dep_name order by score rows between unbounded preceding and unbounded following) as best_stu
-- nth_value(student_name, 2) over(partition by dep_name order by score desc, student_name asc rows between unbounded preceding and unbounded following) as second_best_stu
from student_score;

-- Frames in window functions
with t1 as (
	select *,
	round(avg(temperature) over(partition by city), 1) as city_avg_temp
	from weather
	order by city
)
select *, round(temperature - city_avg_temp, 1) as difference
from t1;

select *,
-- sum(precipitation) over(partition by city rows between 1 preceding and 1 following) as total_precipitation
-- sum(precipitation) over(partition by city rows between 1 preceding and current row) as total_precipitation
-- sum(precipitation) over(partition by city rows between current row and 2 following) as total_precipitation
sum(precipitation) over(partition by city rows between unbounded preceding and current row) as running_total_precipitation
from weather
order by city;

select *,
avg(precipitation) over(partition by city order by date rows between 1 preceding and 1 following) as "3_day_moving_avg"
from weather;

-- Default frame in most window functions: rows between unbounded preceding and unbounded following
-- select * from students;