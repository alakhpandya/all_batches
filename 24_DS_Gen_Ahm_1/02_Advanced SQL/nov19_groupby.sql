use moviesdb;

-- title, industry, industry_avg
/*
KGF					B	7.7
The Godfather		H	8.2
The Dark Knight		H	8.2
3 Idiots			B	7.7
*/

select industry, min(imdb_rating), max(imdb_rating), min(release_year), max(release_year), count(*)
from movies
group by industry;


use final_hr;

select first_name, last_name, count(first_name) as cnt
from employees
group by first_name, last_name
order by 2 desc;

use moviesdb;
-- 39. Print the number of movies produced by all those studio which have produced more than 2 movies
select studio, count(*)
from movies
where studio != ""
group by studio
having count(*) > 2;