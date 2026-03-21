-- Q-1:
use as3;
select actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) >= 3;

-- Q-2:
use hr;
select e.department_id, department_name, avg(salary) as Average_Salary
from employees e
join departments d
on e.department_id = d.department_id
group by department_id, department_name
order by department_id;

-- Q-4:
use hr;
select employee_id, e.department_id, first_name, last_name, job_id, department_name
from employees e
join departments d
on e.department_id = d.department_id
where department_name = "Human Resources";

-- Q-5
use as3;
select product_name, year, price
from sales s
join product p
on s.product_id = p.product_id;

select * from orders;
select * from customers;

-- Q-6:
/*
select customer_id,
sum(case when product_name = "Bread" then 1 else 0 end) as bread_order,
sum(case when product_name = "Milk" then 1 else 0 end) as milk_order,
sum(case when product_name = "Eggs" then 1 else 0 end) as eggs_order
from orders
group by customer_id
having bread_order > 0 and milk_order > 0 and eggs_order = 0;
*/
with cte as (
	select customer_id
	from orders
	group by customer_id
	having
	sum(case when product_name = "Bread" then 1 else 0 end) > 0 and
	sum(case when product_name = "Milk" then 1 else 0 end) > 0 and
	sum(case when product_name = "Eggs" then 1 else 0 end) = 0
)
select cte.customer_id, c.customer_name
from cte
join customers c on cte.customer_id = c.customer_id;
