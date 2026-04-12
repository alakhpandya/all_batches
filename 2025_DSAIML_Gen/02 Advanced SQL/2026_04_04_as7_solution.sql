use as7;
-- Q-1:
with t1 as (
	select *,
	row_number() over(order by first_col) as row_num
	from data
), t2 as (
	select *,
	row_number() over(order by second_col desc) as row_num
	from data
)
select t1.first_col, t2.second_col
from t1
join t2 on t1.row_num = t2.row_num;

-- Q-3:
/*
select g1.user_id, g1.gender
from genders g1
order by (
	select count(*)
    from genders g2
    where g1.gender = g2.gender and
    g2.user_id <= g1.user_id
), 
(
	case
		when g1.gender = "female" then 1
        when g1.gender = "other" then 2
        when g1.gender = "male" then 3
	end
);
*/
with t as (
	select user_id, gender,
    row_number() over(partition by gender order by user_id) as row_num
    from genders
)
select *
from t
order by row_num, 
case
	when gender = "female" then 1
	when gender = "other" then 2
	when gender = "male" then 3
end;

-- Q-4:
with t1 as (
	select c.customer_id, c.name, o.product_id, p.product_name, count(o.product_id) over(partition by c.customer_id, product_name) as freq
	from customers c
	join orders o on c.customer_id = o.customer_id
	join products p on o.product_id = p.product_id
), t2 as (
	select *, rank() over(partition by name order by freq desc) as ranking from t1
)
select distinct customer_id, name, product_id, product_name, freq
from t2
where ranking = 1
order by 1, 3;

-- Q-5:
with t1 as (
	select e.employee_id
	from employees e
	left join salaries s on e.employee_id = s.employee_id
    where s.employee_id is null
), t2 as (
	select s.employee_id 
	from employees e
	right join salaries s on e.employee_id = s.employee_id
    where e.employee_id is null
)
select * from t1
union
select * from t2
order by 1;

-- Q-6:
select product_id, "store1" as store, store1 as price from product where store1 is not null
union
select product_id, "store2" as store, store2 as price from product where store2 is not null
union
select product_id, "store3" as store, store3 as price from product where store3 is not null;

-- Q-7:
use hr;
select e.employee_id, concat(e.first_name, " ", e.last_name) as full_name, e.salary,
d.department_id, d.department_name
from employees e
join departments d on e.department_id = d.department_id
where department_name in ("Administration", "Marketing", "Human Resources");