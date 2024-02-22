# Write your MySQL query statement below
select min(name) as results
from
(select name,
user_rating.rating_counts as rating
from Users as u
left join 
(select user_id, count(rating) as rating_counts from MovieRating group by user_id) as user_rating
on u.user_id = user_rating.user_id) 
as temp1
-- from 으로 사용할 테이블은 alias가 필요하다
where temp1.rating = (select max(rating_counts) from (select user_id, count(rating) as rating_counts from MovieRating group by user_id) as t)
-- 중복된 값을 모두 합치는 명령
union all
select min(title) as results
from
(select m.movie_id, m.title, avg_mr.avg_rating
from Movies as m
left join 
(select movie_id, avg(rating) as avg_rating
from MovieRating
where DATE_FORMAT(created_at,'%Y-%m') = '2020-02'
group by movie_id) as avg_mr
on m.movie_id = avg_mr.movie_id) as temp2
where temp2.avg_rating = (select max(avg_rating) from (select movie_id, avg(rating) as avg_rating from MovieRating where DATE_FORMAT(created_at,'%Y-%m') = '2020-02' group by movie_id) as t)

