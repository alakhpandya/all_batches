-- "value" Window functions - lead, lag, fist_value, last_value, nth_value

use classwork;
select * from student_score;

select *,
lead(score) over() as "next",
lag(score) over() as "previous"
from student_score;

select *,
lead(score) over(partition by dep_name) as "next",
lag(score) over(partition by dep_name) as "previous"
from student_score;

select *,
lead(score) over(partition by dep_name order by student_name) as "next",
lag(score) over(partition by dep_name order by student_name) as "previous"
from student_score;

use hr;
use classwork;
select * from google_gmail_emails;
select * from google_gmail_labels;

/*
Find the number of emails received by each user under each built in email label. 
The email labels are: ‘Promotion’, ‘Social’ and ‘Shopping’. Output the user along with the number of promotion, social & shopping emails they got. 
*/

