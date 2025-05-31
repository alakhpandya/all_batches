-- use demo;

-- select  productLine,count(*) 
-- from (
-- 	select case when productLine in ('Classic Cars','Vintage Cars') then 'Cars' 
-- 			else productLine end productLine 
-- 	from products 
--     where productLine in ('MotorCycles','Ships','Trains','Classic Cars','Vintage Cars')
-- ) p2
-- group by productLine;

-- CTE: Common Table Expression

/*
with p1 as
(
	select 
    case when productLine in ('Classic Cars','Vintage Cars') then 'Cars' 
	else productLine end productLine 
	from products 
    where productLine in ('MotorCycles','Ships','Trains','Classic Cars','Vintage Cars')
),
p2 as 
(
	select *
    from products
)

select productLine, count(*)
from p1
group by productLine;
*/
use paintings;
-- Window functions
select *,
row_number() OVER()
from artists;