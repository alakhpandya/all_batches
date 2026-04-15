create database banking;
use banking;
create table customers(
	customer_id int primary key auto_increment,
    first_name varchar(100) not null,
    last_name varchar(100),
    phone bigint unique,
    address varchar(200),
    balance bigint default 25000,
    dob date,
    is_active varchar(10) check(is_active in ("active", "inactive")),
    date_of_reg timestamp default current_timestamp
);

insert into customers (first_name, phone, is_active) values 
("Rahul", 9876543210, "active"),
("Gini", 1234567890, "inactive"),
("Madhusudan", null, null);
-- ("Samir", 9876543210, "active");
-- ("Tejas", 9898898901, "N/A");
-- (null, 8888999912, "inactive");
truncate table customers;
select * from customers;

set time_zone = "-07:00";
set time_zone = "+05:30";

/*
Create a new database named: blog
Create a table "articles" in the blog database with the following columns:
- article_id: integer, auto-incrementing, starting from 1. Also make this primary key
- title: 100 character long (max)
- date_created: no default date
- date_published: default should be current timestamp value
"yyyy-mm-dd"
"yyyy-mm-dd hh:mm:ss"
*/

create database blog;
use blog;
create table articles (
	aritcle_id int primary key auto_increment,
    title varchar(100) not null,
    date_created timestamp,
    date_published timestamp default current_timestamp
);
insert into articles values(1, "Side effects of SQL", "2025-12-31", "2026-01-14");
insert into articles (title, date_created, date_published) values 
("Benefits of mySQL", "2025-09-08", "2025-10-01 05:30:00");

select * from articles;

/*
Create a table named ’products’ with columns product_id, product_name, product_description, purchase_time and availability 
where product_name must not repeat and availability may have only one of two values "Available"/"Not Available". 
Take constraints of the other columns as per your wisdom. 
Add 5 products in it
*/

-- Joins
-- Syntax:
use hr2;
select * from employees;
-- Difference between