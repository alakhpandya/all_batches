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

-- Q-6:
select *
from employeess
where salary < 15000 and manager_id not in (
	select employee_id from employeess
);

-- Q-7:
use hr;
select e1.employee_id, e1.first_name, e1.last_name, e1.salary, e1.manager_id, concat(e2.first_name, e2.last_name) as manager_name, d.department_name as manager_dept,
l.country_id
from employees e1
join employees e2 on e1.manager_id = e2.employee_id
join departments d on e2.department_id = d.department_id
join locations l on d.location_id = l.location_id
where l.country_id = "US";

-- Q-8:
with t as (
	select p1.x as x1, p1.y as y1, p2.x as x2, p2.y as y2
	from points p1
	cross join points p2
)
select *, round(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)), 2) as shortest
from t
where round(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)), 2) > 0
order by 5
limit 1;