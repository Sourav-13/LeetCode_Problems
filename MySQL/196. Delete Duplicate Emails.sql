# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

DELETE FROM Person
WHERE id NOT IN (select * from (
                SELECT MIN(id)
                FROM Person    
                GROUP BY email
                HAVING COUNT(email)=1 OR COUNT(email)>1
                ORDER BY id
) as t)