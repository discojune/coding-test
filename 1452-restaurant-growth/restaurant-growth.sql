# Write your MySQL query statement below
-- data_sub, date_add를 통해 window 생성
select visited_on,
(
    select sum(amount)
    from Customer
    where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on -- 메인 쿼리의 값을 c를 통해 가져와 서브 쿼리 생성
) as amount,
(
    select round(sum(amount) / 7, 2)
    from Customer
    where visited_on between date_sub(c.visited_on, interval 6 day) and c.visited_on
) as average_amount
from Customer as c
-- window의 가장 처음 날짜를 min으로 끝이 되는 날짜는 min 날짜 + 6일 이후의 값으로 설정할 수 있다.
where visited_on >= (
    select date_add(min(visited_on), interval 6 day)
    from Customer
)
group by visited_on