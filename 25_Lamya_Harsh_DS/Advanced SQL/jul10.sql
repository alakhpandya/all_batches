use hr;
-- Print the artist names appearing more than once. Use 'artists' table from 'paintings' database
use paintings;

select *,
row_number() over() as row_num
from artists;

/*
Using 'student_score' database, allot department-wise roll number to each student. 
For example, students in Biochemistry department will have roll numbers 1, 2 & 3 (as there are only 3 students in this
department) then students of Computer Science department will have roll numbers 1, 2, 3 & 4 and so on.
*/
use classwork;
select *,
row_number() over(partition by dep_name) as roll_no
from student_score;

-- difference between group by & partition by:
select dep_name, count(*)
from student_score
group by dep_name;

use paintings;
with t1 as (
	select *,
	row_number() over(partition by first_name, last_name) as row_num
	from artists
)
select *
from t1
where row_num > 1;

-- Re-allot the roll numbers in the alphabetical order of student_name
use classwork;
select *,
row_number() over(partition by dep_name order by student_name) as roll_no
from student_score;

select *,
row_number() over(order by student_name) as roll_no
from student_score;

-- Print top-3 earners from each department in employees table of hr database
use hr;
with t1 as (
	select *,
	row_number() over(partition by department_id order by salary desc) as earner_row_num,
	rank() over(partition by department_id order by salary desc) as earner_rank,
	dense_rank() over(partition by department_id order by salary desc) as earner_dense_rank
	from employees
)
select * from t1;
-- where earner <= 3;

use classwork;
select *,
round(percent_rank() over(partition by dep_name order by score)*100, 2) as percentile
from student_score;

-- We want to organize an intra-department quiz competition. Divide students of each department into two groups to compete with each other.
-- Assign more student in the first group if there are odd number of students in a department.
select *,
-- ntile(2) over() as grp
-- ntile(2) over(partition by dep_name) as grp
-- ntile(3) over(partition by dep_name) as grp
ntile(2) over(partition by dep_name order by score) as grp
from student_score;