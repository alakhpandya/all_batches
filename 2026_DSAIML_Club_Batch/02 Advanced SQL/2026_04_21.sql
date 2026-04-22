-- Types of joins: inner, left, right, full outer, cross
-- Natural Join
use moviesdb;

-- select movie_id, industry, title, studio, name, imdb_rating, release_year, movies.language_id 
select *
from movies
join languages 
using(language_id);

-- Non-natural join
select movies.*, languages.name
from movies
join languages on movies.language_id = languages.language_id;

-- Print language of each movie in the movies table. Return movie_id, title and language_name columns only.
-- select m.movie_id, m.title, l.name as language_name
select movie_id, title, name as language_name
from movies m
join languages l 
on m.language_id = l.language_id;

-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id
select ma.actor_id, m.title
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
order by ma.actor_id;

-- Print number of movies played by each actor beside his/her name sorted in ascending order of actor_id
select a.name, count(movie_id) as no_of_movies
from actors a
join movie_actor ma on a.actor_id = ma.actor_id
group by a.actor_id
order by a.actor_id;

/*
Print names of all the actors vs. movie_id of all the movies they have played roles in. 
Print your result in alphabetical order of actors’ names. 
Make sure to print names of every actor irrespective of whether they have played role in any movie or not.
*/
select * 
from actors a
left join movie_actor ma on a.actor_id = ma.actor_id;

select *
from movie_actor ma
right join actors a on ma.actor_id = a.actor_id;

/*
Print average imdb_rating of the movies played by only those actors who have played role in at least one movie. 
Return avg_rating column beside name of each actor.
*/
select a.name, round(avg(m.imdb_rating), 1) avg_rating
from movies m
join movie_actor ma on m.movie_id = ma.movie_id
join actors a on ma.actor_id = a.actor_id
group by a.name;

-- Understanding the Sales_order dataset:
-- Print the orders which were placed after august 2003 and their deal size is small
use demo;
select *
from sales_order
where order_date > "2003-08-31" and deal_size = "Small";

-- Print orders which were placed in the last quarter of 2003 and have deal size small
select *
from sales_order
-- where qtr_id = 4 and year_id = 2003 and deal_size = "Small";
-- where order_date between "2003-10-01" and "2003-12-31" and deal_size = "Small";
WHERE YEAR(order_date) = 2003 AND QUARTER(order_date) = 4 AND deal_size = 'Small';

-- Print the first and last city (alphabetically) of customers from each country
select country, min(city) as first_city, max(city) as last_city
from customers
group by country;

-- Find the minimum & maximum price for each product line
select product_line, min(price) as min_price, max(price) as max_price
from products
group by product_line;

/*
Print all the orders made from the country “USA”. Use  sales_order & customers tables from Demo database. 
Return order_number, order_date & deal_size columns. Show the result in descending order of order_date.
*/
select order_number, order_date, deal_size, country
from sales_order so
join customers c on so.customer = c.customer_id
where country = "USA"
order by order_date desc;

-- Get me the customers who are not from USA and their status is "In Process"
-- select customer_id, customer_name, order_number, order_date, country, status
select distinct customer_id, customer_name
from sales_order so
join customers c on so.customer = c.customer_id
where country <> "USA" and status = "In Process";