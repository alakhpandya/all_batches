create database if not exists school;
use school;
create table if not exists students (
	name varchar(255),
    age int
);
truncate table students;
insert into students values("Rakhil", 24);
insert into students values("Jhanvi", 22);
insert into students(name, age) values("Mehul", 27);

select * from students;

alter table students rename column age to experience;
alter table students rename column name to first_name;
select * from students;

drop table students;
drop table if exists students;

drop database if exists school;

create database if not exists banking;
use banking;
create table customers(
customer_id int primary key,
first_name varchar(50) not null,
last_name varchar(50),
phone bigint unique,
address varchar(100),
dob date,
is_active varchar(10) check(is_active in('active','inactive')));

-- insert into customers values(1, null, "Patel", 987654, "Palace", "2000-01-20", "active");
-- insert into customers values(1, "Kaushik", "Patel", 987654, "Palace", "2000-01-20", "active");
-- insert into customers values(1, "Manish", "Vyas", 987654, "Palace", "2000-01-20", "active");
-- insert into customers values(2, "Manish", "Vyas", 987643, "Palace", "2000-01-20", "N/A");
insert into customers values(2, "Manish", "Vyas", 987643, "Palace", "2000-01-20", "inactive");

select * from customers;

CREATE TABLE Articles ( 
	articleId INT AUTO_INCREMENT PRIMARY KEY, 
	articleTitle VARCHAR(60), 
	dateCreated TIMESTAMP, 
	datePublished TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

insert into articles values(1, "Effects of AI", "2014-08-31", "2025-06-04");
-- insert into articles values("Side Effects of AI", "2018-08-31");
insert into articles(articleTitle, dateCreated) values("Side Effects of AI", "2018-08-31");

select * from articles;

set time_zone = "+00:00";

select * from articles;

INSERT INTO 
	Articles ( articleTitle, dateCreated ) 
VALUES 
	('Sample 1', '2019-07-21 00:00:01'), 
	('Sample 2', '2019-07-14 00:00:01'), 
	('Sample 3', '2019-07-07 00:00:01'), 
	('Sample 4', '2019-07-01 00:00:01');

select * from articles;

-- Home work:
/*
Create a table named ’products’ with columns product_id, product_name, product_description, purchase_time and availability where product_name must not repeat and 
availability may have only one of two values "Available"/"Not Available". 
Add 5 products into it.
*/