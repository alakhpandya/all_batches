use as5;
-- Q-1:
select * from employees;
select * 
from department d
left join employees e on d.department_id = e.department_id
where e.employee_id is null;

-- Q-2:
select *
from employee e
left join bonus b on e.empId = b.empId
where bonus < 1000 or bonus is null
order by bonus;

-- Q-3:
use hr;
select e1.employee_id, e1.first_name, e1.last_name, e1.hire_date as employee_hire_date, e1.manager_id, e2.hire_date as manager_hire_date
from employees e1
left join employees e2 on e1.manager_id=e2.employee_id
where e1.hire_date < e2.hire_date;

-- solution using connected subqueries
select *
from employees e1
where e1.hire_date < (
	select hire_date
    from employees e2
    where e1.manager_id = e2.employee_id
);

-- Q-4:
use as5;
-- select session_id, start_time, end_time, a.ad_id, a.timestamp
select distinct session_id
from Playback p
join Ads a on p.customer_id = a.customer_id
where timestamp not between start_time and end_time
order by session_id;

-- Q-5:
select *
from cinema
where free = 1 and 
(
	seat_id in (
			select seat_id+1 from cinema where free=1
	) or seat_id in (
			select seat_id-1 from cinema where free=1
	)
);