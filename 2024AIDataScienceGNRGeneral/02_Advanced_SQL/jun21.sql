-- lead, lag, first_value, last_value, nth_value
use classwork;
select *,
-- lead(student_name) over(),
-- lag(student_name) over()
-- lead(score) over(partition by dep_name)
lag(student_name) over(partition by dep_name order by score)
from student_score;

-- writing two columns in partition by:
use hr;
select *,
row_number() over(partition by department_id, job_id order by salary) as temp 
from employees;

select employee_id, first_name, last_name, salary, department_id,
lead(salary, 2) over(partition by department_id order by employee_id),
lag(first_name, 3) over(partition by department_id order by employee_id)
from employees;

use classwork;
select *,
first_value(student_name) over(partition by dep_name order by score desc),
last_value(student_name) over(partition by dep_name order by score desc)
from student_score;

use hr2;
select employee_id, first_name, last_name, salary, department_id,
nth_value(first_name, 3) over(partition by department_id)
from employees;

-- Frames in window functions
use classwork;
-- print 3 days moving average of city-wise precipitation
select *,
-- sum(precipitation) over(partition by city)
round(avg(precipitation) over(partition by city rows between 1 preceding and 1 following), 2) as three_days_moving_avg
from weather;

-- Get me the total_salary_paid in the employee table of hr database
use hr;
select employee_id, first_name, last_name, salary, department_id,
-- sum(salary) over(partition by department_id) as dep_total_salary
sum(salary) over(rows between unbounded preceding and current row) as total_salary_paid
from employees;

-- what is the default value of rows between in the following query?
select employee_id, first_name, last_name, salary, department_id,
-- sum(salary) over(partition by department_id) as dep_total_salary
sum(salary) over(partition by department_id rows between unbounded preceding and unbounded following) as dep_total_salary
from employees;

-- what is the default value of rows between in the following query?
select employee_id, first_name, last_name, salary, department_id,
sum(salary) over(partition by department_id order by employee_id rows between unbounded preceding and current row) as total_salary_paid
-- rows between unbounded preceding and current row
from employees;

-- Any aggregate window function will give you running total/running average/running count etc when we write order by in it.
-- Options:
/*
rows between unbounded preceding and unbounded following
rows between unbounded preceding and current row
rows between current row and unbounded following
rows between X preceding and Y following
rows between X preceding and current row
rows between current row and Y following
*/

-- OTAP & OLAP 