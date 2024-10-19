use as7;
select * from genders;
select *,
ntile(3) over(partition by gender) as groop
from genders
order by 3;

select *
from genders
order by ntile(3) over(partition by gender);

with cte as
(
	select *,
	case 
		when gender = "female" then 1
		when gender = "other" then 2
		when gender = "male" then 3
	end as groop
	from genders
)
select user_id, gender
from cte
order by ntile(3) over(partition by groop);