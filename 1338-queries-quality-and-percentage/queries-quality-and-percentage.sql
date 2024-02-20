# Write your MySQL query statement below
select q.query_name, 
round(sum(q.rating / q.position) / count(q.position), 2) as quality, 
round(sum(case when q.rating < 3 then 1 else 0 end) / count(q.position) * 100, 2) as poor_query_percentage
from Queries as q
where q.query_name is not null
group by q.query_name