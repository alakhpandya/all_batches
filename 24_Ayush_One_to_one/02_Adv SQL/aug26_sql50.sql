use sql50;
drop table if exists transactions;
Create table If Not Exists Transactions (id int, country varchar(4), state enum('approved', 'declined'), amount 
int, trans_date date);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values ('121', 'US', 'approved', '1000', '2018-12-18');
insert into Transactions (id, country, state, amount, trans_date) values ('122', 'US', 'declined', '2000', '2018-12-19');
insert into Transactions (id, country, state, amount, trans_date) values ('123', 'US', 'approved', '2000', '2019-01-01');
insert into Transactions (id, country, state, amount, trans_date) values ('124', 'DE', 'approved', '2000', '2019-01-07');

select * from transactions;

with t1 as
(
	select id, country, state, amount, substr(trans_date, 1, 7) as month
    from transactions
),
t2 as
(
	select month, country, count(*) as trans_count from t1 group by month, country
),
t3 as
(
	select month, country, count(state) as approved_count from t1 
    where state = "approved"
    group by month, country
),
t4 as
(
	select month, country, sum(amount) as trans_total_amount
    from t1 group by month, country
),
t5 as
(
	select month, country, sum(amount) as approved_total_amount
    from t1 where state = "approved"
    group by month, country
)

select t2.month, t2.country, t2.trans_count, t3.approved_count, t4.trans_total_amount, t5.approved_total_amount
from t2
join t3 on t2.month = t3.month and t2.country = t3.country
join t4 on t3.month = t4.month and t3.country = t4.country
join t5 on t3.month = t5.month and t3.country = t5.country;
