-- Q-1:
use as3;
select actor_id, director_id 
from actordirector
group by actor_id, director_id
having count(*) >= 3;

-- Q-2:
use hr2;
select e.department_id, department_name, round(avg(salary), 0)
from employees e
join departments d on e.department_id = d.department_id
group by e.department_id, department_name
order by 1;

-- Q-3:
use hr2;
select department_name, count(employee_id) as No_of_Employees, sum(salary) as Total_Salary
from employees e
right join departments d on e.department_id = d.department_id
group by e.department_id, department_name
order by 1;

-- Q-4:
select employee_id, e.department_id, first_name, last_name, job_id, department_name
from employees e
join departments d on e.department_id = d.department_id
where d.department_name = 'Human Resources';

-- Q-5:
use as3;
select sale_id, product_name, year, price 
from sales s
left join product p on s.product_id = p.product_id;

-- Q-6:
use as3;
select * 
from customers c
join orders o on c.customer_id = o.customer_id
where product_name in ("Bread", "Milk");
select * from orders where product_name="Milk";

-- Option-1:
select *
from customers
where 
customer_id in (select customer_id from orders where product_name="Bread")
AND
customer_id in (select customer_id from orders where product_name="Milk")
AND
customer_id NOT in (select customer_id from orders where product_name="Eggs");

-- Option-2:
select c.customer_id, customer_name
from customers c
join orders o on c.customer_id = o.customer_id
group by customer_id, customer_name
having
sum(o.product_name = "Bread") > 0 AND
sum(o.product_name = "Milk") > 0 AND
sum(o.product_name = "Eggs") = 0;

select customer_id, sum(product_name = "Bread")
from orders
group by customer_id;

-- Option-3
select 1 as new_col
from orders o
where o.product_name = "Jam";

select customer_id, customer_name
from customers c
where exists (
	select 1
    from orders o
    where o.customer_id = c.customer_id and o.product_name = "Bread"
) and
exists (
	select 1
    from orders o
    where o.customer_id = c.customer_id and o.product_name = "Milk"
) and
not exists (
	select 1
    from orders o
    where o.customer_id = c.customer_id and o.product_name = "Eggs"
);

-- Q-7:
use hr;
select employee_id, concat(first_name, " ", last_name) as full_name, salary, phone_number, e.department_id, department_name, street_address, city,
country_name, c.region_id, region_name
from employees e
join departments d on e.department_id=d.department_id
join locations l on d.location_id=l.location_id
join countries c on l.country_id = c.country_id
join regions r on c.region_id=r.region_id
where region_name = "Europe";