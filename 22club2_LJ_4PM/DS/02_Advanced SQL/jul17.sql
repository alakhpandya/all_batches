use moviesdb;
/*
select * from movies;
select studio, count(*)
from movies
-- where industry = "Hollywood"
group by studio;
*/
/*
select -> from -> where -> group by -> having -> order by

select studio, count(imdb_rating)
from movies
group by studio;
*/
/*
select *, if(unit = "Billions", budget*1000, if(unit = "Thousands", budget/1000, budget)) as new_budget,
if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as new_revenue
from financials;
*/

/*
-- select *, if(imdb_rating >= 7, "Hit", "Average") as review
select *, if(imdb_rating >= 7, "Hit", if(imdb_rating < 4, "Flop", "Average")) as review
from movies;
*/

select *, 
if(unit = "Billions", budget*1000, if(unit = "Thousands", budget/1000, budget)) as new_budget,
if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as new_revenue,
if(currency = "USD", new_budget*80, new_budget) as adj_budget,
if(currency = "USD", new_revenue*80, new_revenue) as adj_revenue
from financials;

-- Subquery
select *,
if(currency = "USD", new_budget*80, new_budget) as adj_budget,
if(currency = "USD", new_revenue*80, new_revenue) as adj_revenue
from
(
	select *, 
	if(unit = "Billions", budget*1000, if(unit = "Thousands", budget/1000, budget)) as new_budget,
	if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as new_revenue
	from financials
) as t1;

-- Create a column of "Profit" that is in Million INR and print movie titles, imdb_rating, studio, industry, profit and performance columns where performance is "Block Buster"
-- if the profit is more than 100 Cr, Hit if the profit is between 50 Cr to 100 Cr, Average if between 10 Cr to 50 Cr otherwise flop.