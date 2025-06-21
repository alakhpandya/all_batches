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

-- Fetch two employees from each department who joined first. Use hr dataset.

-- Print top 3 earners from each department. Use hr2 database.

/*
•Find the number of emails received by each user under each built in email label. 
The email labels are: ‘Promotion’, ‘Social’ and ‘Shopping’. Output the user along with the number of promotion, social & shopping emails they got. 
Use google_gmail database.
*/

use classwork;
select to_user,
sum(case when label = "Promotion" then 1 else 0 end) as Promotion_mails,
sum(case when label = "Social" then 1 else 0 end) as Social_mails,
sum(case when label = "Shopping" then 1 else 0 end) as Shopping_mails
from google_gmail_emails as ge
join google_gmail_labels as gl
on ge.id = gl.email_id
group by to_user;

-- Frames in window functions
use hr2;
select employee_id, first_name, last_name, salary, department_id, 
-- sum(salary) over(partition by department_id) as dep_total_salary
sum(salary) over(order by employee_id) as salary_paid
from employees;

select employee_id, first_name, last_name, salary, department_id, 
sum(salary) over(order by employee_id) as salary_paid
from employees;

use classwork;
select *,
-- avg(precipitation) over(partition by city) as avg_rainfall
-- avg(precipitation) over(partition by city rows between 1 preceding and 1 following) as three_days_moving_avg
-- round(avg(precipitation) over(partition by city rows between 1 preceding and current row), 2) as two_days_moving_avg
-- avg(precipitation) over(partition by city rows between unbounded preceding and unbounded following) as default_avg
sum(precipitation) over(partition by city order by date rows between unbounded preceding and current row) as running_total  -- default
from weather;


-- HW
/*
1. Swap the names of each two adjacent students.  Use students database.
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

select * from students;