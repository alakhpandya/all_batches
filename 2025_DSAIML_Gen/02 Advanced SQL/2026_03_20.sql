-- From the "products" table of "Demo" database, identify how many cars, motorcycles, trains and ships are available in the inventory.Treat all types of cars just as “Cars”
use demo;
with t as (
	select 
	case when product_line like '%cars%' then 'Car'
	else product_line 
    end as new_product_line
	from products
)
select vechile, count(vechile) 
from t
group by vechile;

/*
Display all the available paintings and their artists. 
If a painting was sold then mark them as "Sold" and if more than 1 painting of an artist are sold then display a "**" beside their name.
*/
use paintings;
select p.id as painting_id, p.name as painting_name, 
case
	when p.artist_id in (
		select artist_id
		from sales
		group by artist_id
		having count(*) > 1
	) then concat(a.first_name, " ", a.last_name, "**")
	else concat(a.first_name, " ", a.last_name) 
	end as artist_name, 
case
	when s.id is null then "Available"
	else "Sold"
end as status
from paintings p
join artists a on a.id = p.artist_id
left join sales s on p.id = s.painting_id;

-- Give me the artist names appearing more than once in the artists table
select first_name, last_name
from artists
group by first_name, last_name
having count(*) > 1;

-- From hr dataset, get me the top 2 earners from each department

/*
Print movie_id, title, industry, imdb_rating, studio & average rating of that studio from the movies table of moviesdb database. 
Print the result sorted in ascending order of movie_id.
*/
use moviesdb;
with t as (
	select studio, round(avg(imdb_rating), 1) as studio_avg
	from movies
	group by studio
)
select movie_id, title, industry, imdb_rating, m.studio, studio_avg
from movies m
join t on t.studio = m.studio;

-- Window Functions
select movie_id, title, industry, imdb_rating, studio,
min(imdb_rating) over() as min_rating,
max(imdb_rating) over() as max_rating,
avg(imdb_rating) over() as avg_rating,
count(imdb_rating) over() as no_of_rating,
sum(imdb_rating) over() as total_of_ratings
from movies;

select movie_id, title, industry, imdb_rating, studio,
avg(imdb_rating) over(partition by studio) as studio_avg
from movies;

-- Print the total salary paid to each department along with all the columns of employees table in hr database
use hr;
select *,
sum(salary) over(partition by department_id) as dep_total_salary
from employees
order by employee_id;