-- Full Outer Join
use classwork;

select * from employees;
select * from department;
alter table department rename column emp_id to employee_id;

/*
SELECT E.EMPLOYEE_ID, D.EMPLOYEE_ID
FROM EMPLOYEES E 
LEFT JOIN DEPARTMENT D 
ON E.EMPLOYEE_ID = D.EMPLOYEE_ID
UNION 
SELECT E.EMPLOYEE_ID, D.EMPLOYEE_ID
FROM EMPLOYEES E 
RIGHT JOIN DEPARTMENT D 
ON E.EMPLOYEE_ID = D.EMPLOYEE_ID;
*/

-- Find the popularity percentage for each user on Meta/Facebook. 
-- The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, 
-- then converted into a percentage by multiplying by 100. Output each user along with their popularity percentage. Order records in ascending order by user id.
select * from facebook_friends;

WITH all_users AS (
    SELECT user1 AS usr FROM facebook_friends
    UNION ALL
    SELECT user2 AS usr FROM facebook_friends
) , 
t2 AS(
SELECT user1 AS usr FROM facebook_friends
UNION
SELECT user2 AS usr FROM facebook_friends
)
SELECT usr, COUNT(usr) as friends,(count(usr)/(SELECT COUNT(*) from t2))*100 AS popularity_pct
FROM all_users 
GROUP BY usr ORDER BY USR;

-- HW: Identify how many cars, motorcycles, trains and ships are available in the inventory. Treat all types of cars just as “Cars”. 
-- DO NOT USE ‘LIKE’ IN THIS EXAMPLE. (Use ‘demo’ database)

use demo;
select * from products;

select distinct product_line
from products;

select
case
	when product_line in ("Classic Cars", "Vintage Cars") then "cars"
    else product_line
end as new_product_line,
count(*) as cnt
from products
group by new_product_line;

-- Do the same example using union/union all
select product_line, count(*) as cnt
from products
where product_line not in ("Classic Cars", "Vintage Cars")
group by product_line
union
select 'cars' as product_line, count(*) as cnt
from products
where product_line in ("Classic Cars", "Vintage Cars");