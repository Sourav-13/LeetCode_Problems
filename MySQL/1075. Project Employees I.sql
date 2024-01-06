# Write your MySQL query statement below

SELECT project_id, ROUND(AVG(experience_years),2) average_years
FROM Project p INNER JOIN Employee e on p.employee_id = e.employee_id
GROUP BY project_id