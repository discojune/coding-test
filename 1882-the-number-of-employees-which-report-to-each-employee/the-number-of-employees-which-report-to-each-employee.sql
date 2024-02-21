# Write your MySQL query statement below

select e3.employee_id,
e3.name,
count(*) as reports_count,
round(avg(e3.age), 0) as average_age
from (
    select e2.name, e2.employee_id, e.age
    from Employees as e
    left join Employees as e2
    on e.reports_to = e2.employee_id
) as e3
group by e3.employee_id
having e3.employee_id is not null and count(*) >= 1
order by e3.employee_id