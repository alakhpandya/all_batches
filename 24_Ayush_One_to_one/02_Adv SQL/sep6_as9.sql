use as9;
select * from users;
select * from orders2;
select * from items;

-- 2nd order
with t1 as
(
	select *,
	row_number() over(partition by seller_id order by order_date) as num
	from orders2
),
t2 as
(
	select seller_id, order_date, item_id
	from t1
	where num > 1 
),
t3 as
(
	select u.user_id as seller_id, favorite_brand, t2.item_id
	from users u
	left join t2
	on u.user_id = t2.seller_id
)
select t3.seller_id,
case
	when t3.favorite_brand = i.item_brand then "yes"
    else "no"
end as 2nd_item_fav_brand
from t3
left join items i
on t3.item_id = i.item_id;