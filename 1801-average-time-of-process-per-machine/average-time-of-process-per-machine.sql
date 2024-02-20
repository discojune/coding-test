# Write your MySQL query statement below
select act1.machine_id, round(avg(act2.timestamp - act1.timestamp), 3) as processing_time
from Activity as act1 join Activity as act2
on act1.machine_id = act2.machine_id and act1.process_id = act2.process_id and
act1.activity_type = 'start' and act2.activity_type = 'end'
group by Act1.machine_id