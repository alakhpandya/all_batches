use as7;
/*
create table if not Exists data (first_col int, second_col int); 
Truncate table data; insert into data (first_col, second_col) values (4, 2); 
insert into data (first_col, second_col) values (2, 3); 
insert into data (first_col, second_col) values (3, 1); 
insert into data (first_col, second_col) values (1, 4);
*/

select * from data;
with t1 as (
	select *,
    row_number() over() as row_num
    from data
    order by first_col
),
t2 as (
	select *,
    row_number() over() as row_num
    from data
    order by second_col desc
)
select t1.first_col, t2.second_col
from t1
join t2 on t1.row_num = t2.row_num;

use hr;
select * from employees;

-- Get me the top 2 earners from each department_id
with t1 as (
	select department_id, first_name, last_name, salary,
	row_number() over(partition by department_id order by salary desc) row_num
	from employees
)
select department_name, first_name, last_name, salary
from t1
join departments d
on t1.department_id = d.department_id
where row_num <= 3
order by department_name;
-- limit 2;
-- order by department_id desc;

with t1 as (
	select department_id, first_name, last_name, salary,
	rank() over(partition by department_id order by salary desc) ranking
	from employees
)
select department_name, first_name, last_name, salary
from t1
join departments d
on t1.department_id = d.department_id
where ranking <= 3
order by department_name;

use as7;
/*
create table if not Exists genders (user_id int, gender varchar(20)); 
Truncate table genders; 
insert into genders (user_id, gender) values (1, "male"); 
insert into genders (user_id, gender) values (2, "other"); 
insert into genders (user_id, gender) values (3, "other"); 
insert into genders (user_id, gender) values (4, "male"); 
insert into genders (user_id, gender) values (5, "female"); 
insert into genders (user_id, gender) values (6, "male"); 
insert into genders (user_id, gender) values (7, "female");
*/

select *,
rank() over(partition by gender order by user_id) as ranking
from genders
order by ranking;