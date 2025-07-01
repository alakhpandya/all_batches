/*
Write a query to find the customer_id and customer_name of customers who bought products "Bread" and "Milk" but did not buy the product "Eggs".
• Return the output ordered by customer_name in ascending order
*/
/*
select *
from customers c 
join orders o
on c.customer_id = o.customer_id;

select customer_name, count(*)
from customers c 
join orders o
on c.customer_id = o.customer_id
group  by c.customer_name
having
	sum(product_name='Bread') > 0 and
	sum(product_name = 'Milk') > 0 and
    sum(product_name = 'Eggs') = 0
order by customer_name ;

with t as (
	select
		c.customer_id,c.customer_name,o.product_name
	from
		customers c
	join
		orders o
	on
		c.customer_id=o.customer_id
)
select customer_id,customer_name from t 
where customer_id not in (
	select customer_id from t where product_name = "Eggs"
)
group by 
	customer_id,customer_name
having
	sum(product_name='Bread') > 0 and
	sum(product_name = 'Milk') > 0
order by
	customer_name asc;
*/

-- AS-5: Q-1
/*
Write a query to display the details of all those departments that don't have any working employees.
•	Return the columns 'department_id', and 'department_name'.
*/
/*
select d.department_id,  d.department_name
from employees e
right join department d
on d.department_id = e.department_id
where e.employee_id is null;
*/
/*
Display the details of the employees who joined the company before their managers joined the company.
•	Return the columns 'employee_id', 'first_name', and 'last_name'.
•	Return the result ordered by employee_id in ascending order.
*/
/*
use hr;
select e1.employee_id, e1.first_name, e1.hire_date, e2.hire_date as manager_hire_date
from employees e1
join employees e2
on e1.manager_id = e2.employee_id
where e1.hire_date < e2.hire_date;
*/

-- AS-5, Q-4
/*
Write a query to report all the sessions that did not get shown any ads.
Return the resultant table ordered by session_id in ascending order.
*/
/*
select p.session_id, p.start_time, p.end_time, p.customer_id, a.timestamp
from playback p
join ads a
on p.customer_id = a.customer_id;
*/

-- AS-5, Q-5
/*
Write a query to report all the consecutive available seats in the cinema.
•	Return the result table ordered by seat_id in ascending order.
*/
/*
select * from cinema;
with result as (
	SELECT c1.seat_id --  as seat_id_1, c1.free as free1, c2.seat_id as seat_id_2, c2.free as free2
	FROM cinema c1
    JOIN cinema c2 ON c1.seat_id = c2.seat_id + 1
    WHERE c1.free = 1 AND c2.free = 1 
    UNION 
    SELECT c2.seat_id
    FROM cinema c1
    JOIN cinema c2 ON c1.seat_id = c2.seat_id + 1
    WHERE c1.free = 1 AND c2.free = 1
	
)
select * from result
ORDER BY seat_id;

select * from cinema;

-- seats which themselves are free
select seat_id
from cinema c1
where free = 1 
and (
seat_id in (
-- seats whose next seat is free
	select seat_id-1
	from cinema c1
	where free = 1
	order by seat_id
	)
	or
-- seats whose previous seat is free
seat_id in (
	select seat_id+1
	from cinema c1
	where free = 1
	order by seat_id
	)
);
*/

-- AS-5, Q-8
/*
Write a query to find the shortest distance between any two points from the points table. Round the distance to two decimal points
Note:
•	The distance between two points p1(x1, y1) and p2(x2, y2) is calculated using euclidean distance formula √((x2 - x1)2 + (y2 - y1)2).
•	Save the new column as 'shortest'.
*/
select * from points;

with t as (
	select round(sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2)), 2) as d 
	from points p1
	cross join points p2
	where round(sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2)), 2) > 0
)
select min(d)
from t;
