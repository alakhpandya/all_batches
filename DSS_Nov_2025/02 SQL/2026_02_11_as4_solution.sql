-- Q-1

select distinct title, Kids_content, program_date
from content c
join tvprogram t
on c.content_id = t.content_id
where Kids_content = "Y" and 
program_date between "2020-06-01" and "2020-06-30"
order by title;

-- Q-2
select employee_id, 
-- if(employee_id % 2 != 0 and substr(name, 1, 1) != "M", salary, 0) as bonus
case 
	when employee_id % 2 != 0 and substr(name, 1, 1) != "M" then salary
    else 0
end as bonus
from employees
order by employee_id;

-- Q-3:
select *,
case
	when x + y > z and y + z > x and x + z > y then "Yes"
    else "No"
end as triangle
from triangle
order by x, y, z;

-- Q-4:
use hr2;
select e.employee_id, d.department_name, jh.job_id, j.job_title, j.min_salary
from employees e
join departments d on e.department_id = d.department_id
join job_history jh on e.employee_id=jh.employee_id
join jobs j on jh.job_id = j.job_id
where j.job_title like "%Sales%" and j.min_salary >= 6000
order by employee_id, min_salary;

-- Q-5:
use hr2;
select employee_id, salary,
case
	when salary > 20000 then "Class A"
    when salary between 10000 and 20000 then "Class B"
    else "Class C"
end as salary_bin
from employees
order by employee_id;

-- Q-6:
use hr2;
select employee_id, first_name, last_name, salary,
case
	when job_id in ("FI_ACCOUNT", "AC_ACCOUNT") then 1
    else 0
end as Accountant
from employees
order by employee_id;