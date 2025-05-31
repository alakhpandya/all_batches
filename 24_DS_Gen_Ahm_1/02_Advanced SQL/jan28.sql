use classwork;
select * from students;

select id, student_name,
coalesce(if(id % 2 = 1, lead(student_name) over(), lag(student_name) over()), student_name) as new_name
from students;

SELECT social_network, date, new_subscribers,
FIRST_VALUE(new_subscribers) OVER(PARTITION BY social_network ORDER BY date) AS first_day,
LAST_VALUE(new_subscribers) OVER(PARTITION BY social_network ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_day
FROM subscribers ORDER BY social_network, date;
