use moviesdb;

-- 25.	Print the top 5 movies according to their imdb_ratings
select *
from movies
order by imdb_rating desc, movie_id
limit 5;

/*
26.	We have organized an award ceremony for these movies. Top 3 movies are getting the bumper prizes which have been already announced. 
Now we want to give condolence prizes to the movies which stood from rank 4th till 10th according to their imdb_rating. 
You are asked to print titles and ratings of these movies.
*/

select *
from movies
order by imdb_rating desc, movie_id
limit 7
offset 3;

-- 27.	Print the least, highest & average values of imdb_ratings rounded off after one decimal place
select min(imdb_rating) as least_rating, max(imdb_rating) as highest_rating, round(avg(imdb_rating), 1) avg_rating
from movies;

-- 28.	Print the average imdb_rating of the “Vinod Chopra Films” studio
select avg(imdb_rating)
from movies
where studio = "Vinod Chopra Films";

/*
29.	print the table in the following format:
id		title							release_year	imdb_rating		studio
101		K.G.F: Chapter 2 | Bollywood	2022			8.4				Hombale Films
*/
select movie_id, concat(title, " | ", industry), release_year, imdb_rating, studio
from movies;

-- 30.	Print first character of title of each movie
-- select substring(title, 1, 1)
select substr(title, 1, 1)
from movies;

-- 31.	Print the titles of movies in a way that first character of title of every movie is capitalized and every other character in lower case.
select concat(upper(substr(title, 1, 1)), lower(substr(title, 2))) as new_title
from movies;

-- 32.	Replace all the null values in imdb_ratings column by 0.
-- select coalesce(imdb_rating, 0)
-- select ifnull(imdb_rating, 0)
-- select if(imdb_rating is null, 0, imdb_rating)
select case
	when imdb_rating is null then 0
    else imdb_rating
end as new_rating
from movies;

-- Give me the average rating of Bollywood movies
select avg(imdb_rating)
from movies
where industry = "bollywood";

-- Print the average rating of Hollywood movies
select avg(imdb_rating)
from movies
where industry = "hollywood";

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
where studio <> ""
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

-- Some common mistakes with group by
select title, industry, avg(imdb_rating)
from movies
group by industry;

use hr;
select * from employees;

select department_id, avg(salary)
from employees
group by department_id;

select first_name, avg(salary)
from employees
group by first_name;

select first_name, last_name, avg(salary)
from employees
group by first_name, last_name;