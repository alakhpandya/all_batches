/*
In moviesdb, using ‘financials’ table print a new table that has the following columns:
movie_id: as it is
USD_budget: budget converted in USD
USD_revenue: revenue converted in USD
Unit: unit column as it is
*/
use moviesdb;
select movie_id,
if(currency="INR", budget/80, budget) as budget_USD,
if(currency="INR", revenue/80, revenue) as budget_USD,
unit
from financials;

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
end as language
from movies;

-- Datatypes:
/*
- char(50) vs. varchar(50)
- int, bigint
- float
- date
- time
- datetime vs. timestamp
*/

-- Creating new database:
create database temp_2026;

-- Deleting a database
drop database temp_2026;

create database if not exists temp;
use temp;

drop table if exists students;

create table students(
name varchar(100),
age int,
gender char(1)
);

truncate table students;
select * from students;

alter table students rename column name to full_name;

alter table students rename to new_students;

select * from new_students;

drop table new_students;
drop database temp;
drop database if exists school;

create database school;
use school;
create table students(
name varchar(100),
age int
);

insert into students values ("Mosam" , 18);
insert into students (name, age) values ("Kalp", 19);
-- insert into students values ("Kushal");			Error
insert into students (name) values ("Kushal");
insert into students (name, age) values 
("Yash", 20),
("Shalin", 21),
("Vraj", null);

select * from students;