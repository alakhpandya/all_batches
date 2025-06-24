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

-- Fetch two employees from each department who joined first. Use hr dataset.
/*
Find the number of emails received by each user under each built in email label. 
The email labels are: ‘Promotion’, ‘Social’ and ‘Shopping’. Output the user along with the number of promotion, social & shopping emails they got. 
Use google_gmail database.
*/


-- HW
/*
1. Swap the names of each two adjacent students. Use students database.
2. Calculate the three-days moving average temperature separately for each city from `weather` table of `classwork` database. 
Give your answer rounded off after one decimal place.
3. Calculate the total precipitation for the last three days (i.e. a three-day running total) separately for both the cities from `weather` table of `classwork` database.
4. Calculate the running totals for the number of new subscribers separately for each network from `subscribers` table of `classwork` database.
5. From the `subscribers` table of `classwork` database, for each social_network show:
	A. The number of new subscribers added on the first day and, 
	B. The number of new subscribers added on the last day
6. Get me the running total of points for each group_name in the `player` table from `classwork` database
7. Answer the following questions from the "farmer's market" database:
	A. Give me the maximum original_price for each vendor
    B. Rank the products in each vendor’s inventory based on original_price so that expensive products get smaller rank
    C. As a famer, you want to figure out which of your products were above the average price per product on each market date. Find it out.
*/