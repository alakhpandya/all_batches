use as3;
-- Q-6
select * from customers;
select * from orders;

select c.customer_id, customer_name from customers c
join orders o on c.customer_id = o.customer_id
where o.product_name in ("Bread", "Milk")
and c.customer_id not in (
	select distinct(customer_id)
	from orders 
	where product_name = "Eggs"
)
group by c.customer_id, customer_name
having count(distinct(product_name)) > 1;
/*
select distinct(customer_id)
from orders 
where product_name = "Eggs";
*/