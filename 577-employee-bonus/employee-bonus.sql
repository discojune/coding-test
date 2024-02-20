# Write your MySQL query statement below
select emp.name, bonus.bonus
from Employee as emp left join Bonus as bonus
on emp.empId = bonus.empId
where bonus.bonus < 1000 or bonus.bonus is null