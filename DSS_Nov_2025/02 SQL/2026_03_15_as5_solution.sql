use as5;
-- Q-1:
select d.department_id, d.department_name
from department d
left join employees e on d.department_id = e.department_id
where e.department_id is null;
-- OR
select department_id, department_name
from department
where department_id not in (
	select department_id from employees
);

-- Q-2:
select e.empId, e.name, b.bonus
from employee e
left join bonus b on e.empId = b.empId
where bonus < 1000 or bonus is null;

-- Q-3:
use hr;
select e1.employee_id, e1.first_name, e1.last_name, e1.hire_date, e1.manager_id, 
e2.first_name as manager_first_name, e2.last_name as manager_last_name, e2.hire_date as manager_hire_date
from employees e1
join employees e2 on e1.manager_id=e2.employee_id
where e1.hire_date < e2.hire_date;

-- Q-4:
select distinct session_id
from playback p
left join ads a on p.customer_id = a.customer_id
where timestamp not between start_time and end_time;

-- Q-5:
select * from cinema;

-- Q-6:
select * from employeess
where manager_id is null;