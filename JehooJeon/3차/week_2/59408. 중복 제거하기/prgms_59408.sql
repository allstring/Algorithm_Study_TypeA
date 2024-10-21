-- 코드를 입력하세요
SELECT
    COUNT(DISTINCT name) AS count
FROM 
    animal_ins
WHERE 1 = 1
    AND name IS NOT NULL;