# Write your MySQL query statement below

select e2.employee_id,
e2.name,
count(*) as reports_count,
round(avg(e.age), 0) as average_age
from Employees as e
left join Employees as e2
on e.reports_to = e2.employee_id
group by e2.employee_id
having e2.employee_id is not null and count(*) >= 1
order by e2.employee_id