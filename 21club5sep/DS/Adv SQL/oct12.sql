-- create database classwork;
use classwork;

DROP TABLE IF EXISTS student_score;

CREATE TABLE student_score (
  student_id SERIAL PRIMARY KEY,
  student_name VARCHAR(30),
  dep_name VARCHAR(40),
  score INT
);

INSERT INTO student_score VALUES (11, 'Nitin', 'Computer Science', 80);
INSERT INTO student_score VALUES (7, 'Taiwo', 'Microbiology', 76);
INSERT INTO student_score VALUES (9, 'Nikki', 'Biochemistry', 80);
INSERT INTO student_score VALUES (8, 'Joel', 'Computer Science', 90);
INSERT INTO student_score VALUES (10, 'Mauli', 'Industrial Chemistry', 78);
INSERT INTO student_score VALUES (5, 'Murlidhar', 'Biochemistry', 85);
INSERT INTO student_score VALUES (2, 'Yuyutsu', 'Biochemistry', 70);
INSERT INTO student_score VALUES (3, 'Heena', 'Microbiology', 80);
INSERT INTO student_score VALUES (1, 'Tomiwa', 'Microbiology', 65);
INSERT INTO student_score VALUES (4, 'Gbadebo', 'Computer Science', 80);
INSERT INTO student_score VALUES (12, 'Tolu', 'Computer Science', 67);

select * from student_score;

-- Get me the maximum score from each department
-- Print the average score of each department
-- Print student_name, their department name, score, average score of that department and difference of each student from average score.

with cte as (
	select student_name, dep_name, score, 
	avg(score) over(partition by dep_name order by dep_name) as avg_score
	from student_score
)
select *,
avg_score - score as difference
from cte;

select * from student_score;
select *,
-- LAG(score) over(partition by dep_name order by score) as Prev_score
-- LAG(score) over() as Prev_score
-- LAG(score) over(order by score desc) as Prev_score

LEAD(score) over(partition by dep_name order by score) as next_score
from student_score;

-- Print the difference of marks of each student from the marks of the student who scored more than them from the same department

Create table If Not Exists Products (product_id int, new_price int, change_date date);
Truncate table Products;
insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15');
insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16');
insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17');
insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18');

-- Print the average number of days it takes to change price of every product