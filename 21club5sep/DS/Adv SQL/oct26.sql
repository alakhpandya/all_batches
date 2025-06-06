/*
use moviesdb;

select * from movies;
-- Get me the best movie (rating wise) of each studio. Print all the movies if they all are having best ratings for that particular studio.

use classwork;
select * from student_score;

select dep_name, student_name, score;
-- Indexing & Partitioning: range between unbounded preceeding 

use classwork;

create table students(
		id int primary key,
		student_name varchar(50) not null
);
insert into students values
(1, 'James'),
(2, 'Michael'),
(3, 'George'),
(4, 'Stewart'),
(5, 'Robin');
select * from students;

select id,
case 
	when id % 2 != 0 then lead(student_name, 1, student_name) over()
    when id % 2 = 0 then lag(student_name, 1, 'N/A') over()
end new_names
from students;

create database SQL50;
use SQL50;

Create table If Not Exists Logs (log_id int);
Truncate table Logs;
insert into Logs (log_id) values ('1');
insert into Logs (log_id) values ('2');
insert into Logs (log_id) values ('3');
insert into Logs (log_id) values ('7');
insert into Logs (log_id) values ('8');
insert into Logs (log_id) values ('10');
*/
use SQL50;

select * from logs;

with cte as (
	SELECT *,
	ROW_NUMBER() OVER(ORDER BY log_id) as new_num
	FROM Logs
),

cte2 as (
	select *, log_id - new_num as windows
	from cte
)

select *
from cte2;
-- group by windows
-- order by count(*) desc;
-- limit 2;
/*
select min(log_id) start, max(log_id) end
from cte2
group by windows;

select min(log_id) as start, max(log_id) as end
from cte
group by log_id - new_num;
*/