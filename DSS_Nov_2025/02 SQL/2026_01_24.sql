use moviesdb;

select * from financials;

select movie_id, budget, unit, budget*85 as budget_INR
from financials
where currency = "USD";

-- print movie_id, revenue, unit & revenue in USD for the movie_ids whose currency is in INR. Take the exchange rate of 1 USD = 80 INR
select movie_id, revenue, unit, revenue/80 as revenue_USD
from financials
where currency = "INR";

-- print all the columns of financials table along with two new columns - budget_USD & revenue_USD. 
-- Keep only the rows which have currency in INR with exchange rate of 1 USD = 85 INR
select *, 
budget/85 as budget_USD,
revenue/85 as revenue_USD
from financials
where currency="INR";

select * from financials;

-- If / else: if
select *,
if(currency="INR", budget/100, budget) as budget_USD,
if(currency="INR", revenue/100, revenue) as revenue_USD
from financials;

/*
Print all the columns of movies table along with a new column movie_type & assign value 'old' to the movies which were released before 2000 & label 'new' 
to the rest of the movies. Use moviesdb dataset.
*/
select *
from movies;

-- Create a new column in the movies table with the name "language". Put value "English" into it if the language_id is 5 otherwise put "Other" in that column.
select *, if(language_id=5, "English", "Other") as language
from movies;

use hr;
select * from employees;
-- In the employees table from hr dataset, create a new column named "payscale_evaluation". 
-- For the employees whose salary is above 15000 put "Overpaid" otherwise "Underpaid" in that column.
select *, if(salary > 15000, "Overpaid", "Underpaid") as payscale_evalution
from employees;

-- In the employees table from hr dataset, create a new column named "payscale_evaluation". 
-- For the employees whose salary is above 15000 put "Overpaid" 
-- for the employees whose salary is less than 5000 then "Underpaid" 
-- otherwise "OK" in that column.
select *, if(salary > 15000, "Overpaid", if(salary < 5000, "Underpaid", "OK")) as payscale_evaluation
from employees;

select *,
CASE
	WHEN salary > 15000 THEN "Overpaid"
    WHEN salary < 5000 THEN "Underpaid"
    ELSE "OK"
END as payscale_evaluation
from employees;

-- In countries table of hr dataset, create a new column of "Region" and place "Asia" in it if the coutry_name is India, "Europe" if the country_name is France
-- and "Americas" if the coutry_name is United States of America
select * from countries;

-- In the financials table from the moviesdb dataset, create a new column of budget_adj where we will convert all the units into Millions.
-- Also there is no need to return Unit column then after hence show only movie_id, budget, budget_adj and currency columns.

select movie_id, budget, 
CASE
	WHEN unit="Billions" THEN budget*1000
    when unit="Thousands" then budget/1000
    else budget
END as budget_adj, 
currency
FROM financials;

-- Round off the budget_adj column to 4 decimal places in the previous answer.
select movie_id, budget, 
ROUND(CASE
	WHEN unit="Billions" THEN budget*1000
    when unit="Thousands" then budget/1000
    else budget
END, 4)
as budget_adj, 
currency
FROM financials;

-- In the financials table from the moviesdb dataset, create two columns- budget_adj & revenue_adj where we will convert all the units into Millions.
-- Show only movie_id, budget, budget_adj, revenue, revenue_adj and currency columns. Also round off budget_adj & revenue_adj columns to 4 decimal places
select movie_id, budget, 
ROUND(CASE
	WHEN unit="Billions" THEN budget*1000
    when unit="Thousands" then budget/1000
    else budget
END, 4) as budget_adj, 
revenue, 
ROUND(CASE
	WHEN unit="Billions" THEN revenue*1000
    when unit="Thousands" then revenue/1000
    else revenue
END, 4) as revenue_adj,
currency
FROM financials;

/*
In countries column of hr dataset create a new column named "region" and put the values in it as below:
"Southern Americas" if country_name is Argentina or Brazil 
"Northern Americas" if coutry_name is Canada, United States of America or Mexico
"Europe" if coutry_name is Belgium, Switzerland, Germany, Denmark, France, Italy, Netherlands or United Kingdom
"Asia-Pacific" if coutry_name is Australia, China, HongKong, India, Japan or Singapore
"Middle east" if country_name is Egypt, Israel, or Kuwait
"Africa" if country_name is Nigeria, Zambia or Zimbabwe
*/


/*
From movies table from moviesdb database, create a column named "Box Office Performance" which has type of movie based on its ratings as below:
	Less than 4 - flop    
	4 - 5.9 - Average    
	6 - 7.9 - Hit    
	8 or more - Blockbuster
*/
select *,
case when imdb_rating < 4 then "flop"
-- when imdb_rating between 4 and 5.9 then "Average"
when 4 <= imdb_rating and imdb_rating <= 5.9 then "Average"
when imdb_rating between 6 and 7.9 then "Hit"
when imdb_rating >= 8 then "Blockbuster"
end as 'Box Office Performance'
from movies;

/*
In movies table of moviesdb dataset, Create a column named "Language" which has the following values in it: 
"Hindi" if language_id is 1, 
"English" if language_id is 5, 
“Tamil” if language_id is 4, 
“Bengali” if language_id is 7 
otherwise “Other”
*/