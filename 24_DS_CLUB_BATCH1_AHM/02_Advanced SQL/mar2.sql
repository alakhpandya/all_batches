use paintings;
select * from artists;

-- Give me the artist names appearing more than once

-- Remove duplicate entries from the artist table

-- Display all the available paintings and all the artist. If a painting was sold then mark them as "Sold" and if more than 1 painting of an artist was sold then display 
-- "**" beside their name.

select * from paintings;
/*
with new_artists as 
(
	select id,first_name,last_name 
	from artists group by id,first_name,last_name 
	having count(id)>1 
	union 
    select * from artists 
	order by id 
)
*/

with new_artist as
(
	select distinct id, first_name, last_name
    from artists
),
t2 as
(
	select p.id as painting_id, name, s.id as sales_id, s.artist_id, first_name, last_name
	from paintings p
	left join sales s
	on p.id = s.painting_id
	left join new_artist a
	on s.artist_id = a.id
)
-- select * from t2;
select artist_id, first_name, last_name, count(*) 
from t2
group by artist_id, first_name, last_name;