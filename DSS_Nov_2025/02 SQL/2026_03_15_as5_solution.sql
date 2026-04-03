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
/*
(seat after current seat is free or sear before the current seat is free)
and
seat itself is free
*/
select seat_id-1 from cinema where free=1;		-- seats whose next seat is free
select seat_id+1 from cinema where free=1;		-- seats whose previous seat is free

select *
from cinema
where seat_id in (
	select seat_id from cinema where free=1
) and (
	seat_id in (
		select seat_id-1 from cinema where free=1
    ) or
    seat_id in (
		select seat_id+1 from cinema where free=1
    )
);

-- Q-6:
select * 
from employeess
where manager_id not in (
	select employee_id from employees
) and salary < 15000;


-- Q-7:
use hr;
select employee_id, first_name, last_name, department_name, country_id
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id
where country_id = "US";

-- Q-8:
use as5;
with t as (
	select p1.x as x1, p1.y as y1, p2.x as x2, p2.y as y2 
	from points p1
	cross join points p2
)
select  
-- round(sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)), 2) as shortest,
round(sqrt(pow((x2-x1), 2) + pow((y2-y1), 2)), 2) as shortest
from t
where round(sqrt(pow((x2-x1), 2) + pow((y2-y1), 2)), 2) <> 0
order by 1
limit 1;