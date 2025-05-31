drop database if exists school;
create database if not exists school;
use school;
create table if not exists students (
	roll_no int,
    first_name varchar(255),
    last_name varchar(255),
    -- mobile_no bigint
    mobile_no char(10),
    enrolled date,
    batch_time time
);

select * from students;
insert into students values(1, "Birva", "Bhatt", "987654321", "2025-04-12", "16:54:00");
truncate table students;
insert into students(roll_no, first_name, last_name, mobile_no, enrolled, batch_time) values(1, "Birva", "Bhatt", "987654321", "2025-04-12", "16:54:00");

alter table students rename to new_students;
select * from new_students;

alter table new_students rename column first_name to f_name;

drop table if exists new_students;

-- Table with constraints:

drop table if exists students;
create table if not exists students (
	student_id int primary key auto_increment,
    first_name varchar(255),
    last_name varchar(255),
    -- mobile_no bigint
    mobile_no char(10) unique,
    enrolled date not null,
    batch_time time not null default "07:00",
    is_active char(20) check(is_active in ("active", "inactive", "temporarily inactive")) default "active"
);

insert into students(first_name, last_name, mobile_no, enrolled, batch_time) values("Birva", "Bhatt", "987654321", "2025-04-12", "16:54:00");
insert into students(first_name, last_name, enrolled, batch_time) values("Hetal", "Tewar", "2025-04-12", "16:54:00");
insert into students(first_name, last_name, enrolled, is_active) values("Hema", "Raval", "2025-04-12", "inactive");

-- insert into students(first_name, last_name, enrolled, is_active) values("Anuj", "Jani", "2024-02-24", "ative");
insert into students(first_name, last_name, enrolled, is_active) values("Anuj", "Jani", "2024-02-24", "temporarily inactive");

select * from students;

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

set time_zone = "-05:30";

-- joins: Left, Right, Inner, Outer/Full Outer, Cross join, Self join
use moviesdb;

-- 1. Print language of each movie in the movies table
select * from movies;
select * from languages;

select m.movie_id, m.title, m.imdb_rating, m.language_id, l.name
from movies m
join languages l		-- inner join
on m.language_id = l.language_id;

select *
from movies m
join languages l		-- inner join
using(language_id);

-- Print actor_id vs. movies names that actor has played a role in. Sort your result in the ascending order of actor_id.
select * from movies;
select * from movie_actor;

select actor_id, title
from movie_actor ma
left join movies m
on ma.movie_id = m.movie_id
order by actor_id;

-- Print number of movies played by each actor_id sorted in ascending order of actor_id.
select actor_id, count(*)
from movie_actor
group by actor_id
order by actor_id;

-- Print actor names vs. movies played by each actor. That is, write name of the actor and names of movies played they played a role in.
use moviesdb;
select * from actors;
select * from movies;
select * from movie_actor;

-- cross join
select *
from actors a
cross join movie_actor ma;