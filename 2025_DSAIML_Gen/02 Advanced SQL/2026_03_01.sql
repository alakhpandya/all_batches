create database if not exists temp;
use temp;
-- select * from table_1;
-- truncate table table_1;
drop table if exists t1;
create table t1 (
	id int,
    f_name varchar(50),
    l_name varchar(50),
    gender char(1),
    mobile char(10),
    marks float,
    dob timestamp,
    departure_time time
);
truncate table t1;
alter table t1 rename to students;
select * from students;
alter table students rename column departure_time to exam_time;
select * from students;

drop table if exists students;
create table students(
	id int,
    name varchar(50)
);
insert into students values (1, "Vishwa");
insert into students values 
(3, "Krishna"),
(4, "Pratham"),
(5, "Soham");

insert into students (id, name) values (2, "Sia");
insert into students (id, name) values 
(3, "Krishna"),
(4, "Pratham"),
(5, "Soham");

select * from students;

-- Constraints
drop table if exists students;
create table students(
	id int primary key auto_increment,
    f_name varchar(50) not null,
    l_name varchar(50),
    email varchar(100) unique
);
insert into students values (100, "Vishwa", null, "v@g.com");

insert into students (f_name, l_name) values ("Pratham", "Bodana");

insert into students values (200, "Panth", null, "p@g.com");
select * from students;
insert into students (f_name, l_name) values ("Pratham", "Bodana");

/*
Create a database named 'banking' which has the following tables:
customers table which has following columns (choose suitable datatypes yourself):
cust_id
first_name
last_name
mobile_no
address
dob
is_active – values in this column can be either active or inactive only
*/
drop database if exists banking;
create database banking;
use banking;
create table customers (
	cust_id int primary key auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50),
    mobile_number char(10) unique,
    address varchar(200),
    dob date,
    is_active varchar(8) check(is_active in ("Active", "Inactive"))
);

create table articles(
	article_id int primary key auto_increment,
    article_name varchar(100) not null,
    author_name varchar(100) default "Unknown",
    publish timestamp default current_timestamp
);
truncate table articles;
insert into articles (article_name, author_name, publish) values ("Side effects of SQL", "Dhaval Prajapati", "2025-12-31 17:25:30");
select * from articles;
insert into articles (article_name) values ("Holi celebration in India");

set time_zone = "+05:30";
select * from articles;

/*
Create a table named ’products’ with columns product_id, product_name, product_description, purchase_time and availability 
where product_name must not repeat and availability may have only one of two values "Available"/"Not Available". 
Add 5 products in it
*/
create table if not exists customers2(
	cust_id int primary key auto_increment,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    mobile_no bigint unique,
    address varchar(255),
    dob timestamp check(dob <= current_timestamp()),
    is_active varchar(8) check(is_active in ("Active","Inactive"))
);
