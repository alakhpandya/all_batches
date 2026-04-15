use as8;

-- Q-1
select u.city, count(*) as total_orders  
from trades t
join users u on t.user_id = u.user_id
where status = "completed"
group by city
order by 2 desc
limit 3;

-- Q-2
select gender, day,
sum(score_points) over(partition by gender order by day) as total
from scores;

-- Q-3:
with t1 as (
	select id as user_id, cast(substr(phone_number, 1, 3) as unsigned) as country_code
	from person p
),
t2 as (
	select t1.user_id, c.name as country
	from t1
	join country c on t1.country_code = c.country_code
),
t3 as (
	select caller_id, callee_id, duration from calls
	union
	select callee_id, caller_id, duration from calls
),
t4 as (
	select caller_id, country, duration 
	from t3
	join t2 on t2.user_id = t3.caller_id
	order by country
)
select country,
avg(duration) over(partition by country) as country_avg,
avg(duration) over() as global_avg
from t4;


with t1 as (
	select c.name as country, cl.duration
	from calls cl
	join person p on cl.caller_id = p.id or cl.callee_id = p.id
	join country c on substring_index(p.phone_number, '-', 1) = c.country_code
)
select country, avg(duration) as country_avg
from t1
group by country
having avg(duration) >
(
    select avg(duration)
    from t1
)
order by country;

-- Q-4:
select *,
dense_rank() over(order by salary) as team_id
from employees
where salary not in (
	select salary from employees
    group by salary having count(salary) = 1
);


-- Q-5:
use hr;
with t as (
	select employee_id, first_name, job_id, salary,
	rank() over(partition by job_id order by salary desc) as salary_rank
	from employees
)
select *
from t
where salary_rank = 5;

-- Q-6: