use classwork;
-- drop table Employees; 
Create table If Not Exists Employees (employee_id int, name varchar(30));
Create table If Not Exists Salaries (employee_id int, salary int);
Truncate table Employees; 
insert into Employees (employee_id, name) values ('2', 'Crew'); 
insert into Employees (employee_id, name) values ('4', 'Haven'); 
insert into Employees (employee_id, name) values ('5', 'Kristian'); 
Truncate table Salaries; 
insert into Salaries (employee_id, salary) values ('5', '76071'); 
insert into Salaries (employee_id, salary) values ('1', '22517'); 
insert into Salaries (employee_id, salary) values ('4', '63539');

select * from Employees;
select * from Salaries;

-- Print the employees with missing name or salary

with cte1 as (
	select e.employee_id, e.name, s.salary 
	from Employees e
	left join Salaries s on e.employee_id = s.employee_id
),
cte2 as(
	select s.employee_id, e.name, s.salary
    from Salaries s
    left join Employees e on s.employee_id = e.employee_id
),
cte3 as( 
	select * from cte1
	union
	select * from cte2
)
select employee_id
from cte3
where name is null or salary is null
order by employee_id;