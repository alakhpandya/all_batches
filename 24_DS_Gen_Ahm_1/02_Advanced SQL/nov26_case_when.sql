-- 40) Create a new column at the end of movies table from moviesdb & assign value 'old' to the movies which were released before 2000 & label 'new' to the rest of the movies.
use moviesdb;
/*
select *,
case 
	when release_year < 2000 then "old"
    else "new"
end as "Type"
from movies;
*/
select *,
if(release_year < 2000, "old", "new") as "Type"
from movies;

/*
41) Create a column named "Box Office Performance" which has type of movie based on its ratings as below:
	Less than 4 - flop    
	4 - 5.9 - Average    
	6 - 7.9 - Hit    
	8 or more - Blockbuster
*/
select *,  
case 
	when imdb_rating<4 then "flop"  
    when imdb_rating between 4 and 5.9 then "Average"
	when imdb_rating between 6 and 7.9 then "Hit" 
    when imdb_rating between 8 and 10 then "Blockbuster"
end "Box Office Performance" 
from movies;

select * from financials;

-- 42) Convert budget & revenue of each movie into millions and name the new columns as: budget_mn & revenue_mn
select movie_id, currency,
case
      when unit like "Billions" then budget*1000
      when unit like "Thousands" then budget/1000
      else budget 
end as "budget_mn", 
case
      when unit like "Billions" then revenue*1000
      when unit like "Thousands" then revenue/1000
      else revenue 
end as "revenue_mn"
from financials;

/*
43) In movies table of moviesdb dataset, Create a column named "Language" which has value "Hindi" if language_id is 1, 
"English" if language_id is 5, “Tamil” if language_id is 4, “Bengali” if language_id is 7 otherwise “Other”
*/

drop database if exists temp;
create database if not exists temp;
use temp;
create table if not exists temp1 (
	id int,
    name varchar(255)
);
truncate table temp1;
insert into temp1 (id, name) values (1, "Hello");
select * from temp1;

alter table temp1 rename to temp2;
drop table if exists temp2;
drop table if exists temp1;
create table if not exists temp1 (
	id int primary key auto_increment,
    first_name varchar(255) not null,
    last_name varchar(255),
    mobile bigint unique,
    email varchar(100) unique not null
);
insert into temp1 (first_name, last_name, mobile, email) values("Hello", null, 1234, "abc@pq.com");
insert into temp1 (id, first_name, last_name, mobile, email) values(2, "Hi", "Universe", 5234, "xyz@pq.com");


select * from temp1;