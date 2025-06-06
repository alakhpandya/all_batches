use demo;

select distinct productLine, count(*) as 'Total'
from (
	select 
	case when productLine in ('Classic Cars', 'Vintage Cars') then 'Cars'
	else productLine end productLine
	from products
) t1
group by productLine;

-- CTE: Common Table Expression
with t1 as
(
	select productName,
	case when productLine in ('Classic Cars', 'Vintage Cars') then 'Cars'
	else productLine end productLine
	from products
),
t2 as
(
	select productLine, count(*) as 'Total'
    from t1
    group by productLine
)

-- select distinct productLine, count(*) as 'Total'
-- from t1
-- group by productLine;
select *
from t2;

use paintings;
with cte as
(
	select *, row_number() over() as RowNumber
    from artists
)

select * from cte
where RowNumber in (
	select max(RowNumber)
    from cte
    group by first_name, last_name
    having count(*) > 1 
);

-- Display the duplicate entries in the artists table

-- Delete the duplicate entries from the artists table
