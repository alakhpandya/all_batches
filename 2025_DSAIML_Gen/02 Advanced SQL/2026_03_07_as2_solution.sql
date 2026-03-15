use as2;

-- Q-1:
select * 
from cinema
where id % 2 != 0 and description not like "%boring%";

-- Q-3:
select *, round(salary * 1.2, 0) as new_salary
from employees;

-- Q-4:
select original_title
from movies
where release_year > 2014 and vote_average > 7
order by original_title;

-- Q-5:
select original_title, director, genres, cast, budget, revenue, runtime, vote_average
from movies
where keywords like '%sport%' or 
keywords like '%sequel%' or 
keywords like '%suspense%';

-- Q-6:
select original_title, popularity
from movies
where genres like "%Horror%"
order by popularity desc;

-- Q-7:
select original_title, genres, vote_average, revenue
from movies
where release_year between 2012 and 2015
order by 1;

-- Q-8:
select original_title, round( 
	(vote_count / (vote_count + 104) * vote_average) + (104 / (104 + vote_count) * 5.97)
,2) as Weighted_avg_rating
from movies
order by 2 desc
limit 10;