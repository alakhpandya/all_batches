use moviesdb;

-- Print the number of movies produced by all those studio which have produced more than 2 movies
select studio, count(title)
from movies
group by studio
having count(title) > 2;

select studio, max(release_year), count(title)
from movies
where industry = "Bollywood" and studio != ""
group by studio
having count(title) >= 2
order by studio;

/*
Create a new column at the end of movies table from moviesdb & assign value 'old' to the movies which were released before 2000 & label 'new' to the rest of the movies.
*/
select *, if(release_year < 2000, "old", "new") as movie_type
from movies;

select *, if(imdb_rating < 4, "flop", if(imdb_rating < 8, "hit", "block buster")) as box_office
from movies;


select *,
case
	when imdb_rating < 4 then "flop"
    when imdb_rating between 4 and 7 then "hit"
    else "block buster"
end as box_office
from movies;