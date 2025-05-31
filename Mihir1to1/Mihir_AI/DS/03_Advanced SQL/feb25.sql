-- use as5;
-- Create table If Not Exists points (x int, y int); 
-- Truncate table points; 
-- insert into points (x, y) values (-1, -1); 
-- insert into points (x, y) values (0, 0); 
-- insert into points (x, y) values (-1, -2);

-- √((x2 - x1)2 + (y2 - y1)2
select *, round(sqrt(pow(p2.x-p1.x, 2) + pow(p2.y - p1.y, 2)), 2) as d
from points p1
join points p2
where not ( p1.x = p2.x and p1.y = p2.y);

use as6;

select name
from salesperson
where sales_id not in (
	select s.sales_id
	from salesperson s
	left join orders o on s.sales_id = o.sales_id
	left join company c on o.com_id = c.com_id
	where c.name = "RED"
);