# Write your MySQL query statement below
-- with 사용
with base as(select requester_id as id from RequestAccepted
union all
select accepter_id as id from RequestAccepted)


select id, count(*) as num  from base group by 1 order by 2 desc limit 1