-- CRUD: Create, Read, Update, Delete
-- create database school;
create database if not exists school;

use school;
create table if not exists Student(
	id int,
    f_name varchar(255)
);
Truncate table Student;
insert into student values(1, "Jalpesh");

-- drop table Student;
-- drop database school;

alter table student rename column f_name to first_name;
insert into student (id, first_name) values(2, "Asutosh");
insert into student (id, first_name) values
(3, "Ronak"),
(4, "Umesh"),
(5, "Mehul");
select * from Student;
alter table student rename to new_student;

drop table if exists student;
create table if not exists Student(
	id int primary key auto_increment,
    first_name varchar(255) not null default "Lalo",
    last_name varchar(255),
    mobile bigint unique,
    email varchar(255) unique not null,
    is_active varchar(8) check(is_active in ("Active", "Inactive"))
);
insert into student (first_name, last_name, email) values("Jalpesh", "Dave", "jd@gmail.com");
insert into student (first_name, mobile, email) values("Asutosh", 9876543210, "ad@gmail.com");
insert into student (first_name, last_name, mobile, email) values("Ronak", "Patel", 1234567890, "bd@gmail.com");
insert into student (last_name, mobile, email) values("Patel", 1234567890, "cd@gmail.com");

select * from student;

CREATE TABLE Articles ( 
	articleId INT AUTO_INCREMENT PRIMARY KEY, 
	articleTitle VARCHAR(60), 
	dateCreated TIMESTAMP, 
	datePublished TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- set time_zone = "+05:30";
INSERT INTO 
	Articles ( articleTitle, dateCreated ) 
VALUES 
	('Sample 1', '2019-07-21 00:00:01'), 
	('Sample 2', '2019-07-14 00:00:01'), 
	('Sample 3', '2019-07-07 00:00:01'), 
	('Sample 4', '2019-07-01 00:00:01');

select * from articles;

set time_zone = "05:30";

drop database if exists school;
create database if not exists school;
use school;
drop table if exists students;
create table if not exists students (
	student_id int primary key auto_increment,
    first_name varchar(255),
    last_name varchar(255),
    -- mobile_no bigint
    mobile_no char(10) unique,
    subscription timestamp default current_timestamp,
    is_active char(20) check(is_active in ("active", "inactive", "temporarily inactive")) default "active"
);
insert into students(first_name, last_name, is_active) values("Rushir", "Sheth", "active");
select * from students;
set time_zone = "+05:30";