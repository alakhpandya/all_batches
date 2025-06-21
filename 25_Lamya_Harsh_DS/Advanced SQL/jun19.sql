-- Datatypes
/*
char(255) vs. varchar(255): char(255) will occupie all 255 Bytes irrespective of the length of the data stored in it while varchar(255) occupies only the size 
required by the data in it, at max the data can be of 255 B.
int
bigint
date
time
datetime
timestamp - also contains the info about the time zone and is also faster in comparision to datetime when it comes to execution time
*/

-- create database temp1;

create database if not exists school;
use school;
-- create table students
create table if not exists students(
	name varchar(255),
    age int
);
truncate table students;

insert into students values ("Dishant", 21);
insert into students(name, age) values ("Tejas", 24);

select * from students;

alter table students rename to new_students;
alter table new_students rename column name to first_name;

select * from new_students;

-- drop table if exists new_students;
-- drop database if exists school;

CREATE TABLE Articles ( 
	articleId INT AUTO_INCREMENT PRIMARY KEY, 
	articleTitle VARCHAR(60), 
	dateCreated TIMESTAMP, 
	datePublished TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

INSERT INTO 
	Articles (articleTitle, dateCreated) 
VALUES 
	('Sample 1', '2019-07-21 00:00:01'), 
	('Sample 2', '2019-07-14 00:00:01'), 
	('Sample 3', '2019-07-07 00:00:01'), 
	('Sample 4', '2019-07-01 00:00:01');

set time_zone = "-4:00";

select * from articles;

-- Home work:
/*
Create a table named ’products’ with columns product_id, product_name, product_description, purchase_time and availability 
where product_name must not repeat and availability may have only one of two values "Available"/"Not Available". 
Now add 5 products in it
*/

-- Joins
-- Print language of each movie in the movies table using join
use moviesdb;

select *
from movies m
-- natural join languages;
join languages l
-- using(language_id);
on m.language_id = l.language_id;

-- Don’t show the language_id column twice in the previous output
select movie_id, title, m.industry, release_year, imdb_rating, studio, m.language_id, l.name
from movies m
join languages l
on m.language_id = l.language_id;

-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id.
select ma.actor_id, m.title
from movies m
join movie_actor ma
on m.movie_id = ma.movie_id
order by ma.actor_id;

-- Print number of movies played by each actor_id sorted in ascending order of actor_id.
select actor_id, count(movie_id)
from movie_actor 
group by actor_id
order by actor_id;
