/*
Print the movies which produced more than 500% profit despite of having lower ratings than the average. 
Formula to find percentage profit is: profit * 100 / Budget.
Use CTE method instead of subquery if needed.
*/
use moviesdb;
with t as (
	select movie_id, (revenue - budget)*100/budget as profit_pct
	from financials
)
select m.*
from movies m
join t on m.movie_id = t.movie_id
where t.profit_pct > 500 and imdb_rating < (select avg(imdb_rating) from movies);

/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ 
(Use ‘demo’ database)
*/
-- Using multiple CTE:
with t1 as (
	select order_number, sales, so.customer, deal_size, c.city
    from sales_order so
    join customers c on so.customer=c.customer_id
),
t2 as (
	select city, round(avg(sales), 2) as city_avg
	from sales_order so
	join customers c on so.customer=c.customer_id
	group by city 
)
select * 
from t1
join t2 on t1.city=t2.city
where deal_size <> "Small" and sales > city_avg;

-- Print the movie titles, industry and profit of each movie. Sort the result in descending order of profit (profit = revenue – budget). Use CTE in place of subqueries.
use moviesdb;
with t1 as (
	select movie_id, 
    if(currency="USD", budget*80, budget) as budget_inr,
    if(currency="USD", revenue*80, revenue) as revenue_inr,
    unit
	from financials
),
t2 as (
	select movie_id,
    case
		when unit = "Billions" then budget_inr*1000
        when unit = "Thousands" then budget_inr/1000
        else budget_inr
	end as budget_mn_inr,
	case
		when unit = "Billions" then revenue_inr*1000
        when unit = "Thousands" then revenue_inr/1000
        else revenue_inr
	end as revenue_mn_inr
    from t1
)
select m.*, round(revenue_mn_inr - budget_mn_inr, 2) as profit 
from movies m
left join t2 on m.movie_id = t2.movie_id
order by profit desc;

-- Find the difference in average sales for each month of 2003 and 2004 (Use ‘demo’ database)
use demo;
select min(month_id), max(month_id) from sales_order;
with t1 as (
	select month_id, avg(sales) avg_sales_2004
	from sales_order
	where year_id = 2004
	group by month_id
	order by month_id
),
t2 as (
	select month_id, avg(sales) avg_sales_2003
	from sales_order
	where year_id = 2003
	group by month_id
	order by month_id
)
select t1.month_id, 
round(t1.avg_sales_2004 - t2.avg_sales_2003, 2) as sales_diff
from t1
join t2 on t1.month_id = t2.month_id;

/*
Find the popularity percentage for each user on Meta/Facebook. 
The popularity percentage is defined as the total number of friends the user has, divided by the total number of users on the platform, 
then converted into a percentage by multiplying by 100. 
Output each user along with their popularity percentage. Order records in ascending order by user id.
*/
use classwork;
with t as (
	select user1, user2 from facebook_friends
	union
	select user2, user1 from facebook_friends
)
-- select count(distinct user1) from t;
select user1, count(user2)*100/(select count(distinct user1) from t) as popularity_pct
from t
group by user1
order by user1;