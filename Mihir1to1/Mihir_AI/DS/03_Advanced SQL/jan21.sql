use moviesdb;
select * from financials;
/*
Print a new table that has the following columns:
movie_id: as it is
USD_budget: converted in USD
USD_revenue: converted in USD
unit: as it is
*/
select movie_id,
-- CASE WHEN currency = "INR" THEN budget/80 ELSE budget END as USD_budget,
-- CASE WHEN currency = "INR" THEN revenue/80 ELSE revenue END as USD_revenue,
if(currency = "INR", budget/80, budget) as USD_budget,
if(currency = "INR", revenue/80, revenue) as USD_revenue,
unit
from financials;

/*
Print a new table that has the following columns:
movie_id: as it is
budget_Mn: budget in Millions
revenue_Mn: revenue in Millions
currency: as it is
*/