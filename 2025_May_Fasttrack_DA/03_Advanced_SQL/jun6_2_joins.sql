-- Joins

-- Print language of each movie along with the other columns of movies table
use moviesdb;
select * from movies;
select * from languages;

select *
from movies
join languages
using(language_id);	-- natural join

-- Types of joins:
/*
1. Inner join
2. Left join
3. Right join
4. Full outer join/Outer join
5. Cross join
6. Self join	-- this is not type of joins
*/

select * 
from movies m
-- join languages as l	-- by default it is inner join
-- inner join languages as l
-- left join languages as l
right join languages as l
on m.language_id = l.language_id;

select *
from movies m
cross join languages as l;

-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id.
select * from movies;
select * from actors;
select * from movie_actor;

select ma.actor_id, m.title
from movie_actor ma
join movies m
on ma.movie_id = m.movie_id
order by ma.actor_id;

-- Print number of movies played by each actor_id sorted in ascending order of actor_id.
select * from movie_actor;
select actor_id, count(movie_id)
from movie_actor
group by actor_id
order by actor_id;

select a.actor_id, count(movie_id)
from movie_actor ma
right join actors a
on ma.actor_id = a.actor_id
group by a.actor_id
order by 2;

/*
Print names of all the actors vs. all the movies they have played roles in. Print your result in alphabetical order of actors’ names. 
Make sure to print names of every actor irrespective of whether they have played role in any movie or not.
*/
select a.name, m.title
from actors a
left join movie_actor ma
on a.actor_id = ma.actor_id
left join movies m
on m.movie_id = ma.movie_id
order by a.name;

/*
Print average imdb_rating of the movies played by only those actors who have played role in at least one movie. Return avg_rating column beside name of each actor.
*/
select a.name, round(avg(m.imdb_rating), 1) as avg_rating
from movies m
join movie_actor ma
on m.movie_id = ma.movie_id
join actors a
on ma.actor_id = a.actor_id
group by a.name
order by 2 desc;

-- Download & understand "demo" database
-- Print the orders which were placed after august 2003 and their deal size is small
use demo;
select * 
from sales_order
where deal_size = "small" and order_date > "2003-08-31";

-- Print orders which were placed in the last quarter of 2003 and have deal size small
select *
from sales_order
-- where qtr_id = 4 and year_id = 2003 and deal_size = "Small";
-- where month_id between 10 and 12 and year_id = 2003 and deal_size = "Small";
where order_date between "2003-10-01" and "2003-12-31" and deal_size = "Small";

-- Print the first and last city (alphabetically) of customers from each country
select country, min(city) as first_city, max(city) as last_city 
from customers
group by country;

-- Find the minimum & maximum price for each product line
select PRODUCT_LINE, MIN(PRICE) AS MIN_PRICE, MAX(PRICE) AS MAX_PRICE 
from products
GROUP BY PRODUCT_LINE;

/*
Print all the orders made from the country “USA”. Use  sales_order & customers tables from Demo database. 
Return order_number, order_date & deal_size columns. Show the result in descending order of order_date.
*/
select so.order_number, so.order_date, so.deal_size
from sales_order so
left join customers c
on so.customer = c.customer_id
where c.country = "USA"
order by 2 desc;

-- Homework
/*
1. Get me the customers who are not from USA and their status is "In Process"
*/
use demo;
select c.customer_id, c.customer_name, c.country, so.status
from customers c
left join sales_order so
on c.customer_id = so.customer
where c.country != "USA" and so.status = "In Process";

/*
2. Print the names of the actors who did not play role in any movie (Use moviesdb database)
*/
use moviesdb;
select a.actor_id, a.name
from actors a
left join movie_actor ma
on a.actor_id = ma.actor_id
where ma.actor_id is null;

/*
3. Print the names of the departments in which no employee is working (Use hr2 database)
*/
use hr2;
select d.department_id, d.department_name
from employees e
right join departments d
on e.department_id = d.department_id
where e.department_id is null;