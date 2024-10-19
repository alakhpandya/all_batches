-- create database temp; 
-- create database if not exists temp;
-- creating tables, inserting values...
-- use temp;
-- create table students (
--		id int PRIMARY KEY AUTOINCREMENT
-- 		name varchar(255),
--     	age int
-- );
-- create table if not exists students (
-- 	name varchar(255),
--     age int
-- );

-- alter table students rename to new_students;

-- alter table new_students rename column name to first_name;

-- insert into new_students values ("Bhagyashree", 19);
-- insert into new_students (name, age) values ("Bhavna", 21);

-- select * from new_students;
-- use classwork;

-- Create table If Not Exists ActorDirector (actor_id int, director_id int, timestamp int);
-- truncate ActorDirector;
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '0');
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '1');
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '1', '2');
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '3');
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('1', '2', '4');
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '5');
-- insert into ActorDirector (actor_id, director_id, timestamp) values ('2', '1', '6');

-- select * from ActorDirector;
-- drop table new_students;
-- drop database temp;

create database if not exists temp;
use temp;
/*
create table customers(
	customer_id varchar(50),
	first_name varchar(50),
	last_name varchar(50),
	phone int,
	address varchar(100),
	dob date,
	is_active varchar(10)
);

insert into customers (customer_id, first_name, last_name, phone, address, dob, is_active) values('C1','mohan','agarwal', 786766,'bangalore', '1990-05-07', 'active');
insert into customers values ('C2', null, 'Xavier', 786766, 'Chennai', '1995-05-07', 'Sandeep');


select * from customers;

drop table customers;
*/
/*
create table if not exists customers(
	customer_id varchar(50) primary key,
	first_name varchar(50) not null,
	last_name varchar(50),
	phone int unique,
	address varchar(100),
	dob date,
	is_active varchar(10) check (is_active in ('active', 'inactive'))
);
truncate customers;
select * from customers;

insert into customers (customer_id, first_name, last_name, phone, address, dob, is_active) values('C1','mohan','agarwal', 786766,'bangalore', '1990-05-07', 'active'); 
insert into customers values ('C2', 'James', 'Xavier', 7867669, 'Chennai', '1995-05-07', 'inactive');

alter table customers modify column phone bigint;

insert into customers values ('C3', 'Krutika', 'Aacharya', 1978676696795, 'Ahmedabad', '2003-08-07', 'active');
*/

CREATE TABLE Artciles ( 
	articleId INT AUTO_INCREMENT PRIMARY KEY, 
	articleTitle VARCHAR(60), 
	dateCreated TIMESTAMP, 
	datePublished TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 

SET TIME_ZONE = "-05:30";
INSERT INTO
	 Artciles ( articleTitle, dateCreated )  
VALUES 
	('Sample 1', '2019-07-21 00:00:01'), 
	('Sample 2', '2019-07-14 00:00:01'), 
	('Sample 3', '2019-07-07 00:00:01'), 
	('Sample 4', '2019-07-01 00:00:01');

SELECT * FROM Artciles;
SET TIME_ZONE = "+00:00";
SELECT * FROM Artciles;