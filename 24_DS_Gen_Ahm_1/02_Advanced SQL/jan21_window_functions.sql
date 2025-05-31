use classwork;
select * from google_gmail_emails;
select * from google_gmail_labels;
/*
Find the number of emails received by each user under each built in email label. 
The email labels are: ‘Promotion’, ‘Social’ and ‘Shopping’. Output the user along with the number of promotion, social & shopping emails they got.
*/
select to_user,
sum(case when label="Promotion" then 1 else 0 end) as Promotion,
sum(case when label="Social" then 1 else 0 end) as Social,
sum(case when label="Shopping" then 1 else 0 end) as Shopping
from google_gmail_emails e
join google_gmail_labels l
on e.id = l.email_id
group by to_user;

-- Aggregate Window Functions
select * from student_score;
-- Get me the average marks of each department beside all the 12 rows.
select *,
avg(score) over(partition by dep_name) as dep_avg_marks
from student_score;

-- Get me the running total of marks of the students for each department
select *,
sum(score) over(partition by dep_name order by student_name) as dep_total
from student_score;

select *,
count(student_name) over(partition by dep_name) as dep_total
from student_score;

select *,
min(score) over(partition by dep_name) as dep_min,
max(score) over(partition by dep_name) as dep_max
from student_score;

select *,
ntile(2) over() as "group"
from student_score;

select *,
ntile(5) over() as "group"
from student_score;

select *,
ntile(2) over(partition by dep_name) as "group"
from student_score;

select *,
ntile(2) over(partition by dep_name order by score) as "group"
from student_score;

select * from students;
-- HW: Swap the names of each two adjacent students.

-- Value Window Function
select *,
lead(score) over() as "Lead",
lag(score) over() as "Lag"
from student_score;

select *,
lead(score) over(partition by dep_name) as "Lead",
lag(score) over(partition by dep_name) as "Lag"
from student_score;

select *,
lead(score) over(partition by dep_name order by score desc) as "Lead",
lag(score) over(partition by dep_name order by score desc) as "Lag"
from student_score;

select *,
-- first_value(score) over(partition by dep_name order by score) as "first",
last_value(score) over(partition by dep_name order by score) as "last"
from student_score;