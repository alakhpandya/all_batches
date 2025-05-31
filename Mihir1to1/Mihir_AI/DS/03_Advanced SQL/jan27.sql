/*
use moviesdb;

select * from financials;
select * from movies;
*/
-- Types of join
/*
1. inner join: Common data in both the tables will be returned
2. left join: All the data of left table is returned
3. right join: All the data of right table is returned
4. full outer join(*): All the data of both the tables is returned
*/
/*
select m.movie_id, m.title, m.industry, m.imdb_rating, m.studio, m.release_year, f.budget, f.revenue, f.unit, f.currency
from movies m
join financials f	-- inner join
on m.movie_id = f.movie_id;
*/
use as3;
/*
Create table If Not Exists customers (customer_id int, customer_name varchar(255));
Truncate table customers;
insert into customers (customer_id, customer_name) values ('1', 'Andrew');
insert into customers (customer_id, customer_name) values ('2', 'Erin');
insert into customers (customer_id, customer_name) values ('3', 'Stanley');
Create table If Not Exists orders (order_id int, customer_id int, product_name 
varchar(255));
Truncate table orders;
insert into orders (order_id, customer_id, product_name) values ('10', '1', 'Bread');
insert into orders (order_id, customer_id, product_name) values ('20', '1', 'Milk');
insert into orders (order_id, customer_id, product_name) values ('30', '1', 'Butter');
insert into orders (order_id, customer_id, product_name) values ('40', '1', 'Eggs');
insert into orders (order_id, customer_id, product_name) values ('50', '2', 'Bread');
insert into orders (order_id, customer_id, product_name) values ('60', '2', 'Milk');
insert into orders (order_id, customer_id, product_name) values ('70', '3', 'Butter');
*/

select * from customers;
select * from orders;

select c.customer_id, c.customer_name
from customers c
join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name
having sum(o.product_name = "Bread") >= 1 and sum(o.product_name = "Milk") >= 1 and sum(o.product_name = "Eggs") = 0;

use demo;
