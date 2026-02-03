create database if not exists temp;
use temp;

drop table if exists t1;
create table if not exists t1(
	sr_no int,
    name varchar(255)
);

truncate table t1;
insert into t1 values (1, "Mohit");
insert into t1(sr_no, name) values (2, "Nikita");
-- insert into t1 values ("Jay");			Error
insert into t1(name) values ("Jay");
insert into t1(name, sr_no) values ("Arbaz", 4);

select * from t1;

alter table t1 rename to table_1;
select * from table_1;

alter table table_1 rename column sr_no to stu_id;
select * from table_1;

/*
Create a database named 'banking' which has the following tables:
customers table which has following columns (choose suitable datatypes yourself):
cust_id
first_name
last_name
mobile_no
address
dob
is_active – values in this column will be either active or inactive only
*/
drop database banking;
create database banking;
use banking;

drop table if exists customers;
create table customers(
customer_id int auto_increment primary key,
first_name varchar(100) not null,
last_name varchar(100) DEFAULT "N/A",
-- phone int(16),			Depricated
phone varchar(10) unique,
address varchar(100),
dob date,
is_active varchar(10) check (is_active in ("active", "inactive"))
);

truncate table customers;
/*
insert into customers values (
	1, null, "Shaikh", 9999988888, "ABCD", "2005-12-26", "active"
);
insert into customers values (
	1, "Aman", "Shaikh", 9999988888, "ABCD", "2005-12-26", "active"
);
insert into customers values (
	1, "Ruchir", "Ganatra", "1111122222", "ABCD", "2005-12-26", "active"
);
*/
insert into customers (first_name, last_name, phone, address, dob, is_active) values (
	"Ruchir", "Ganatra", "1111122222", "ABCD", "2005-12-26", "active"
);
insert into customers (first_name, phone, address, dob, is_active) values (
	"Arbaz", "1101020403", "ABCD", "2005-12-26", "inactive"
);

insert into customers values (
	4, "Arbaz", "Shaikh", "3333311111", "ABCD", "2005-12-26", "active"
);

select * from customers;

-- TIME STAMP
CREATE TABLE Articles ( 
	articleId INT AUTO_INCREMENT PRIMARY KEY, 
	articleTitle VARCHAR(60), 
	dateCreated TIMESTAMP, 
	datePublished TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 

SET TIME_ZONE = '+00:00'; 

INSERT INTO 
	Articles ( articleTitle, dateCreated ) 
VALUES 
	('Sample 1', '2019-07-21 00:00:01'), 
	('Sample 2', '2019-07-14 00:00:01'), 
	('Sample 3', '2019-07-07 00:00:01'), 
	('Sample 4', '2019-07-01 00:00:01');
select * from Articles;
SET TIME_ZONE = "+05:30";
select * from Articles;
INSERT INTO 
	Articles ( articleTitle, dateCreated, datePublished) 
VALUES 
	('Sample 5', '2019-07-21 00:00:01', '2020-07-21 00:00:01'),
	('Sample 5', '2019-07-21 00:00:01', DEFAULT),
	('Sample 5', '2019-07-21 00:00:01', '2020-07-21 00:00:01');


/*
Create a table named ’products’ with columns product_id, product_name, product_description, purchase_time and availability where product_name must not repeat and 
availability may have only one of two values "Available"/"Not Available". 
Add 5 products in it
*/

-- JOINS
use moviesdb;
select * from movies;
select * from financials;

-- Combining these two tables, print movie_id, title, industry, budget, unit, currency & studio
select movie_id, title, industry, budget, unit, currency, studio
from movies
-- join financials		-- inner join
inner join financials
-- using(movie_id);		-- natural join
on movies.movie_id = finaincials.movie_id;

-- select *
select m.movie_id, title, industry, budget, unit, currency, studio
from movies m
inner join financials f
on m.movie_id = f.movie_id;

-- Print the language_name of each movie in the movies table (return all columns including language_name)
select m.*, l.name as language_name
from movies m
join languages l
on m.language_id = l.language_id;