/*
Problem statement: Sort the movie titles in the descending order of their profit.

1. Calculate profit of each movie
2. Convert all of them in same unit
3. Convert all of them in same currency
*/
use moviesdb;
with t1 as
(
	select movie_id, if(currency="USD", budget*80, budget) as budget,
    if(currency="USD", revenue*80, revenue) as revenue, unit
    from financials
),
t2 as
(
	select movie_id,
    case
		when unit = "Billions" then budget*1000
        when unit = "Thousands" then budget/1000
        else budget
	end as budget,
    case
		when unit = "Billions" then revenue*1000
        when unit = "Thousands" then revenue/1000
        else revenue
	end as revenue
    from t1
)
select m.movie_id, m.title, round(revenue - budget, 2) as profit
from movies m
left join t2 on m.movie_id = t2.movie_id
order by 3 desc;

use classwork;
select * from product;

create table new_products (
	product_id int primary key,
    prodcut_name varchar(50)
);
insert into new_products values 
(400, "Google"),
(500, "One Plus"),
(200, "Apple");

select * 
from product
-- union
union all
select *
from new_products;

select * from google_gmail_emails;
insert into google_gmail_emails values (7, "Ayush", "Alakh", 3);
select * from google_gmail_labels;
insert into google_gmail_labels values (8, "Spam");