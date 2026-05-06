use as2;
-- Q1
select * 
from cinema
where id % 2 <> 0 and description not like "%boring%"
order by rating desc;

-- Q3
select *,
round(((salary * 20)/100) + salary, 0) as New_salary
from employees
order by emp_id;