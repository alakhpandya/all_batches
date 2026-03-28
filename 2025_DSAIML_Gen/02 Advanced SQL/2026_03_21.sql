use classwork;
select *,
-- row_number() over(partition by dep_name)
-- row_number() over(partition by dep_name order by score desc) as ranking
row_number() over(partition by dep_name order by student_name) as roll_no
from student_score;
-- order by score desc;

-- From hr dataset, get me the top 2 earners from each department
use hr;
with t as (
	select *,
 -- row_number() over(partition by department_id order by salary desc) as earner_rank
	rank() over(partition by department_id order by salary desc) as earner_rank,
	dense_rank() over(partition by department_id order by salary desc) as earner_dense_rank
	from employees
)
select * from t;

use classwork;
select *,
-- percent_rank() over(partition by dep_name order by score) as percentile
-- ntile(2) over() as group_no
ntile(2) over(partition by dep_name) as group_no,
ntile(3) over(partition by dep_name order by score desc) as new_group_no
from student_score;

-- Value Window Functions
select *,
-- lead(student_name) over() as lead_result
-- lead(student_name, 2) over() as lead_result
lead(student_name) over(partition by dep_name order by student_name) as lead_result,
lag(student_name) over(partition by dep_name order by student_name) as lag_result,
first_value(student_name) over(partition by dep_name order by student_name) as first_student,
last_value(student_name) over(partition by dep_name order by student_name) as last_student,
nth_value(student_name, 3) over() as nth_student
from student_score;

-- Print 5 most profitable movies of each industry

-- Get top earner from each department & then return only top 5 amongst them. Use hr2 database.

-- Fetch two employees from each department who joined first along with their job_title, department_name and region_name. Use hr2 database.

-- Swap the names of each two adjacent students.  Use students table from classwork database.
select *,
	case
		when id % 2 = 0 then lag(student_name) over()
        else ifnull(lead(student_name) over(), student_name)
	end as swapped
from students;

/*
Find the number of emails received by each user under each built in email label. The email labels are: ‘Promotion’, ‘Social’ and ‘Shopping’. 
Output the user along with the number of promotion, social & shopping emails they got. Use google_gmail database.
*/