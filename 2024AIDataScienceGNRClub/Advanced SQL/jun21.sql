-- lag, lead, first_value, last_value & nth_value
use classwork;
select * from student_score;

select *,
-- lead(student_name) over()
-- lead(score) over()
-- lead(score) over(partition by dep_name)
lead(score, 2) over()
from student_score;

select *,
-- lag(student_name) over()
-- lag(student_name, 3) over()
lag(student_name) over(partition by dep_name)
from student_score;

select *,
-- first_value(student_name) over(),
last_value(student_name) over(partition by dep_name)
from student_score;

select *,
nth_value(student_name, 3) over()
from student_score;