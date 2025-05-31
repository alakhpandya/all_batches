use moviesdb;
/*
Create two tables employee & salary.
Employee has 4 employees with emp_id: 1, 2, 4, 5
Salary has salary of 4 employees with emp_id: 1, 3, 4, 6
Perform full outer join on these two tables
*/
use classwork;
CREATE TABLE EMP(
	EMP_ID INT PRIMARY KEY,
    FNAME varchar(50)
);
INSERT INTO EMP (EMP_ID, FNAME) 
VALUES
(1, 'Tirth'),
(2, 'Harsh'),
(3, 'Rudra'),
(4, 'Yash'),
(5, 'Dev');

CREATE TABLE SAL(
	EMP_ID INT PRIMARY KEY,
    SALARY INT
);

INSERT INTO SAL(EMP_ID, SALARY)
VALUES
(1, 1000),
(3,2000),
(4,3000),
(6,4000);

select * from emp;
select * from sal;

with cte as
(
	select e.emp_id as empl_id, fname, s.emp_id, salary
	from emp e
	left join sal s
	on e.emp_id = s.emp_id
	union
	select e.emp_id as empl_id, fname, s.emp_id, salary
	from emp e
	right join sal s
	on e.emp_id = s.emp_id
)
select empl_id, fname, salary
from cte;

select *
from emp
cross join sal;