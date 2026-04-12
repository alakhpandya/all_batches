/*
Print maximum, minimum and average rating of each studio. 
Return your answer in such a way that the studio with highest average ratings appears first and the one with least average ratings goes at the end. 
*/
use moviesdb;
select studio, max(imdb_rating)
from movies
-- group by title, studio;
group by studio;

/*
select studio, title, imdb_rating
from movies
order by studio, title;
*/

-- Remove "null" studio from the previous query
select studio, max(imdb_rating)
from movies
where studio <> ""
group by studio;

-- Find release years in which more than 2 movies were released.
select release_year, count(*)
from movies
group by release_year
having count(*) > 2;

-- Print all the studios which have released at least two movies (excluding empty studios)
select studio
from movies
where studio <> ""
group by studio
having count(*) >= 2;

-- Print all the Bollywood movie studios with the release year of their last movie.
select studio, max(release_year)
from movies
where studio <> "" and industry = "Bollywood"
group by studio;

-- Display all non-repeating release years from the movies table.
select release_year
from movies
group by release_year
having count(*) = 1;

/*
Print all the columns of movies table along with a new column at the end from moviesdb dataset & assign value 'old' to the movies 
which were released before 2000 & label 'new' to the rest of the movies.
*/
select *,
-- if(release_year < 2000, "Old", "New") as "Type"
case
	when release_year < 2000 then "Old"
    else "New"
end as "Type"
from movies;

-- In financials table, convert budget & revenue of each movie into millions and name the new columns as: budget_mn & revenue_mn
select *, 
case
	when unit = "Billions" then budget*1000
    when unit = "Thousands" then budget/1000
    else budget
end as budget_mn,
if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as revenue_mn
from financials;

/*
From movies table, create a column named "Box Office Performance" which has type of movie based on its ratings as below:
	Less than 4 - flop    
	4 - 5.9 - Average    
	6 - 7.9 - Hit    
	8 or more - Blockbuster
*/
select *,
case
	when imdb_rating < 4 then "Flop"
    when imdb_rating between 4 and 5.9 then "Average"
    when imdb_rating between 6 and 7.9 then "Hit"
    when imdb_rating is null then "N/A"
    else "Blockbuster"
end as "Box Office Performance"
from movies