use as5;
select * from cinema;

select seat_id
from cinema
where free = 1 and
(
	seat_id in (
		select seat_id+1 from cinema where free=1
	) or
    seat_id in (
		select seat_id-1 from cinema where free=1
    )
);

use as8;
select * from matches;

with t1 as
(
	select *,
	row_number() over(partition by player_id order by match_day) as match_no,
	rank() over(partition by player_id, result order by match_day) as winning_no
	from matches
),
t2 as
(
	select *, match_no-winning_no as diff
	from t1
),
t3 as
(
	select player_id, result, diff, count(diff) as streaks
	from t2
	group by player_id, result, diff
),
t4 as
(
	select player_id, result, diff,
	case when result <> "Win" then 0 else streaks end as streaks
	from t3
)
select player_id, max(streaks)
from t4
group by player_id
order by player_id;