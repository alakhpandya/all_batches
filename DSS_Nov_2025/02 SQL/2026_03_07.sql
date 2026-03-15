-- creating full outer join using union
use hr2;
select *
from employees e
left join departments d on e.department_id = d.department_id
union
select *
from employees e
right join departments d on e.department_id = d.department_id;

select * from employees;

/*
Identify how many cars, motorcycles, trains and ships are available in the inventory. 
Treat all types of cars just as “Cars”. DO NOT USE ‘LIKE’ IN THIS EXAMPLE. (Use ‘demo’ database)
*/
-- using case-when
use demo;
select case 
	when product_line in ("Classic Cars", "Vintage Cars") then "Cars"
    else product_line
end as new_product_line, count(*)
from products
group by new_product_line;

-- using union
select product_line, count(*)
from products
where product_line not in ("Classic Cars", "Vintage Cars")
group by product_line
union
select "Cars" as product_line, count(*)
from products
where product_line in ("Classic Cars", "Vintage Cars");

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
left join artists a on p.artist_id=a.id
left join sales s on p.id=s.painting_id;

-- Give me the artist names appearing more than once in the artists table
select first_name, last_name
from artists
group by first_name, last_name
having count(*) > 1;

-- Get me the top 2 earners from each department
use hr;

/*
Print movie_id, title, industry, imdb_rating, studio & average rating of that studio from the movies table of moviesdb database. 
Print the result sorted in ascending order of movie_id.
*/
use moviesdb;
select movie_id, title, industry, imdb_rating, m.studio, studio_avg_rating
from movies m
join (
	select studio, avg(imdb_rating) as studio_avg_rating
	from movies
	group by studio
) t on m.studio = t.studio
order by movie_id;

-- Practice Questions
-- Fetch two employees from each department who joined first. Use hr2 database.
use hr2;
with t1 as (
	select employee_id, first_name, last_name, hire_date, department_id, salary,
	rank() over(partition by department_id order by hire_date) as joining_order 
	from employees
)
select *
from t1
where joining_order <= 2;

-- Print top 3 earners from each department. Use hr2 database.
with t1 as (
	select employee_id, first_name, last_name, hire_date, department_id, salary,
	rank() over(partition by department_id order by salary desc) as earner_rank 
	from employees
)
select *
from t1
where earner_rank <= 3;

-- Print 5 most profitable movies of each industry
use moviesdb;
with t1 as (
	select movie_id, revenue - budget as profit, unit, currency
	from financials
),
t2 as (
	select movie_id,
    case when unit = "Billions" then profit*1000
    when unit = "Thousands" then profit/1000
    else profit
    end as profit,
    currency
    from t1
),
t3 as (
	select industry, title, profit, currency,
	rank() over(partition by industry order by profit desc) as profitability_rank
	from t2
	join movies m on m.movie_id = t2.movie_id
)
select *
from t3
where profitability_rank <= 5;

/*
Find the number of emails received by each user under each built in email label. The email labels are: ‘Promotion’, ‘Social’ and ‘Shopping’. 
Output the user along with the number of promotion, social & shopping emails they got. Use google_gmail database.
*/
use classwork;
select to_user,
sum(case when label = 'Promotion' then 1 else 0 end) as Promotion,
sum(case when label = 'Social' then 1 else 0 end) as Social,
sum(case when label = 'Shopping' then 1 else 0 end) as Shopping
from google_gmail_emails E
left join google_gmail_labels L on L.email_id = E.id
group by to_user;

select * from google_gmail_emails E
left join google_gmail_labels L on L.email_id = E.id;
