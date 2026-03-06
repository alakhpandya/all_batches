/*
Print all the columns of movies table along with a new column that is adj_imdb which is imdb_rating on the scale of 0 to 5. 
adj_imdb is half of the actual imdb_rating.
*/
use moviesdb;
select *, imdb_rating/2 adj_imdb
from movies;

/*
Print all the columns of movies table along with a new column at the end from moviesdb dataset & assign value 'old' to the movies which were released before 2000 
& label 'new' to the rest of the movies.
*/
-- if, case-when
select *,
if(release_year < 2000, "Old", "New") as "Old/New"
from movies;

select *,
case
	when release_year < 2000 then "Old"
    else "New"
end as "New/Old"
from movies;

-- print movie_id, revenue, unit & revenue in USD for the movie_ids whose currency is in INR. Take the exchange rate of 1 USD = 80 INR
select movie_id, revenue, unit, if(currency="INR", revenue/80, revenue) as revenue_USD
from financials;

/*
print all the columns of financials table along with two new columns - budget_USD & revenue_USD. 
Keep only the rows which have currency in INR with exchange rate of 1 USD = 85 INR
*/
select *, budget/85 as buget_USD, revenue/85 as revenue_USD
from financials
where currency = "INR";

-- Create a new column in the movies table with the name "language". Put value "English" into it if the language_id is 5 otherwise put "Other" in that column.

/*
In the employees table from hr dataset, create a new column named "payscale_evaluation". 
For the employees whose salary is above 15000 put "Overpaid" otherwise "Underpaid" in that column.
*/ 

use hr;
-- In the employees table from hr dataset, create a new column named "payscale_evaluation". 
-- For the employees whose salary is above 15000 put "Overpaid" 
-- for the employees whose salary is less than 5000 then "Underpaid" 
-- otherwise "OK" in that column.
select *,
-- if(salary > 15000, "Overpaid", if(salary < 5000, "Underpaid", "OK")) as payscale_evaluation
case
	when salary > 15000 then "Overpaid"
    when salary < 5000 then "Underpaid"
    else "OK"
end as payscale_evaluation
from employees;


-- In countries table of hr dataset, create a new column of "Region" and place "Asia" in it if the coutry_name is India, "Europe" if the country_name is France
-- and "Americas" if the coutry_name is United States of America
select *, 
case
	when country_name = "India" then "Asia"
    when country_name = "France" then "Europe"
    when country_name = "United States Of America" then "Americas"
end as region
from countries;


-- In the financials table from the moviesdb dataset, create a new column of budget_adj where we will convert all the units into Millions.
-- Also there is no need to return Unit column then after hence show only movie_id, budget, budget_adj and currency columns.
use moviesdb;
select movie_id, budget, 
case
	when unit="Billions" then budget*1000
    when unit="Thousands" then budget/1000
    else budget
end as budget_adj,
revenue,
case
	when unit="Billions" then revenue*1000
    when unit="Thousands" then revenue/1000
    else revenue
end as revenue_adj,
currency
from financials;

/*
In countries table of hr dataset create a new column named "region" and put the values in it as below:
"Southern Americas" if country_name is Argentina or Brazil 
"Northern Americas" if coutry_name is Canada, United States of America or Mexico
"Europe" if coutry_name is Belgium, Switzerland, Germany, Denmark, France, Italy, Netherlands or United Kingdom
"Asia-Pacific" if coutry_name is Australia, China, HongKong, India, Japan or Singapore
"Middle east" if country_name is Egypt, Israel, or Kuwait
"Africa" if country_name is Nigeria, Zambia or Zimbabwe
*/
use hr;
select *,
case
	when country_name in ("Argentina", "Brazil") then "Southern Americas"
	when country_name in ("Canada", "United States of America", "Mexico") then "Northern Americas"
	when country_name in ("Belgium", "Switzerland", "Germany", "Denmark", "France", "Italy", "Netherlands" "United Kingdom") then "Europe"
	when country_name in ("Australia", "China", "HongKong", "India", "Japan", "Singapore") then "Asia-Pacific"
	when country_name in ("Egypt", "Israel", "Kuwait") then "Middle east"
	when country_name in ("Nigeria", "Zambia", "Zimbabwe") then "Africa"
end as region
from countries;

/*
From movies table, create a column named "Box Office Performance" which has type of movie based on its ratings as below:
	Less than 4 - flop    
	4 - 5.9 - Average    
	6 - 7.9 - Hit    
	8 or more - Blockbuster
*/
select *,
case
	when imdb_rating < 4 then "Flop"
    when imdb_rating between 4 and 5.9 then "Average"
    when imdb_rating between 6 and 7.9 then "Hit"
    else "Blockbuster"
end as "Box Office Performance"
from movies;

/*
In movies table of moviesdb dataset, Create a column named "Language" which has value: 
"Hindi" if language_id is 1, 
"English" if language_id is 5, 
“Tamil” if language_id is 4, 
“Bengali” if language_id is 7 
otherwise “Other”
*/
select *,
case
	when language_id = 1 then "Hindi"
    when language_id = 5 then "English"
    when language_id = 4 then "Tamil"
    when language_id = 7 then "Bengali"
    else "Other"
end as Language
from movies;