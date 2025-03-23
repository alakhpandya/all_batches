use moviesdb;

-- 25.	Print the top 5 movies according to their imdb_ratings
select *
from movies
order by imdb_rating desc
limit 5;

-- 26.	We have organized an award ceremony for these movies. Top 3 movies are getting the bumper prizes which have been already announced. 
-- Now we want to give condolence prizes to the movies which stood from rank 4th till 10th according to their imdb_rating. 
-- You are asked to print titles and ratings of these movies.

select *
from movies
order by imdb_rating desc, movie_id
limit 7
offset 3;

-- 27. Print the least, highest & average values of imdb_ratings rounded off after one decimal place
select min(imdb_rating) least_rating, max(imdb_rating) highest_rating, round(avg(imdb_rating), 1) as avg_rating
from movies;

-- 28.	Print the average imdb_rating of the “Vinod Chopra Films” studio
select avg(imdb_rating) 
from movies
where studio = "Vinod Chopra Films";

/*
29.	print the table in the following format:
id				title					release_year	imdb_rating		studio
101		K.G.F: Chapter 2 | Bollywood	2022			8.4				Hombale Films
*/

select movie_id, concat(title, " | ", industry) as title, release_year, imdb_rating, studio
from movies;

-- 30.	Print first character of title of each movie
select substr(title, 1, 1)
from movies;
-- there is no difference in substr() and substring() in mysql, see the official documentation: https://dev.mysql.com/doc/refman/5.7/en/string-functions.html

-- 31.	Print the titles of movies in a way that first character of title of every movie is capitalized and every other character in lower case.
select concat(upper(substr(title, 1, 1)), lower(substr(title, 2))) as new_title
from movies;

-- 32.	Replace all the null values in imdb_ratings column by 0.
-- select ifnull(imdb_rating, 0)
select coalesce(imdb_rating, 0)
from movies;

-- Give me the average rating of Bollywood movies
select avg(imdb_rating)
from movies
where industry = "Bollywood";

-- Print the average rating of Hollywood movies
select avg(imdb_rating)
from movies
where industry = "Hollywood";

-- Give me the average rating of each industry.
select industry, avg(imdb_rating)
from movies
group by industry;

-- Print the maximum ratings each industry has got.
select industry, max(imdb_rating)
from movies
group by industry;

-- Print maximum, minimum and average rating of each studio. 
-- Return your answer in such a way that the studio with highest average ratings appears first and the one with least average ratings goes at the end.
select studio, min(imdb_rating), max(imdb_rating), avg(imdb_rating)
from movies
where studio != ""
group by studio
order by 4 desc;

-- Print the number of movies produced by all those studio which have produced more than 2 movies
select studio, count(title)
from movies
group by studio
having count(title) > 2;

select studio, count(title)
from movies
where studio <> ""
group by studio
having count(title) > 2;