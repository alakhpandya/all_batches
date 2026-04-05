use as6;
-- Q-1:
with t as (
	select s.sales_id, s.name as sales_person_name, o.order_id, o.com_id, c.name as company_name
	from salesperson s
	left join orders o on s.sales_id = o.sales_id
	left join company c on o.com_id = c.com_id
)
select sales_person_name
from t
where sales_id not in (
	select distinct sales_id from t where company_name = "Red"
)
order by sales_person_name;

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

-- Q-3:
use hr2;
select e1.employee_id, concat(e1.first_name, " ", e2.last_name) as full_name, e1.salary, e2.first_name as manager_name
from employees e1
join employees e2 on e1.manager_id = e2.employee_id
where e2.first_name = "Adam";

-- Q-4:
select *
from employees
where job_id = (
	select job_id from employees where employee_id = 104
);

-- Q-5:
-- select viewer_id, view_date, count(distinct(article_id))
select viewer_id
from views
group by viewer_id, view_date
having count(distinct(article_id)) > 1
order by 1;

-- Q-6:
select l1.account_id, l1.ip_address, l1.login, l1.logout, l2.ip_address, l2.login, l2.logout
from loginfo l1
join loginfo l2 on l1.account_id=l2.account_id and l1.ip_address <> l2.ip_address
where l2.logout between l1.login and l1.logout;

-- Q-7:
use hr2;
select *
from employees 
where employee_id not in (select employee_id from job_history);