# Write your MySQL query statement below
select employee_id, department_id
from Employee
-- where에 속하는 모든 조건을 다 select 한다
where primary_flag = 'Y' or employee_id in (select employee_id from Employee group by employee_id having count(*) = 1)