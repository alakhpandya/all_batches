use demo;

-- select * from products;

-- select productLine, count(*)
-- from (
-- 	select case when productLine in ("Classic Cars", "Vintage Cars") then "Cars" else productLine end as productLine
-- 	from products
-- 	where productLine in ("Classic Cars", "Vintage Cars",  "Motorcycles", "Trains", "Ships")
-- ) as a
-- group by productLine;

-- CTE: Common Table Expression

with cte as
(
	select case when productLine in ("Classic Cars", "Vintage Cars") then "Cars" else productLine end as productLine
	from products
	where productLine in ("Classic Cars", "Vintage Cars",  "Motorcycles", "Trains", "Ships")
)

select productLine, count(*)
from cte
group by productLine;