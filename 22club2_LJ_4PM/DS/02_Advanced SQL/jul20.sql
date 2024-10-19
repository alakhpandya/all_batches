/*

*/
use moviesdb;
SELECT title, adj_revenue, adj_budget, profit, 
CASE WHEN PROFIT BETWEEN 50 AND 100 THEN 'HIT'
	 WHEN PROFIT BETWEEN 10 AND 50 THEN 'AVERAGE'
     ELSE 'FLOP' END AS POPULARITY 
FROM 
	(SELECT *, ADJ_REVENUE - ADJ_BUDGET "PROFIT" FROM 
		(SELECT *, 
		IF(CURRENCY = 'USD', REVENUE * 80, REVENUE) AS ADJ_REVENUE,
		IF(CURRENCY = 'USD', BUDGET * 80, BUDGET ) AS ADJ_BUDGET
		FROM 
			(SELECT M.TITLE "TITLE" , M.INDUSTRY "INDUSTRY" , M.IMDB_RATING "IMDB" , M.STUDIO "STUDIO", F.CURRENCY "CURRENCY",F.UNIT "UNIT",F.REVENUE "REVENUE",
				CASE WHEN UNIT='BILLIONS' THEN REVENUE * 1000 
				ELSE REVENUE END AS UPD_REVENUE,
				F.BUDGET,
				CASE WHEN UNIT='BILLIONS' THEN BUDGET * 1000 
				ELSE BUDGET  END AS UPD_BUDGET
			FROM MOVIES M 
			INNER JOIN FINANCIALS F
			ON M.MOVIE_ID = F.MOVIE_ID) AS T1)
		AS T2)
AS T3;

-- C.T.E. - Common Table Expression
with t1 as
(
	select movie_id, currency, if(unit = "billions", budget*1000, if(unit = "thousands", budget/1000, budget)) as new_budget,
	if(unit = "billions", revenue*1000, if(unit = "thousands", revenue/1000, revenue)) as new_revenue
	from financials
),
t2 as
(
	select movie_id, if(currency = "USD", new_budget*80, new_budget) as adj_budget, if(currency = "USD", new_revenue*80, new_revenue) as adj_revenue 
	from t1
)
select * from t2;

/*
Find the most profitable orders. Orders which have higher sells price than the average sales price 
for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’ (Use ‘demo’ database)
*/
use demo;
with t1 as 
(
	select order_number, sales, deal_size,  city
	from sales_order so
	join customers c
	on c.customer_id = so.customer
	where deal_size <> "Small"
),
t2 as
(
	select city, avg(sales) as avg_sales
    from t1
    group by city
)
select t1.order_number, t1.sales, t1.city, t2.avg_sales
from t1
join t2 on t1.city = t2.city
where t1.sales > t2.avg_sales;