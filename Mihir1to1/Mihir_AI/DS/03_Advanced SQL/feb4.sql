use moviesdb;
select m.movie_id, m.title, f.profit
from movies m
join 
(
	select movie_id, reveue_inr_millions - budget_inr_millions as profit
	from
	(
		select *,
		case
			when unit="Billions" then budget_inr * 1000
			when unit="Thousands" then budget_inr / 1000
			else budget_inr
		end as budget_inr_millions,
		case
			when unit="Billions" then revenue_inr * 1000
			when unit="Thousands" then revenue_inr / 1000
			else revenue_inr
		end as reveue_inr_millions
		from
		(
			select *,
			if(currency = "USD", budget*80, budget) as budget_inr,
			if(currency = "USD", revenue*80, revenue) as revenue_inr
			from financials
		) as f1
	) as f2
) as f on f.movie_id = m.movie_id
order by profit desc;