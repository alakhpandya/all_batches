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