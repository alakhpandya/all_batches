use classwork;
-- create table if not Exists genders (user_id int, gender varchar(20));
-- Truncate table genders;
insert into genders (user_id, gender) values (1, "male");
insert into genders (user_id, gender) values (2, "other");
insert into genders (user_id, gender) values (3, "other");
insert into genders (user_id, gender) values (4, "male");
insert into genders (user_id, gender) values (5, "female");
insert into genders (user_id, gender) values (6, "male");
insert into genders (user_id, gender) values (7, "female");

select * from genders;

with cte as (
	select *,
    rank() over(partition by gender order by user_id) as rank1,
    case 
		when gender = 'female' then 1
        when gender = 'other' then 2
        else 3
	end as rank2
	from genders
) 
select user_id, gender
from cte
order by rank1, rank2;

use moviesdb;
select * from languages;
select *,
lead(name, 2, name) over() as nextt,
lead(name, 2, "N/A") over() as nextt2
from languages;
