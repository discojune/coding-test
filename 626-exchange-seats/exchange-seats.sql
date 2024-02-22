# Write your MySQL query statement below
select s1.id,
case when mod(s1.id, 2) = 0 then s3.student
     else 
        case when s2.student is null then s1.student 
             else s2.student end
end as student
from Seat as s1
left join Seat as s2
on s1.id + 1 = s2.id
left join Seat as s3
on s1.id - 1 = s3.id