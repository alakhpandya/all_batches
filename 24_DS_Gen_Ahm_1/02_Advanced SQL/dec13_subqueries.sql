use moviesdb;

select * from financials;

-- print movie titles & their budget in the descending order of budget
select m.title, f.budget
from movies m
join financials f
on m.movie_id = f.movie_id
order by f.budget desc;

select distinct unit from financials;

-- Task-1: converting all budget & revenue into millions
-- Task-2: converting all budget & revenue into INR
-- Task-3: print titles, budget & revenue of each movie in the movies table in any order
select m.movie_id, m.title, t2.budget_mn_inr, t2.revenue_mn_inr
from 
(
	select movie_id,
		if(currency="USD", budget_mn*80, budget_mn) as budget_mn_inr,
		if(currency="USD", revenue_mn*80, revenue_mn) as revenue_mn_inr
	from
	(
		select movie_id, currency,
		case
			when unit="Billions" then budget*1000
			when unit="Thousands" then budget/1000
			else budget
		end budget_mn,
		case
			when unit="Billions" then revenue*1000
			when unit="Thousands" then revenue/1000
			else revenue
		end revenue_mn
		from financials
	) as t1
) as t2
right join movies m
on t2.movie_id = m.movie_id;


-- Task-4: Calculate profit of each movie (profit = revenue - budget) and print title & profit of each movie in descending order of profit.

select m.movie_id, m.title, round(t2.revenue_mn_inr - t2.budget_mn_inr, 0) as profit
from 
(
	select movie_id,
		if(currency="USD", budget_mn*80, budget_mn) as budget_mn_inr,
		if(currency="USD", revenue_mn*80, revenue_mn) as revenue_mn_inr
	from
	(
		select movie_id, currency,
		case
			when unit="Billions" then budget*1000
			when unit="Thousands" then budget/1000
			else budget
		end budget_mn,
		case
			when unit="Billions" then revenue*1000
			when unit="Thousands" then revenue/1000
			else revenue
		end revenue_mn
		from financials
	) as t1
) as t2
right join movies m
on m.movie_id = t2.movie_id
order by profit desc;