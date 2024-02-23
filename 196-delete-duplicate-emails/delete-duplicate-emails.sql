# Write your MySQL query statement below
delete p from Person as p, Person as p1
where p.email = p1.email and p.id > p1.id
