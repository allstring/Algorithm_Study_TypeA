-- 코드를 입력하세요
SELECT
    HOUR(datetime) AS hour,
    COUNT(*) AS count
FROM 
    animal_outs
WHERE 1 = 1
    AND HOUR(datetime) BETWEEN 9 AND 19
GROUP BY 
    hour
ORDER BY 
    HOUR(datetime) ASC;