/*
Identify how many cars, motorcycles, trains and ships are available in the inventory. 
Treat all types of cars just as “Cars”. DO NOT USE ‘LIKE’ IN THIS EXAMPLE. (Use ‘demo’ database)
*/
use demo;
/*
select
	case
		when product_line in ("classic cars", "vintage cars") then "cars"
        else product_line
	end as new_product_line, count(*)
from products
where product_line in ("classic cars", "vintage cars", "motorcycles", "trains", "ships")
group by new_product_line;
*/
-- OR

select
	case
		when product_line in (select product_line from products where substr(product_line, -4) = "cars") then "cars"
        else product_line
	end as new_product_line, count(*)
from products
where product_line in ("motorcycles", "trains", "ships") or product_line in (select product_line from products where substr(product_line, -4) = "cars")
group by new_product_line;

/*
Display all the paintings and their artists. 
If a painting was sold then mark them as "Sold" and if more than 1 painting of an artist are sold then display a "**" beside their name. 
Use "Painting_Sales_Dataset" database.
*/
use paintings;
with t1 as (
	select p.id as painting_id, p.name as painting_name, p.artist_id, concat(first_name, " ", last_name) as artist_name
	from paintings p
	join artists a on p.artist_id=a.id
),
t2 as (
	select artist_id, count(*) as paintings_sold
    from sales
    group by artist_id
)
select t1.painting_id, t1.painting_name, t1.artist_id,
if(t2.paintings_sold >= 2, concat(artist_name, " **"), artist_name) as artist_name, 
-- coalesce(t2.paintings_sold, 0) as paintings_sold,
case
	when t1.painting_id in (select painting_id from sales) then "Sold"
    else "Available"
end as status
from t1
left join t2 on t1.artist_id=t2.artist_id;

-- Give me the artist names appearing more than once in the artists table
select first_name, last_name
from artists
group by first_name, last_name
having count(*) > 1;

/*
Print movie_id, title, industry, imdb_rating, studio & average rating of that studio from the movies table of moviesdb database. 
Print the result sorted in ascending order of movie_id.
*/
use moviesdb;
with t as (
	select studio, round(avg(imdb_rating), 1) as studio_avg_rating
	from movies
	group by studio
)
select m.*, t.studio_avg_rating
from movies m
join t on m.studio=t.studio;

-- Get me the top 2 earners from each department in hr2 database - Foundation of Window Functions

-- Winodw Functions
/*
1. Aggregate Window Functions
2. Ranking Window Functions
3. Value Window Functions
*/
use moviesdb;
select *,
avg(imdb_rating) over()
from movies;
-- OR
select *
from movies
cross join (select avg(imdb_rating) from movies) t;

-- print avg imdb_rating of each industry beside every movie of that industry
select *,
round(avg(imdb_rating) over(partition by industry), 1) as industry_avg_rating,
round(avg(imdb_rating) over(partition by studio), 1) as studio_avg_rating
from movies;

/*
Create two new columns: 
relative_industry_performance - should have "avg", "above avg" or "below avg" while comparing that movies rating with industrty_avg_rating &
relative_studio_performance - should have "avg", "above avg" or "below avg" while comparing that movies rating with studio_avg_rating
in the output of above query.
*/