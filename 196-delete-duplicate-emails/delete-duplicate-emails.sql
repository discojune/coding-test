# Write your MySQL query statement below
-- 참고: https://leetcode.com/problems/delete-duplicate-emails/solutions/2627589/my-sql-solution
delete p from Person as p, Person as p1
where p.email = p1.email and p.id > p1.id
