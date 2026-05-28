use farmers_market;

-- Give me the maximum original_price for each vendor
select vendor_id, max(original_price) as max_org_price
from vendor_inventory
group by vendor_id;

-- Rank the products in each vendor’s inventory based on original_price so that expensive products get smaller rank
select *,
rank() over(partition by vendor_id order by original_price desc) as product_rank
from vendor_inventory;

-- As a farmer, you want to figure out which products were above the average price on each market date. Find them out.

with t as (
	select *,
	avg(original_price) over(partition by market_date) as avg_price
	from vendor_inventory
)
select *
from t
where original_price > avg_price;

-- Frames in Window Functions
use classwork;
select *,
avg(score) over(partition by dep_name) as dep_avg_score,
avg(score) over(partition by dep_name order by student_name rows between unbounded preceding and current row) as dep_avg_score_2 
from student_score;

use hr;
select employee_id, first_name, department_id, salary,
-- sum(salary) over(partition by department_id order by salary rows between 1 preceding and current row) as total_salary
-- sum(salary) over(partition by department_id order by salary rows between 2 preceding and current row) as total_salary
-- sum(salary) over(partition by department_id order by salary rows between unbounded preceding and current row) as total_salary
sum(salary) over(partition by department_id order by salary rows between unbounded preceding and unbounded following) as total_salary
from employees;

use classwork;
select *,
sum(precipitation) over(partition by city order by date) as running_total_precipitation,
avg(temperature) over(partition by city order by date) as moving_average,
avg(precipitation) over(partition by city order by date rows between 1 preceding and 1 following) as "3_days_moving_avg"
from weather;