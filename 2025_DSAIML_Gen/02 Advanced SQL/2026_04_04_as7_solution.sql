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
