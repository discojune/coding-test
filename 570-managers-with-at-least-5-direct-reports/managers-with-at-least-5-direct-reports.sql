# Write your MySQL query statement below
select emp.name
from Employee as emp
left join
(select emp2.managerID, count(emp2.managerID) as direct_reports from Employee as emp2 group by managerID) as emp2
on emp.id = emp2.managerID
where emp2.direct_reports >= 5
