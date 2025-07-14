use as7;
with cte as (
	select *,
    rank() over(partition by gender order by user_id) as rank1,
    case
		when gender = "female" then 1
        when gender = "other" then 2
        else 3
	end as rank2
    from genders
)
select * from cte
order by rank1, rank2;

-- Q-6:
select product_id, "store1" as store, store1 as price
from products
where store1 is not null
union
select product_id, "store2" as store, store2 as price
from products
where store2 is not null
union
select product_id, "store3" as store, store3 as price
from products
where store3 is not null
order by 1;

use as8;
with t1 as (
	select city, count(*) as counts
	from trades t
	join users u
	using(user_id)
	where status = "Completed"
    group by city
),
t2 as (
select *,
rank() over(order by counts desc) as ranking
from t1
)
select *
from t2
where ranking <=3;

-- Q:3
with t1 as (
	select id as person_id, name as person_name, phone_number,
	cast(substr(phone_number, 1, 3) as signed) as country_code 
	from person p
),
t2 as (
	select c.name as country_name, cl.duration from t1
	join country c using(country_code)
    join calls cl on t1.person_id = cl.caller_id
),
t3 as (
	select c.name as country_name, cl.duration from t1
	join country c using(country_code)
    join calls cl on t1.person_id = cl.callee_id
),
t4 as (
	select * from t2
	union all
	select * from t3
	order by country_name
),
t5 as (
	select *,
	avg(duration) over(partition by country_name) as country_avg,
	avg(duration) over() as global_avg
	from t4
)
select distinct(country_name)
from t5 where country_avg > global_avg;

select * from calls;
select * from person;
select * from country;

-- Q:6 Winning Streak
select m1.player_id, ifnull(max(cnt), 0) as longest_streak
from matches m1
left join(
	select player_id, (p_rnk - rnk) as diff, count(p_rnk - rnk) as cnt
	from(
		select *,     
		rank() over(partition by player_id, result order by match_day) as rnk,
		rank() over(partition by player_id order by match_day) as p_rnk
		from matches m2
        ) t1
	where result = 'Win'
	group by player_id, diff
)t2
on m1.player_id = t2.player_id
group by m1.player_id
order by m1.player_id;

-- AS9 - Q:5
with items_sold as
(
    SELECT distinct(u.user_id) as seller_id, 
    nth_value(o.item_id, 2) over(partition by seller_id order by order_date range between unbounded preceding and unbounded following) 
    as second_item_sold,
    u.favorite_brand
    FROM users u
    left join orders2 o on u.user_id = o.seller_id
)
select seller_id,
case
    when i.item_brand = itm.favorite_brand then 'yes' else 'no'
end as 2nd_item_fav_brand
FROM items_sold as itm
left join items i on itm.second_item_sold = i.item_id 
order by seller_id;