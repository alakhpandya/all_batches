use paintings;
select * from paintings;
select * from sales;

with t1 as
(
	select p.id as painting_id, p.artist_id, s.id as order_id,
    if(s.id is not null, "Sold", null) as "Status"
	from paintings p
	left join sales s
	on p.id = s.painting_id
),
t2 as
(
	select painting_id, artist_id, order_id, status,
	count(status) over(partition by artist_id) as paintings_sold
	from t1
)
select painting_id, artist_id, order_id, status,
if(paintings_sold > 1, "**", "") as Rating
from t2;

select p.id as painting_id, p.artist_id, s.id as order_id,
if(s.id is not null, "Sold", null) as "Status"
from paintings p
left join sales s
on p.id = s.painting_id;

