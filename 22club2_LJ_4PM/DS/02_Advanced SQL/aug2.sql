use as7;
select * from data;

SELECT FIRST_COL,SECOND_COL 
FROM DATA 
ORDER BY FIRST_COL ASC,SECOND_COL DESC;
    
with t1 as
(

	select row_number() over() as row1, first_col, second_col
	from data
	order by first_col
),
t2 as
(
	select *, row_number() over() as row2
	from data
	order by second_col desc
)
select t1.first_col, t2.second_col
from t1
join t2 on t1.row1 = t2.row2;

-- Print title, imdb_rating, studio of top 3 (in terms of their imdb_rating) movies of each studio
use moviesdb;
select * from movies;
