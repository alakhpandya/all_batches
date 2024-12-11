use moviesdb;
select * from financials;
/*
select revenue - budget as profit, 
case
	when unit = "Billions" then profit*1000
    when unit = "Thousands" then profit/1000
    else profit
end as unit_mn, 
case
	when currency = "USD" then profit*80
    else profit
end as currency_mn
from financials;
*/

/*
select movie_id, profit_mn,
case
	when currency = "USD" then profit_mn*80
    else profit_mn
end as profit_inr_mn
from (
	select movie_id, profit, 
	case
		when unit = "Billions" then profit*1000
		when unit = "Thousands" then profit/1000
		else profit
	end as profit_mn, currency 
	from (
		select movie_id, revenue - budget as profit, unit, currency
		from financials
	) as t1
) as t2;
*/

-- CTE: Common Table Expression
with t1 as (
	select movie_id, revenue - budget as profit, unit, currency
	from financials
),
t2 as (
	select movie_id, profit, 
		case
			when unit = "Billions" then profit*1000
			when unit = "Thousands" then profit/1000
			else profit
		end as profit_mn, 
	currency 
	from t1
),
t3 as (
select movie_id, profit_mn,
case
	when currency = "USD" then profit_mn * 80
    else profit_mn
end as profit_inr_mn
from t2)

select m.movie_id, title, industry, round(profit_inr_mn, 2) as profit
from movies m
join t3
on m.movie_id = t3.movie_id
order by 4 desc;

with profitability as(
	select *, (revenue - budget)*100/budget as pct_profit
	from financials
),
below_avg as (
	select * from movies where imdb_rating < (select avg(imdb_rating) from movies)
)
select p.movie_id, title, pct_profit, imdb_rating
from profitability p
join below_avg b on p.movie_id = b.movie_id
where p.pct_profit >= 500;
