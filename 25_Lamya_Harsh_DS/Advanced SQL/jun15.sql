-- Print the average rating of Bollywood movies
use moviesdb;
select avg(imdb_rating) 
from movies
where industry = "Bollywood";

-- Print the average rating of Hollywood movies
select avg(imdb_rating) 
from movies
where industry = "Hollywood";

-- Give me the average rating of each industry.
select industry, studio, avg(imdb_rating)
from movies
group by industry, studio;

select industry, avg(imdb_rating), min(release_year), max(release_year)
from movies
group by industry;

/*
Print maximum, minimum and average rating of each studio. 
Return your answer in such a way that the studio with highest average ratings appears first and the one with least average ratings goes at the end.
*/


/*
Create a new column at the end of movies table from moviesdb & assign value 'old' to the movies which were released before 2000 & label 'new' to the rest of the movies.
*/
select *,
if(release_year < 2000, "old", "new") as version
from movies;


/*
From movies table, create a column named "Box Office Performance" which has type of movie based on its ratings as below:
	Less than 4 - flop    
	4 - 5.9 - Average    
	6 - 7.9 - Hit    
	8 or more - Blockbuster
*/

-- In financials table, convert budget & revenue of each movie into millions and name the new columns as: budget_mn & revenue_mn
select *,
if(unit = "Billions", budget*1000, if(unit = "Thousands", budget/1000, budget)) budget_mn,
if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) revenue_mn
from financials;
