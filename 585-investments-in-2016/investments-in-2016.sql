# Write your MySQL query statement below
-- tiv_2015가 같은 placeholder가 없는 경우 제외
-- 중복되는 위치가 있는 경우 제외
select round(sum(tiv_2016), 2) as tiv_2016
from Insurance as i
where
tiv_2015 in (select tiv_2015 from Insurance where pid != i.pid)
and
(lat, lon) not in (select lat, lon from Insurance where pid != i.pid)