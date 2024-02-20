# Write your MySQL query statement below
-- join이 되지 않는 경우에 대한 예외처리 필요
select p.product_id, ifnull(round(sum(p.price * u.units) / sum(u.units), 2), 0) as average_price
from Prices as p left join UnitsSold as u
-- join이 발생하는 조건을 명시
on p.product_id = u.product_id and u.purchase_date between p.start_date and p.end_date 
group by p.product_id