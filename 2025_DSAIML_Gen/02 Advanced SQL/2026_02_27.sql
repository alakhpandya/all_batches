-- 27.	Print the least, highest & average values of imdb_ratings rounded off after one decimal place
use moviesdb;

select min(imdb_rating) min_rating, max(imdb_rating) max_rating, round(avg(imdb_rating), 1) avg_rating
from movies;

-- 28.	Print the average imdb_rating of the “Vinod Chopra Films” studio
select round(avg(imdb_rating), 1)
from movies
where studio = "Vinod Chopra Films";

/*
29.	print the table in the following format:
id		title								release_year	imdb_rating		studio
101		K.G.F: Chapter 2 | Bollywood		2022			8.4				Hombale Films
*/

select movie_id as id, 
concat(title, " | ", industry),  release_year, imdb_rating, studio
from movies;

-- 30.	Print only the first character of title of each movie
-- select substr(title, 3, 5)
select substr(title, 1, 1) new_title
from movies;

-- 31.	Print the titles of movies in a way that first character of title of every movie is capitalized and every other character in lower case.
select concat(upper(substr(title, 1, 1)), lower(substr(title, 2))) new_title
from movies;

-- 32.	Replace all the null values in imdb_ratings column by 0.
select movie_id, title, coalesce(imdb_rating, 0)
from movies;

-- 33. Print the average rating of Bollywood industry
select industry, avg(imdb_rating)
from movies
where industry = "Bollywood";

-- 34. Print the average rating of Hollywood industry
select avg(imdb_rating)
from movies
where industry = "Hollywood";

-- 35. Get me the average ratings (rounded off by 1 dp) of Bollywood and Hollywood seperately
select industry, round(avg(imdb_rating), 1) as avg_rating
from movies
group by industry;

-- 36. Print the maximum ratings each industry has got.
select industry, max(imdb_rating)
from movies
group by industry;

/*
Print maximum, minimum and average rating of each studio. 
Return your answer in such a way that the studio with highest average ratings appears first and the one with least average ratings goes at the end.
*/
select studio, min(imdb_rating), max(imdb_rating), round(avg(imdb_rating), 1)
from movies
group by studio
order by 4 desc;

-- Remove null from the result of the previous query.
select studio, min(imdb_rating), max(imdb_rating), round(avg(imdb_rating), 1)
from movies
where studio != ""
group by studio
order by 4 desc;

-- Print the number of movies produced by all those studio which have produced more than 2 movies
select studio, count(*)
from movies
group by studio
having count(*) > 2;


select studio, count(*)
from movies
where studio != ""
group by studio
having count(*) > 2
order by 2 desc;

-- Print all the Bollywood movie studios with the release year of their last movie.
select studio, max(release_year)
from movies
where industry = "Bollywood"
group by studio;

-- Print the number of movies produced by all those Hollywood studios which have produced more than 2 movies
select studio, count(*)
from movies
where industry = "Hollywood"
group by studio
having count(*) > 2;