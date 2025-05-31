use as3;
-- 6. Q6. Products Recommendation
select * from customers;
select * from orders;

select distinct(o.customer_id), c.customer_name
from orders o
join customers c
on o.customer_id = c.customer_id
where o.product_name in ('Bread', 'Milk') and o.customer_id not in (
	select customer_id
    from orders
    where product_name = 'Eggs'
);

use hr;
select employee_id, concat(first_name , ' ' , last_name) full_name, salary, phone_number, department_id, department_name, street_address, city, country_name, region_id, 
region_name 
from employees e 
join departments d 
using(department_id) 
join locations 
using(location_id) 
join countries 
using(country_id) 
join regions 
using(region_id) 
where region_name = "europe" order by salary desc , employee_id asc;