-- Group by
-- Give me the average rating of Bollywood movies
select avg(imdb_rating) 
from movies
where industry="Bollywood";

-- Print the average rating of Hollywood movies
select avg(imdb_rating) 
from movies
where industry="Hollywood";

-- Give me the average rating of each industry.
select industry, avg(imdb_rating)
from movies
group by industry;

-- Practice Questions:
-- Print the maximum ratings each industry has got.
select industry, max(imdb_rating) as max_rating
from movies
group by industry;

/*
Print maximum, minimum and average rating of each studio. 
Return your answer in such a way that the studio with highest average ratings appears first and the one with least average ratings goes at the end.
*/
select studio, min(imdb_rating) as min_rating, max(imdb_rating) as max_rating, round(avg(imdb_rating), 1) as avg_rating
from movies
group by studio
order by 4 desc;

-- Remove that "null" studio from the above output
select studio, min(imdb_rating) as min_rating, max(imdb_rating) as max_rating, round(avg(imdb_rating), 1) as avg_rating
from movies
where studio <> ""
group by studio
order by 4 desc;

-- select > from > where > group by > order by > limit > offset

-- Print all the Bollywood movie studios with the release year of their last movie.
select studio, max(release_year) as last_movie
from movies
where industry = "Bollywood" and studio != ""
group by studio;

-- Print the number of movies produced by all those studio which have produced more than 2 movies
select studio, count(*) as no_of_movies
from movies
group by studio
having count(*) > 2;


select studio, count(*) as no_of_movies
from movies
where studio != ""
group by studio
having count(*) > 2;

-- select > from > where > group by > having > order by > limit > offset

-- Case/When
/*
Create a new column at the end of movies table from moviesdb & assign value 'old' to the movies which were released before 2000 & label 'new' to the rest of the movies.
*/
select *,
case
	when release_year < 2000 then "old"
	else "new"
end as movie_type
from movies;

select *,
if(release_year < 2000, "old", "new") as movie_type
from movies;

/*
From movies table, create a column named "Box Office Performance" which has type of movie based on its ratings as below:
	Less than 4 - flop    
	4 - 5.9 - Average    
	6 - 7.9 - Hit    
	8 or more - Blockbuster
*/

SELECT 
    *,
    CASE
        WHEN imdb_rating < 4 THEN 'Flop'
        WHEN imdb_rating BETWEEN 4 AND 5.9 THEN 'Average'
        WHEN imdb_rating BETWEEN 6 AND 7.9 THEN 'Hit'
        ELSE 'Blockbuster'
    END AS performance
FROM
    movies;
    
/*
In financials table, convert budget & revenue of each movie into millions and name the new columns as: budget_mn & revenue_mn
*/
select * from financials;

select movie_id, currency,
if(unit = "Billions", budget*1000, if(unit = "Thousands", budget/1000, budget)) as budget_mn,
if(unit = "Billions", revenue*1000, if(unit = "Thousands", revenue/1000, revenue)) as revenue_mn
from financials;

/*
In movies table of moviesdb dataset, Create a column named "Language" which has value: 
"Hindi" if language_id is 1, 
"English" if language_id is 5, 
“Tamil” if language_id is 4, 
“Bengali” if language_id is 7 
otherwise “Other”
*/
s


/*
In moviesdb, using ‘financials’ table print a new table that has the following columns:
movie_id: as it is
USD_budget: budget converted in USD
USD_revenue: revenue converted in USD
Unit: unit column as it is
*/