use as3;
select actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) >= 3;

use hr;
select e.department_id, department_name, avg(salary) as Average_Salary
from employees e
join departments d
on e.department_id = d.department_id
group by department_id, department_name
order by department_id;

use hr;
select employee_id, e.department_id, first_name, last_name, job_id, department_name
from employees e
join departments d
on e.department_id = d.department_id
where department_name = "Human Resources";

use as3;
select product_name, year, price
from sales s
join product p
on s.product_id = p.product_id;

select * from orders;
select * from customers;