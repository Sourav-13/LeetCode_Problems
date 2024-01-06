# Write your MySQL query statement below
SELECT class
FROM Courses c
GROUP BY class
HAVING count(student)>4