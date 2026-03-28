-- Understanding the dataset: farmers_market
-- Q-1: Give me the maximum original_price for each vendor
use farmers_market;
select vendor_id, max(original_price) 
from vendor_inventory
group by vendor_id;

-- Rank the products in each vendor’s inventory based on original_price so that expensive products get smaller rank
select *,
dense_rank() over(partition by vendor_id order by original_price desc) as price_rank
from vendor_inventory;

-- As a farmer, you want to figure out which products were above the average price on each market date. Find them out.
with t as (
	select market_date, 
	avg(original_price) over(partition by market_date) as avg_price,
	product_id, original_price
	from vendor_inventory
)
select *
from t
where original_price > avg_price
order by market_date, original_price desc;

-- FRAMES in Window Functions
use classwork;
-- Try using avg() window function on score partition by dep_name & order by student_name. Are you getting expected answer?
select *,
avg(score) over(partition by dep_name order by student_name rows between unbounded preceding and unbounded following) as dep_avg_score
from student_score;
-- order by dep_name, student_name;

select *,
sum(precipitation) over(partition by city) as total_precipitation, 
sum(precipitation) over(partition by city order by date) as precipitation_running_total,
avg(temperature) over(partition by city) as city_avg_temp,
avg(temperature) over(partition by city order by date) as moving_avg_temp
from weather;

select *,
sum(precipitation) over(partition by city rows between 1 preceding and current row) as exp_1,
avg(precipitation) over(partition by city rows between 1 preceding and 1 following) as 3_days_moving_average
from weather;

select *,
sum(precipitation) over(partition by city rows between current row and 1 following) as exp_2
from weather;

select *,
-- first_value(student_name) over(partition by dep_name order by score desc rows between unbounded preceding and unbounded following) as temp1, -- default frame
-- first_value(student_name) over(partition by dep_name order by score desc rows between 1 preceding and current row) as temp2,
last_value(student_name) over(partition by dep_name order by score desc) as temp3 -- default frame: rows between unbounded preceding and current row
from student_score;

