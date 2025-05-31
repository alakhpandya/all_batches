use temp;
create table articles (
article_id int primary key auto_increment,
title varchar(50) DEFAULT "Untitled",
date_created TIMESTAMP,
date_published TIMESTAMP default CURRENT_TIMESTAMP
);

insert into articles (date_created)
values ("2024-02-24	00:00:01");

-- set time_zone = "+00:00";
set time_zone = "+05:30";

select * from articles;

-- JOINS:
/*
inner join
left join
right join
full outer join
self join
cross join
*/