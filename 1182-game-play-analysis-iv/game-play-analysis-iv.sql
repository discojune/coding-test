# Write your MySQL query statement below
select round(count(distinct a2.player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from 
(
    select player_id, min(event_date) as event_date
    from Activity
    group by player_id
) as a1
left join Activity as a2
on a1.player_id = a2.player_id and datediff(a2.event_date, a1.event_date) = 1