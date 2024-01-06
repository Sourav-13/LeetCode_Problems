# Write your MySQL query statement below
SELECT name, bonus 
FROM Employee e left outer join Bonus b ON e.empId=b.empId
WHERE bonus<1000 or bonus is null