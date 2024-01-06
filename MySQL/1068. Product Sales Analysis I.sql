# Write your MySQL query statement below
select product_name , year  , price
from Sales s left outer join Product p on s.product_id = p.product_id
