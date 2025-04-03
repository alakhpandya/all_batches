use hr;
select * from employees;

-- Error-1: Using aggreegate functions without group by
select department_id, max(salary)
from employees;
-- group by department_id;

-- Either aggregate the columns or put them in group by
select first_name, last_name, max(salary)
from employees
group by first_name, last_name;

-- Create a new column at the end of movies table from moviesdb & assign value 'old' to the movies which were released before 2000 & label 'new' to the rest of the movies.
use moviesdb;
select *,
case
	when release_year < 2000 then "old"
    else "new"
end as "new/old"
from movies;

/*
From movies table, create a column named "Box Office Performance" which has type of movie based on its ratings as below:
  Less than 4 - flop   
  4 - 5.9 - Average   
  6 - 7.9 - Hit   
  8 or more - Blockbuster
*/
select *,
case
	when imdb_rating < 4 then "flop"
	when imdb_rating >= 4 and imdb_rating < 6 then "Average"
	when imdb_rating >= 6 and imdb_rating < 8 then "Hit"
    when imdb_rating >= 8 then "Blockbuster"
    else "N/A"
end as "Box Office Performance"
from movies;

-- In financials table, convert budget & revenue of each movie into millions and name the new columns as: budget_mn & revenue_mn
select * from financials;
select distinct unit from financials;
select *,
case
	when unit = "Billions" then budget*1000
    when unit = "Thousands" then budget/1000
    else budget
end as budget_mn,
case
	when unit = "Billions" then revenue*1000
    when unit = "Thousands" then revenue/1000
    else revenue
end as revenue_mn
from financials;
/*
In moviesdb, using ‘financials’ table print a new table that has the following columns:
movie_id: as it is
USD_budget: budget converted in USD
USD_revenue: revenue converted in USD
USDunit: unit column as it is
*/
select *,
if(currency="INR", budget/85, budget) as budget_USD,
if(currency="INR", revenue/85, revenue) as revenue_USD
from financials;

select *,
if(unit="Billions", budget*1000, if(unit="Thousands", budget/1000, budget)) as budget_mn
from financials;

/*
In movies table of moviesdb dataset, Create a column named "Language" which has value "Hindi" if language_id is 1, "English" if language_id is 5, “Tamil” if language_id is 4, 
“Bengali” if language_id is 7 otherwise “Other”
*/

-- Datatypes in SQL:
/*
1. char
2. varchar
Difference between char(100) & varchar(100)
3. int
4. big int
5. date
6. time
7. datetime
8. timestamp - can also store time zone info and is faster in performance when compared with datetime
*/

-- CRUD: Create, Read, Update & Delete

drop database school;
-- create database school;
create database if not exists school;
use school;
create table students(
	name varchar(255),
	age int
);
select * from students;
-- drop table students;
truncate table students;

alter table students rename column name to first_name;

insert into students values ("Akshay", 21);
insert into students (first_name, age) values ("Suhag", 19);

drop database if exists school;