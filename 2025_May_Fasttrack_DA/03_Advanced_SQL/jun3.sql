-- 1.	Print and observe all the tables of moviesdb (understand the data)
-- 2.	Print title & industry of all movies from movies table
select title, industry from movies;

-- 3.	Print all the Bollywood movies from movies table
select *
from movies
where industry = "bollywood";

-- 4.	Print all the different industries present in the movies table
select distinct industry
from movies;

-- or
select distinct(industry)
from movies;

/*
5.	Suppose your query is going to produce result on the IMDB website based on user’s search. 
Return all the details of movies (all columns) if a user searches “Thor” on IMDB website search. 
Feel free to actually go on IMDB to check what it returns on the same search.
*/
select *
from movies
where title like "%Thor%";

-- 6.	Do the same (as in previous question) for a user who searches “Avenger”
select *
from movies
where title like "%Avenger%";

-- 7.	Give me movies with rating at least 8.
select * from movies
where imdb_rating >= 8;

-- 8.	Print names, ratings, industry and production studios of the movies which have got at least 5 ratings on imdb but have not got more than 9 ratings
select title, imdb_rating, industry, studio
from movies
-- where imdb_rating >= 5 and imdb_rating <= 9;
where imdb_rating between 5 and 9;

-- 9.	Give me all the details of the movies with rating between 1 to 4 (including both)
select *
from movies
where imdb_rating between 1 and 4;

-- 10.	Give me all the Bollywood movies with rating more than 7 (titles, ratings & studio)
select title, imdb_rating, studio
from movies
where industry = "bollywood" and imdb_rating > 7;

-- 11.	Print titles, ratings & studio of the Hollywood movies which have even movie_id & ratings above 7
select title, imdb_rating, studio
from movies
where industry = "hollywood" and movie_id % 2 = 0 and imdb_rating > 7;

-- 12.	Print titles & release_year of all the movies from Marvel Studios
select title, release_year
from movies
where studio = "Marvel Studios";

-- 13.	Print all the movies which have word “The” in them and have rating between 5 to 9 (including both)
select *
from movies
where title like "%the%" and imdb_rating between 5 and 9;

-- 14.	Print the year in which Godfather movie was released
select release_year
from movies
where title like "%Godfather%";

-- 15.	Print all the movie studios of Bollywood.
select distinct studio
from movies
where industry = "bollywood";

-- 16.	Give me all the movies released in the years 2015, 2016, 2017 or 2018.
select *
from movies
-- where release_year = 2015 or release_year = 2016 or release_year = 2017 or release_year = 2018;
where release_year between 2015 and 2018;

-- 17.	Print the number of Bollywood movies present in the movies table
-- select count(*) as no_of_movies
select count(*) no_of_movies
from movies
where industry = "bollywood";

-- 18.	Give me the total number of movies released in years 2013, 2017 & 2022
select count(*) as no_of_movies
from movies
where release_year in (2013, 2017, 2022);

-- 19.	Give me the movies for which imdb_rating is not available.
select *
from movies
where imdb_rating is null;

-- 20.	Give me only those movies for which imdb_ratings are available
select *
from movies
where imdb_rating is not null;

-- 21.	Print all the movies which were not released in the year 2022
select *
from movies
-- where release_year != 2022;
where release_year <> 2022;

-- 22.	Print the movies sorted by their year of release such that the older movies come at the top and latest at the bottom.
select *
from movies
order by release_year;

-- 23.	Print the movies sorted by their imdb_ratings in a way that the highest rated movie comes first and lowest rated last.
select *
from movies
order by imdb_rating desc;

/*
24.	Print the movies such that the oldest movies come first & latest last but 
in a particular year, they should be arranged so that the movie with highest imdb_rating is at the top & movie with least imdb_rating is at the bottom.
*/
select *
from movies
order by release_year asc, imdb_rating desc;

-- 25.	Print the top 5 movies according to their imdb_ratings
select *
from movies
order by imdb_rating desc
limit 5;

-- select > from > order by > limit

/*
26.	We have organized an award ceremony for these movies. 
Top 3 movies are getting the bumper prizes which have been already announced. 
Now we want to give condolence prizes to the movies which stood from rank 4th till 10th (including both) according to their imdb_rating. 
You are asked to print titles and ratings of these movies.
*/
select *
from movies
order by imdb_rating desc
limit 7
offset 3;

-- 27.	Print the least, highest & average values of imdb_ratings rounded off after one decimal place
select min(imdb_rating) as min_rating, max(imdb_rating) as max_rating, round(avg(imdb_rating), 1) as avg_rating
from movies;

-- 28.	Print the average imdb_rating of the “Vinod Chopra Films” studio
select avg(imdb_rating)
from movies
where studio = "Vinod Chopra Films";

/*
29.	print the table in the following format:
id	title							release_year	imdb_rating		studio
101	K.G.F: Chapter 2 | Bollywood	2022			8.4				Hombale Films
*/
select movie_id as id, concat(title, " | ", industry) as title, release_year, imdb_rating, studio
from movies;

-- 30.	Print first character of title of each movie
select substr(title, 1, 1) as first_char
from movies;

-- 31.	Print the titles of movies in a way that first character of title of every movie is capitalized and every other character in lower case.
select concat(upper(substr(title, 1, 1)), lower(substr(title, 2))) as new_title
from movies;

-- 32.	Replace all the null values in imdb_ratings column by 0.
select title, coalesce(imdb_rating, 0)
from movies;