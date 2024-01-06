# Write your MySQL query statement below
SELECT e.name Employee
from Employee e INNER JOIN Employee m on e.managerId=m.id
WHERE e.salary> m.salary