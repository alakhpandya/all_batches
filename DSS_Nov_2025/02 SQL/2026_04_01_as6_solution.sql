use as6;
-- Q-1:
with t as (
	select s.sales_id, s.name, o.order_id, o.com_id, c.name as company_name
	from salesperson s
	left join orders o on s.sales_id = o.sales_id
	left join company c on o.com_id = c.com_id
)
select * 
from t
where sales_id not in (
	select sales_id from t where company_name="RED"
)
order by 2;

-- Q-2:
with t as (
	select s.buyer_id, s.product_id, p.product_name
	from sales s
    join product p on s.product_id = p.product_id
)
select *
from t
where buyer_id in (
	select buyer_id from t where product_name = "S8" 
) and buyer_id not in (
	select buyer_id from t where product_name = "iPhone" 
);


-- This will not work:
with t as (
select s.buyer_id, s.product_id, p.product_name
from Sales s 
join Product p
on s.product_id = p.product_id
)
select *
from t
where product_name = "S8" and  product_name <> "iphone"
order by buyer_id asc;

-- Q-3:
use hr2;
select employee_id, concat(first_name, " ", last_name) as employee_name, manager_id, salary
from employees
where manager_id = (select employee_id from employees where first_name = "Adam");