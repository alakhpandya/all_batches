-- Rank
use hr;

with t1 as
(
	select first_name, last_name, department_id, salary,
	rank() over(partition by department_id order by salary desc) as top_earners
	from employees
	order by department_id
)
select *
from t1
where top_earners <= 3;

select first_name, last_name, department_id, salary,
-- rank() over(partition by department_id order by salary desc) as top_earners,
-- dense_rank() over(partition by department_id order by salary desc) as dense_top_earners,
round(percent_rank() over(partition by department_id order by salary), 2) as pct_top_earners
from employees
order by department_id;


use classwork;
select * from student_score;

select *,
ntile(2) over() as 'group'
from student_score;

select *,
ntile(3) over(partition by dep_name) as grp
from student_score
order by dep_name;

with t1 as
(
	select *,
	ntile(3) over(partition by dep_name order by score desc) as grp
	from student_score
	order by dep_name
)
select student_id, student_name, dep_name, score
from t1
where grp = 1;

use demo;
select * from sales_order;
-- print average sales price for each deal size
select deal_size, round(avg(sales), 2) as avg_sales
from sales_order
group by deal_size;

select order_number, sales, 
round(avg(sales) over(partition by deal_size), 2) as avg_deal_sales,
deal_size
from sales_order
order by order_number;

select order_number, sales, 
round(max(sales) over(partition by deal_size), 2) as max_deal_sales,
round(min(sales) over(partition by deal_size), 2) as min_deal_sales,
round(sum(sales) over(partition by deal_size), 2) as total_deal_sales,
count(sales) over(partition by deal_size) as deal_orders_count,
deal_size
from sales_order
order by order_number;

use classwork;
select *,
lead(score) over() as "next",
lag(score) over() as "prev" 
from student_score
order by dep_name, score desc;

select *,
lead(score) over(partition by dep_name order by score desc) as "next",
lag(score) over(partition by dep_name order by score desc) as "prev" 
from student_score
order by dep_name, score desc;

select *,
-- first_value(score) over(order by score desc) as "first"
first_value(score) over(partition by dep_name order by score desc) as "first",
last_value(score) over(partition by dep_name) as "last",
nth_value(score, 3) over(partition by dep_name) as "3rd"
from student_score
order by dep_name;

select * from students;