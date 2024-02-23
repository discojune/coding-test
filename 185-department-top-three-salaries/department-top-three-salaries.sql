# Write your MySQL query statement below
with base as
(
    select e.departmentId, d.name as department, e.name, e.salary, e.salary_rank
    from 
    (select id, name, salary, departmentId, dense_rank() over (partition by departmentId order by salary desc) as salary_rank from Employee) as e
    left join Department as d
    on e.departmentId = d.id
    order by e.departmentId asc, e.salary desc
)

-- department마다 세번째로 큰 연봉 참기, dense_rank, partition by 사용법 / nth_value도 참고
select department as Department, name as Employee, salary as Salary
from base
where salary_rank <= 3
