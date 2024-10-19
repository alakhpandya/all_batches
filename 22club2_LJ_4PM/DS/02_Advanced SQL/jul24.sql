use as5;
-- select d.department_id, department_name
-- from department d
-- left join employees e
-- on d.department_id = e.department_id
-- where employee_id is null;

-- select e.name, b.bonus
-- from employee e
-- left join bonus b on e.empId = b.empId
-- where b.bonus < 1000 or b.bonus is null
-- order by b.bonus;

-- select * from playback;
-- select * from ads;
-- select distinct session_id from Ads a
-- join Playback p on a.customer_id = p.customer_id
-- where a.timestamp not between p.start_time and p.end_time;

select session_id from playback 
where session_id not in
(
	select session_id
	from Ads a
	join Playback p using(customer_id)
	where a.timestamp between p.start_time and p.end_time
);


with t1 as
(
	select session_id
	from Ads a
	join Playback p using(customer_id)
	where a.timestamp between p.start_time and p.end_time
)

select session_id from playback
where session_id not in (select * from t1);