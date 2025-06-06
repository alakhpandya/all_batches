use moviesdb;

select *
from movies;

select *,
row_number() over() as sr_no,
row_number() over(partition by studio order by studio) as group_wise_sr
from movies;

use paintings;

select * from artists;

select *,
row_number() over(partition by first_name order by first_name) duplication
from artists;

select *
from (
	select *,
	row_number() over(partition by first_name order by first_name) duplication
	from artists
) x
where duplication > 1;

-- delete
select *
from artists
where id in (
	select id
	from (
		select *,
		row_number() over(partition by first_name, last_name order by first_name) duplication
		from artists
	) x
	where duplication > 1
);

select * from artists;