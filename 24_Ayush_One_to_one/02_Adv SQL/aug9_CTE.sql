/*
Print the movie titles, industry and revenue. Sort the result in descending order of profit. 
Clean the revenue & budget so that it becomes easy to compare the profit each movie did 
(Hint: both of them must be in the same currency and in the same unit (thousand/million/billion etc) to compute the profit.)
•Use of IF(currency = “USD”, revenue*80, revenue) as revenue_INR
•Use case when to get all units in millions
*/

use moviesdb;
select * from financials;
select movie_id,
round(case
	when currency = "USD" then budget_mn * 80
    else budget_mn
end, 2) as budget_inr_mn,
round(if(currency = "USD", revenue_mn*80, revenue_mn), 2) as revenue_inr_mn
from
(
	select movie_id,
	case
		when unit = "Billions" then budget*1000
		when unit = "Thousands" then budget/1000
		else budget
	end as budget_mn,
	case
		when unit = "Billions" then revenue*1000
		when unit = "Thousands" then revenue/1000
		else revenue
	end as revenue_mn,
	currency
	from financials
) as t1;


/*
Find the most profitable orders. 
Orders which have higher sells price than the average sales price for their city and for which the deal size is not small are considered as ‘Most Profitable Orders’
*/

-- C.T.E. : Common Table Expression

use demo;

select c.city, avg(so.sales) as avg_city_sales
from sales_order so
join customers c
on so.customer = c.customer_id
group by c.city;

use hr2;
/*
Based on the employee's salary, divide the employees into three different classes.
1. Salary greater than 20,000 (i.e, excluding 20,000) as 'Class A'
2. Salary between 10,000 to 20,000 (i.e, including both 10,000 and 20,000) as 'Class B'
3. Salary less than 10,000 (i.e, excluding 10,000) as 'Class C'. Return the new column as 'Salary_bin'.
• Return the columns 'employee_id', 'salary', and 'Salary_bin'.
• Return the result ordered by employee_id in ascending order.

Print the employees those belong to class C only.
*/

with t1 as
(
	select employee_id, first_name, last_name, salary,
	case
		when salary < 10000 then "Class C"
		when salary >= 10000 and salary <= 20000 then "Class B"
		else "Class A"
	end as salary_bin
	from employees
)
select *
from t1
where salary_bin = "Class B";