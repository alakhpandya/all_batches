-- create database demo;

use demo;
-- SELECT COUNT(*) FROM PRODUCTS WHERE PRODUCT_LINE LIKE "%Cars%" or product_line like "%trains% or product_line like "%motorcycles%";
-- select * from products; 

-- select productLine, count(*)
-- from products
-- group by productLine;

-- SELECT 
--     CASE 
--         WHEN productLine IN ('Vintage Cars', 'Classic Cars') THEN 'Car'
--         ELSE productLine
--     END AS product_category,
--     COUNT(*) AS product_count
-- FROM products
-- GROUP BY product_category;

select productLine, count(*)
from (
	select CASE 
			 WHEN productLine IN ('Vintage Cars', 'Classic Cars') THEN 'Car'
			 ELSE productLine
		 END AS productLine
	from products
	where productLine in ('Vintage Cars', 'Classic Cars', 'Motorcycles', 'Trains', 'Ships')
) a
group by productLine;