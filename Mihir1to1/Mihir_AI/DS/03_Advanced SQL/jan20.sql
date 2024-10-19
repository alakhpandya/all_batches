use classwork;
drop table if exists customers;
create table customers(
customer_id int auto_increment Primary key,
first_name varchar(50) not null,
last_name varchar(50),
phone int unique,
address varchar(100),
dob date,
is_active varchar(10) check(is_active in ('active', 'inactive'))
);

truncate table customers;
insert into customers (customer_id, first_name, last_name, phone, address, dob, is_active) values ('1','mohan','agarwal', 786766,'bangalore', '1990-05-07', 'active');
insert into customers values ('2', 'James', 'Xavier', null, 'Chennai', '1995-05-07', 'active');
-- insert into customers (customer_id, first_name, last_name, phone, address, dob, is_active) values (Null,'Sohan','Shah', 790364,'bangalore', '1995-04-17', 'active');
-- insert into customers (customer_id, first_name, last_name, phone, address, dob, is_active) values (2,'Sohan','Shah', 790364,'bangalore', '1995-04-17', 'active');
insert into customers (first_name, last_name, phone, address, dob, is_active) values ('Sohan','Shah', 790364,'bangalore', '1995-04-17', 'active');
insert into customers (first_name, last_name, phone, address, dob, is_active) values ('Neha','Talati', 890534,'Bharuch', '1996-05-27', 'inactive');
select * from customers;

drop table if exists Articles;
CREATE TABLE Articles ( 
	articleId INT AUTO_INCREMENT PRIMARY KEY, 
	articleTitle VARCHAR(60) DEFAULT "UN-NAMED ARTICLE", 
	dateCreated TIMESTAMP, 
	datePublished TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 

truncate table Articles;
SET TIME_ZONE = '+00:00';
insert into Articles (articleId, articleTitle, dateCreated) values(1, "My Article", "2024-01-14");
insert into Articles (dateCreated) values("2023-12-18");
select * from Articles;

SET TIME_ZONE = '+05:30';