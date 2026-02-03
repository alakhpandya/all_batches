-- Q-1
use as2;
select * 
from cinema
where id % 2 != 0 and description != "boring"
order by rating desc;

-- Q-2
select emp_id, name, salary,
round(salary + (salary * 20)/100, 0) as New_salary
from employees
order by emp_id asc;