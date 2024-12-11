use moviesdb;

select * from movies;
select * from languages;

select * 
from movies m
join languages l
on m.language_id = l.language_id;

select * 
from movies
join languages
using(language_id);

-- Print actor_id vs. movies names that actor has played a role in.
select * from movie_actor;

select actor_id, ma.movie_id, title
from movie_actor ma
inner join movies m
on ma.movie_id = m.movie_id
order by ma.actor_id;

use demo;
select * from sales_order;
select * from customers;
select * from orders;
select * from employees;
select * from products;

select order_number, order_date, deal_size
from sales_order so
left join customers c
on so.customer = c.customer_id
where country = "USA"
order by order_date desc;